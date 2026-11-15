"""Task helper: list, apply --file request.json, recover, migrate."""
import argparse
import json
import re
import sys
from pathlib import Path
from store import Store, StoreError, atomic, digest, encode, lock


def migrate(store):
    with lock(store.lockpath):
        if store.path.exists():
            raise StoreError('Already migrated; refusing to replace the task store.')
        original = (store.kb / 'tasks.md').read_text(encoding='utf-8')
        tasks, legacy = [], []
        for line in original.splitlines():
            cells = [c.strip() for c in line.strip('|').split('|')]
            if re.match(r'^\| T-\d{3} \|', line) and len(cells) == 10:
                title, _, description = cells[1].partition('. ')
                start = re.search(r'\d{4}-\d{2}-\d{2}', cells[6])
                tasks.append({'id': cells[0], 'title': title.rstrip('.'), 'description': description,
                    'owner': cells[2], 'assigned_by': cells[3], 'assignment_note': cells[8],
                    'sources': re.findall(r'\]\((sources/[^)]+)\)', cells[4]), 'status': 'To do' if start else 'Backlog',
                    'priority': 'Normal', 'start': start[0] if start else None, 'end': None, 'deadline': None,
                    'dependencies': ['LEGACY-T-008'], 'order': len(tasks)*1000, 'archived': False,
                    'notes': [], 'revision': 1, 'completed_at': None})
            elif re.match(r'^\| LEGACY-T-\d{3} \|', line):
                legacy.append({'id': cells[0], 'title': cells[1], 'owner': cells[2], 'status': cells[3], 'detail': ' | '.join(cells[4:])})
        if len(tasks) != 6 or len(legacy) != 8:
            raise StoreError('Expected six current tasks and eight legacy records. Review migration input.')
        state = {'schema': 1, 'revision': 1, 'next_id': 7, 'tasks': tasks, 'legacy': legacy, 'events': [],
                 'legacy_markdown': original[original.index('## Task ID migration'):],
                 'projection_before': {'tasks.md': digest((store.kb / 'tasks.md').read_bytes()), 'sources/task-events.md': None}}
        for task in tasks:
            store.validate_task(task)
        # Preserve exact original bytes, including line endings, for migration recovery.
        archive = store.root / 'app' / 'docs' / 'tasks-before-migration.md'
        if archive.exists():
            raise StoreError('Migration archive already exists; inspect before proceeding.')
        atomic(archive, (store.kb / 'tasks.md').read_bytes())
        atomic(store.path, encode(state))
        store.recover(state)
        return {'migrated': len(tasks), 'legacy': len(legacy)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['list', 'apply', 'recover', 'migrate'])
    parser.add_argument('--file', help='UTF-8 JSON request, or - to read stdin')
    args = parser.parse_args()
    store = Store(Path(__file__).resolve().parents[1])
    try:
        if args.action == 'migrate':
            result = migrate(store)
        elif args.action == 'apply':
            if not args.file:
                parser.error('apply requires --file (or --file - for stdin)')
            request = json.loads(sys.stdin.read() if args.file == '-' else Path(args.file).read_text(encoding='utf-8-sig'))
            request['actor'] = 'You via task command'
            result = store.command(request)
        else:
            result = store.snapshot()
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (StoreError, ValueError, OSError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
