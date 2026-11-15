"""One transactional task store shared by the local UI and CLI. Standard library only."""
import copy
import hashlib
import json
import os
import re
import tempfile
import time
from contextlib import contextmanager
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

STATUSES = ('Backlog', 'To do', 'In progress', 'Review', 'Done')
PRIORITIES = ('Low', 'Normal', 'High')
FIELDS = {'title', 'description', 'owner', 'assigned_by', 'assignment_note', 'sources',
          'status', 'priority', 'start', 'end', 'deadline', 'dependencies', 'order', 'archived'}
MANILA = timezone(timedelta(hours=8))


class StoreError(Exception):
    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix='.' + path.name + '-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


@contextmanager
def lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+b') as stream:
        if path.stat().st_size == 0:
            stream.write(b'0')
            stream.flush()
        start = time.monotonic()
        while True:
            try:
                stream.seek(0)
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except (OSError, BlockingIOError):
                if time.monotonic() - start > 5:
                    raise StoreError('Another task save is busy. Please retry.', 409)
                time.sleep(.05)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == 'nt':
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


def cell(value):
    # HTML is never executed by the app; Markdown cells remain structurally valid.
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\n', '<br>')


class Store:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.kb = self.root / 'knowledge-base'
        self.path = self.kb / 'tasks.json'
        self.lockpath = self.root / 'app' / '.runtime' / 'tasks.lock'

    def projections(self, state):
        lines = ['# Tasks and next steps', '', '> Generated from tasks.json. Use the app or task helper to edit tasks; manual edits are detected and preserved for reconciliation.', '',
                 '## Dated task register', '', '| ID | Task | Owner | Assigned by | Status | Priority | Planned dates | Hard deadline | Evidence |',
                 '|---|---|---|---|---|---|---|---|---|']
        for task in sorted(state['tasks'], key=lambda t: (t['order'], t['id'])):
            dates = task['start'] or 'Unscheduled'
            if task['end'] and task['end'] != task['start']:
                dates += ' to ' + task['end']
            evidence = ', '.join(f'[{Path(s).stem}]({s})' for s in task['sources'])
            lines.append('| ' + ' | '.join([cell(task['id']), cell(task['title']), cell(task['owner']), cell(task['assigned_by']),
                         cell(('Archived / ' if task['archived'] else '') + task['status']), cell(task['priority']), cell(dates), cell(task['deadline'] or 'None stated'), evidence]) + ' |')
        lines += ['', 'Planned dates use Asia/Manila. Done means user-reported completion, not Alex approval.', '', '## Task details', '']
        for task in state['tasks']:
            lines += [f"### {task['id']}", '', cell(task['description']), '', 'Assignment context: ' + cell(task['assignment_note']),
                      'Dependencies: ' + cell(', '.join(task['dependencies']) or 'None recorded'), '']
            for note in task['notes']:
                lines += ['- ' + cell(note['at'] + ' — ' + note['text'])]
        lines += ['', '## Live task history', '', '[Task event evidence](sources/task-events.md). Existing source archives and earlier ID mappings are preserved below.', '', state['legacy_markdown']]
        events = ['# Task event evidence', '', 'Generated from the append-only events in tasks.json. Each EVT ID is stable. UI events are user reports, not independent completion verification.', '']
        for event in state['events']:
            events += [f"## {event['id']}", '', f"- Author: {event['actor']}", f"- Original/intake time: {event['at']}",
                       f"- Subject: {event['action']} {event['task_id']}", '- Type: Task change / user report', '', '```json',
                       json.dumps({k: event[k] for k in ('request', 'before', 'after')}, ensure_ascii=False, indent=2), '```', '']
        return {'tasks.md': ('\n'.join(lines) + '\n').encode(), 'sources/task-events.md': ('\n'.join(events) + '\n').encode()}

    def validate_task(self, task):
        for field in ('title', 'description', 'owner', 'assigned_by', 'assignment_note'):
            if not isinstance(task.get(field), str) or len(task[field]) > 20000:
                raise StoreError(f'Invalid {field}.')
        if not task['title'].strip() or not task['owner'].strip():
            raise StoreError('Title and owner are required.')
        if task['status'] not in STATUSES or task['priority'] not in PRIORITIES:
            raise StoreError('Unknown status or priority.')
        if task['assigned_by'] not in ('You', 'Alex', 'Unknown', 'Assistant suggestion'):
            raise StoreError('Unknown assignment attribution.')
        for field in ('start', 'end', 'deadline'):
            if task[field] is not None:
                try:
                    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', task[field]):
                        raise ValueError()
                    date.fromisoformat(task[field])
                except (ValueError, TypeError):
                    raise StoreError(f'{field} must be a valid YYYY-MM-DD date.')
        if task['end'] and (not task['start'] or task['end'] < task['start']):
            raise StoreError('End date must be on or after the start date.')
        if task['status'] == 'Backlog' and (task['start'] or task['end']):
            raise StoreError('Backlog tasks must be unscheduled.')
        if type(task['archived']) is not bool or type(task['order']) is not int or abs(task['order']) > 10**12:
            raise StoreError('Invalid archive flag or ordering.')
        for field in ('sources', 'dependencies'):
            if not isinstance(task[field], list) or not all(isinstance(x, str) for x in task[field]):
                raise StoreError(f'{field} must be a list of strings.')
        for source in task['sources']:
            path = (self.kb / source.split('#')[0]).resolve()
            if not re.fullmatch(r'sources/[A-Za-z0-9_.-]+\.md(?:#[a-z0-9-]+)?', source) or not path.is_relative_to(self.kb / 'sources') or not path.is_file():
                raise StoreError('Source must reference an existing knowledge-base source Markdown file.')
        if task['assigned_by'] == 'Alex' and not (task['sources'] or task['assignment_note'].strip()):
            raise StoreError('Describe or link Alex’s assignment. A report is labeled user-reported, not verified approval.')
        if type(task['revision']) is not int or task['revision'] < 0 or not isinstance(task['notes'], list):
            raise StoreError('Invalid task revision or notes.')
        for note in task['notes']:
            if not isinstance(note, dict) or any(not isinstance(note.get(k), str) for k in ('text', 'at', 'actor')):
                raise StoreError('Invalid task note.')
        if task['completed_at'] is not None and not isinstance(task['completed_at'], str):
            raise StoreError('Invalid completion time.')

    def load(self):
        try:
            raw = self.path.read_bytes()
            state = json.loads(raw)
            if state['schema'] != 1 or type(state['revision']) is not int:
                raise ValueError('Unsupported schema')
            ids = set()
            for task in state['tasks']:
                self.validate_task(task)
                if not re.fullmatch(r'T-\d{3,}', task['id']) or task['id'] in ids:
                    raise ValueError('Duplicate or invalid task ID')
                ids.add(task['id'])
            if state['next_id'] <= max([int(x[2:]) for x in ids] or [0]):
                raise ValueError('Invalid next ID')
            if not isinstance(state['events'], list) or not isinstance(state['legacy_markdown'], str) or not isinstance(state['legacy'], list):
                raise ValueError('Invalid history')
            if set(state['projection_before']) != {'tasks.md', 'sources/task-events.md'}:
                raise ValueError('Invalid projection recovery metadata')
            for index, event in enumerate(state['events'], 1):
                if event['id'] != f'EVT-{index:06}' or not all(key in event for key in ('actor','at','action','task_id','request','before','after','operation_id','request_hash')):
                    raise ValueError('Invalid task event history')
            return state, digest(raw)
        except StoreError:
            raise
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise StoreError('Task store cannot be read safely. Restore or reconcile tasks.json: ' + str(error), 503)

    def recover(self, state):
        outputs = self.projections(state)
        # Check every target before writing any, so manual edits are never overwritten.
        for name, content in outputs.items():
            target = self.kb / name
            current = digest(target.read_bytes()) if target.exists() else None
            if current not in (digest(content), state['projection_before'].get(name)):
                raise StoreError(f'{name} was edited outside the task store. Preserve those edits and reconcile them before saving. See app/docs/usage.md.', 409)
        for name, content in outputs.items():
            target = self.kb / name
            if not target.exists() or target.read_bytes() != content:
                atomic(target, content)

    def snapshot(self):
        with lock(self.lockpath):
            state, token = self.load()
            self.recover(state)
            return dict(state, token=token)

    def command(self, request):
        if not isinstance(request, dict):
            raise StoreError('Expected a JSON object.')
        operation = request.get('operation_id', '')
        if not isinstance(operation, str) or not re.fullmatch(r'[A-Za-z0-9-]{8,100}', operation):
            raise StoreError('A unique operation_id (8–100 letters, digits or hyphens) is required.')
        request_hash = digest(encode({k: v for k, v in request.items() if k != 'expected'}))
        with lock(self.lockpath):
            state, token = self.load()
            self.recover(state)
            for event in state['events']:
                if event['operation_id'] == operation:
                    if event['request_hash'] != request_hash:
                        raise StoreError('Operation ID already used for different data.', 409)
                    return dict(state, token=token)
            if request.get('expected') != token:
                raise StoreError('Tasks changed since you opened this view. Reload the latest tasks, compare your draft, then retry.', 409)
            action = request.get('action')
            if action not in ('create', 'update', 'note'):
                raise StoreError('Action must be create, update or note.')
            actor = request.get('actor', 'You via local UI')
            if actor not in ('You via local UI', 'You via task command'):
                raise StoreError('Invalid actor; this tool cannot assert Alex approval.')
            now = datetime.now(MANILA).isoformat(timespec='seconds')
            before = None
            if action == 'create':
                task = {'id': f"T-{state['next_id']:03}", 'title': '', 'description': '', 'owner': 'Charles',
                        'assigned_by': 'You', 'assignment_note': '', 'sources': [], 'status': 'Backlog', 'priority': 'Normal',
                        'start': None, 'end': None, 'deadline': None, 'dependencies': [], 'order': state['next_id'] * 1000,
                        'archived': False, 'notes': [], 'revision': 0, 'completed_at': None}
            else:
                task = next((t for t in state['tasks'] if t['id'] == request.get('id')), None)
                if task is None:
                    raise StoreError('Task not found.', 404)
                before = copy.deepcopy(task)
            if action == 'note':
                note = request.get('text')
                if not isinstance(note, str) or not note.strip() or len(note) > 20000:
                    raise StoreError('Enter a note of 1–20,000 characters.')
                task['notes'].append({'at': now, 'text': note, 'actor': actor})
            else:
                changes = request.get('changes', {})
                if not isinstance(changes, dict) or set(changes) - FIELDS:
                    raise StoreError('Unknown task fields.')
                task.update(changes)
                if changes.get('status') == 'Backlog' and before and before['status'] != 'Backlog':
                    task['start'] = task['end'] = None
                elif task['start'] and task['status'] == 'Backlog':
                    task['status'] = 'To do'
                if 'start' in changes and task['start'] is None:
                    task['end'] = None
                if task['assigned_by'] == 'Alex' and not task['sources'] and not task['assignment_note'].startswith('User-reported:'):
                    task['assignment_note'] = 'User-reported: ' + task['assignment_note'] if task['assignment_note'].strip() else ''
                self.validate_task(task)
                allowed_ids = {t['id'] for t in state['tasks']} | {x['id'] for x in state['legacy']}
                if any(dep not in allowed_ids or dep == task['id'] for dep in task['dependencies']):
                    raise StoreError('Dependencies must reference other existing tasks.')
                graph = {t['id']: t['dependencies'] for t in state['tasks']}
                graph[task['id']] = task['dependencies']
                def visit(node, path):
                    if node in path:
                        raise StoreError('Task dependencies cannot form a cycle.')
                    for dep in graph.get(node, []):
                        visit(dep, path | {node})
                visit(task['id'], set())
            task['revision'] += 1
            if task['status'] == 'Done':
                task['completed_at'] = task['completed_at'] or now
            else:
                task['completed_at'] = None
            if action == 'create':
                state['tasks'].append(task)
                state['next_id'] += 1
            event = {'id': f"EVT-{len(state['events']) + 1:06}", 'operation_id': operation, 'request_hash': request_hash,
                     'at': now, 'actor': actor, 'action': action, 'task_id': task['id'], 'request': request,
                     'before': before, 'after': copy.deepcopy(task)}
            state['events'].append(event)
            state['revision'] += 1
            state['projection_before'] = {name: digest((self.kb / name).read_bytes()) for name in self.projections(state)}
            atomic(self.path, encode(state))  # Commit point; projections can be recovered after process interruption.
            self.recover(state)
            return dict(state, token=digest(self.path.read_bytes()))
