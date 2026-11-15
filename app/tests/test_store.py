import copy
import json
import multiprocessing
import shutil
import sys
import tempfile
import threading
import unittest
import uuid
from pathlib import Path
from unittest.mock import patch
from urllib.request import Request, urlopen
from urllib.error import HTTPError

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
from store import Store, StoreError, atomic, encode
from tasks import migrate
from server import Handler, ThreadingHTTPServer


def competing_save(root, token, title, queue):
    try:
        Store(root).command({'action':'update','id':'T-001','expected':token,'operation_id':str(uuid.uuid4()),'changes':{'title':title}})
        queue.put('saved')
    except StoreError as error:
        queue.put(error.status)


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.kb = self.root / 'knowledge-base'
        (self.kb / 'sources').mkdir(parents=True)
        # The migration archive is a real immutable fixture, never the user's live task store.
        shutil.copyfile(APP / 'docs/tasks-before-migration.md', self.kb / 'tasks.md')
        for name in ('SRC-011-monday-phase-0-tasks.md',):
            (self.kb/'sources'/name).write_text('fixture evidence')
        self.store = Store(self.root)
        migrate(self.store)

    def tearDown(self):
        self.temp.cleanup()

    def command(self, action='update', **values):
        request={'action':action,'id':'T-001','expected':self.store.snapshot()['token'],'operation_id':str(uuid.uuid4())}
        request.update(values)
        return self.store.command(request)

    def test_migration_preserves_six_tasks_and_eight_legacy(self):
        state=self.store.snapshot()
        self.assertEqual([t['id'] for t in state['tasks']], [f'T-{i:03}' for i in range(1,7)])
        self.assertEqual(len(state['legacy']),8)
        self.assertTrue(all(t['start']=='2026-11-16' and t['status']=='To do' and t['assigned_by']=='You' for t in state['tasks']))
        self.assertEqual(state['events'],[])
        self.assertEqual((self.root/'app/docs/tasks-before-migration.md').read_bytes(),(APP/'docs/tasks-before-migration.md').read_bytes())
        with self.assertRaises(StoreError): migrate(self.store)

    def test_create_schedule_and_increment_id(self):
        state=self.command('create',changes={'title':'New task','start':'2026-11-18'})
        task=state['tasks'][-1]
        self.assertEqual((task['id'],task['status']),('T-007','To do'))
        self.assertIn('T-007',(self.kb/'tasks.md').read_text())
        self.assertIn('EVT-000001',(self.kb/'sources/task-events.md').read_text())

    def test_status_dates_and_deadline(self):
        self.command(changes={'deadline':'2026-11-30','status':'In progress'})
        state=self.command(changes={'start':'2026-11-20','end':'2026-11-22'})
        self.assertEqual(state['tasks'][0]['deadline'],'2026-11-30')
        state=self.command(changes={'status':'Backlog'})
        self.assertIsNone(state['tasks'][0]['start'])
        self.assertIsNone(state['tasks'][0]['end'])
        self.assertEqual(state['tasks'][0]['deadline'],'2026-11-30')

    def test_completion_reopen_archive_and_restore(self):
        state=self.command(changes={'status':'Done'})
        self.assertIsNotNone(state['tasks'][0]['completed_at'])
        state=self.command(changes={'status':'Review','archived':True})
        self.assertIsNone(state['tasks'][0]['completed_at'])
        self.assertTrue(state['tasks'][0]['archived'])
        state=self.command(changes={'archived':False})
        self.assertFalse(state['tasks'][0]['archived'])
        self.assertEqual(len(state['events']),3)

    def test_assignment_retained_and_alex_report_labeled(self):
        self.command(changes={'assigned_by':'Alex','sources':[],'assignment_note':'Alex asked me to review this'})
        state=self.command(changes={'start':'2026-11-23'})
        self.assertEqual(state['tasks'][0]['assigned_by'],'Alex')
        self.assertTrue(state['tasks'][0]['assignment_note'].startswith('User-reported:'))
        with self.assertRaises(StoreError):
            self.command(changes={'assigned_by':'Alex','sources':[],'assignment_note':''})

    def test_stale_edit_rejected_and_data_retained(self):
        token=self.store.snapshot()['token']
        self.command(changes={'title':'Winner'})
        with self.assertRaises(StoreError) as ctx:
            self.command(expected=token,changes={'title':'Stale'})
        self.assertEqual(ctx.exception.status,409)
        self.assertEqual(self.store.snapshot()['tasks'][0]['title'],'Winner')

    def test_duplicate_request_is_idempotent(self):
        req={'action':'create','changes':{'title':'Once'},'operation_id':str(uuid.uuid4()),'expected':self.store.snapshot()['token']}
        first=self.store.command(req)
        again=self.store.command(req)
        self.assertEqual(first['token'],again['token'])
        req['changes']['title']='Different'
        with self.assertRaises(StoreError): self.store.command(req)

    def test_notes_and_markdown_escaping(self):
        state=self.command('note',text='Finding | second column\n<script>not executable</script>')
        self.assertEqual(len(state['tasks'][0]['notes']),1)
        md=(self.kb/'tasks.md').read_text()
        self.assertIn('&#124;',md)
        self.assertIn('&lt;script&gt;',md)

    def test_invalid_dates_status_sources_and_dependencies(self):
        for changes in ({'start':'2026-02-30'}, {'end':'2026-01-01'}, {'status':'Approved'},
                        {'sources':['../../outside.md']}, {'dependencies':['T-999']}, {'dependencies':['T-001']},
                        {'archived':'yes'}, {'owner':''}, {'title':''}):
            with self.subTest(changes=changes), self.assertRaises(StoreError): self.command(changes=changes)
        self.assertEqual(self.store.snapshot()['events'],[])

    def test_manual_projection_edit_is_never_overwritten(self):
        p=self.kb/'tasks.md';p.write_text(p.read_text()+'\nmanual edit')
        with self.assertRaises(StoreError) as ctx: self.store.snapshot()
        self.assertEqual(ctx.exception.status,409)
        self.assertTrue(p.read_text().endswith('manual edit'))

    def test_interrupted_projection_is_recovered(self):
        original=atomic
        def fail_projection(path,content):
            if path.name=='tasks.md':raise OSError('Simulated interruption after commit')
            original(path,content)
        token=self.store.snapshot()['token']
        req={'action':'update','id':'T-001','changes':{'title':'Committed'},'expected':token,'operation_id':str(uuid.uuid4())}
        with patch('store.atomic',side_effect=fail_projection),self.assertRaises(OSError):self.store.command(req)
        state=Store(self.root).snapshot()
        self.assertEqual(state['tasks'][0]['title'],'Committed')
        self.assertIn('Committed',(self.kb/'tasks.md').read_text())
        self.assertEqual(len(self.store.command(req)['events']),1)

    def test_failure_before_commit_preserves_state(self):
        before=self.store.snapshot()
        with patch('store.atomic',side_effect=OSError('disk unavailable')),self.assertRaises(OSError):
            self.command(changes={'title':'Not committed'})
        self.assertEqual(self.store.snapshot()['token'],before['token'])

    def test_malformed_store_fails_closed(self):
        self.store.path.write_text('{bad json')
        with self.assertRaises(StoreError): self.store.snapshot()

    def test_new_scheduled_task_with_form_default_backlog(self):
        state=self.command('create',changes={'title':'Scheduled form task','status':'Backlog','start':'2026-11-18'})
        self.assertEqual(state['tasks'][-1]['status'],'To do')
        self.assertEqual(state['tasks'][-1]['start'],'2026-11-18')

    def test_dependency_cycle_rejected(self):
        self.command(id='T-001',changes={'dependencies':['T-002']})
        with self.assertRaises(StoreError):self.command(id='T-002',changes={'dependencies':['T-001']})

    def test_two_processes_only_one_wins(self):
        token=self.store.snapshot()['token'];ctx=multiprocessing.get_context('spawn');queue=ctx.Queue()
        processes=[ctx.Process(target=competing_save,args=(str(self.root),token,f'Writer {i}',queue)) for i in range(2)]
        for p in processes:p.start()
        for p in processes:p.join(10);self.assertFalse(p.is_alive())
        self.assertCountEqual([queue.get(timeout=2),queue.get(timeout=2)],['saved',409])
        queue.close()
        self.assertEqual(len(self.store.snapshot()['events']),1)


class HTTPTests(unittest.TestCase):
    setUp = StoreTests.setUp
    tearDown = StoreTests.tearDown
    def test_http_round_trip_events_and_origin(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.daemon_threads=True;server.store=self.store
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        url=f'http://127.0.0.1:{server.server_port}'
        try:
            with urlopen(url+'/api/tasks',timeout=3) as r:state=json.load(r)
            req={'action':'update','id':'T-001','changes':{'status':'Review'},'expected':state['token'],'operation_id':str(uuid.uuid4())}
            request=Request(url+'/api/commands',data=json.dumps(req).encode(),headers={'Content-Type':'application/json'})
            with urlopen(request,timeout=3) as r:self.assertEqual(json.load(r)['tasks'][0]['status'],'Review')
            with urlopen(url+'/api/events',timeout=3) as r:
                first = json.loads(r.readline()[6:])
                latest = self.store.snapshot()
                changed = self.store.command({'action':'update','id':'T-002','changes':{'priority':'High'},'expected':latest['token'],'operation_id':str(uuid.uuid4()),'actor':'You via task command'})
                for _ in range(8):
                    line = r.readline()
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        self.assertEqual(event['token'], changed['token'])
                        self.assertNotEqual(event['token'], first['token'])
                        break
                else: self.fail('Helper update was not streamed to the UI')
            request=Request(url+'/api/commands',data=json.dumps(req).encode(),headers={'Content-Type':'application/json','Origin':'https://example.com'})
            with self.assertRaises(HTTPError) as ctx:urlopen(request,timeout=3)
            self.assertEqual(ctx.exception.code,403)
            for path in ('/','/app.js','/dates.js','/style.css'):
                with urlopen(url+path,timeout=3) as r:self.assertEqual(r.status,200)
        finally:
            server.shutdown();server.server_close();thread.join(3)


if __name__=='__main__':unittest.main()
