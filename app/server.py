"""Local task board. Run: python app/server.py [--port 8765] [--open]."""
import argparse
import hashlib
import json
import mimetypes
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, unquote
from store import Store, StoreError

ROOT = Path(__file__).resolve().parents[1]
STATIC = Path(__file__).parent / 'static'


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def trusted(self):
        # A local-only server still needs protection from browser requests made by other sites.
        allowed = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
        if self.headers.get('Host') not in allowed:
            raise StoreError('Unrecognized host.', 403)
        origin = self.headers.get('Origin')
        if origin and origin not in {'http://' + host for host in allowed}:
            raise StoreError('Cross-origin requests are not allowed.', 403)

    def send(self, status, content, mime='application/json; charset=utf-8'):
        if not isinstance(content, bytes):
            content = json.dumps(content, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        try:
            self.trusted()
            path = unquote(urlsplit(self.path).path)
            if path == '/api/tasks':
                self.send(200, self.server.store.snapshot())
            elif path == '/api/events':
                self.send_response(200)
                self.send_header('Content-Type', 'text/event-stream')
                self.send_header('Cache-Control', 'no-cache')
                self.end_headers()
                previous = None
                for _ in range(300):
                    try:
                        snapshot = self.server.store.snapshot()
                        payload = {'token': snapshot['token']}
                    except (StoreError, OSError) as error:
                        payload = {'error': str(error)}
                    current = json.dumps(payload)
                    if current != previous:
                        self.wfile.write(('data: ' + current + '\n\n').encode())
                        previous = current
                    else:
                        self.wfile.write(b': heartbeat\n\n')
                    self.wfile.flush()
                    time.sleep(1)
            elif path.startswith('/source/'):
                source = (ROOT / 'knowledge-base' / path[len('/source/'):].split('#')[0]).resolve()
                if source.suffix != '.md' or not source.is_relative_to((ROOT / 'knowledge-base' / 'sources').resolve()):
                    raise StoreError('Source not allowed.', 404)
                self.send(200, source.read_bytes(), 'text/plain; charset=utf-8')
            else:
                file = (STATIC / ('index.html' if path == '/' else path.lstrip('/'))).resolve()
                if not file.is_relative_to(STATIC.resolve()) or not file.is_file():
                    raise StoreError('Not found.', 404)
                mime = {'.js': 'text/javascript', '.css': 'text/css', '.html': 'text/html'}.get(file.suffix, mimetypes.guess_type(file)[0] or 'application/octet-stream')
                self.send(200, file.read_bytes(), mime + '; charset=utf-8')
        except StoreError as error:
            self.send(error.status, {'error': str(error)})
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass
        except OSError as error:
            self.send(503, {'error': 'Local file unavailable: ' + str(error)})

    def do_POST(self):
        try:
            self.trusted()
            if self.path != '/api/commands':
                raise StoreError('Not found.', 404)
            if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                raise StoreError('Use application/json.', 415)
            length = int(self.headers.get('Content-Length', '0'))
            if length <= 0 or length > 250000:
                raise StoreError('Request body must be 1–250,000 bytes.', 413)
            request = json.loads(self.rfile.read(length))
            if not isinstance(request, dict):
                raise StoreError('Expected a JSON object.')
            request['actor'] = 'You via local UI'
            self.send(200, self.server.store.command(request))
        except StoreError as error:
            self.send(error.status, {'error': str(error)})
        except (ValueError, TypeError):
            self.send(400, {'error': 'Invalid JSON or content length.'})
        except OSError as error:
            self.send(503, {'error': 'Save interrupted. Keep your draft and retry the same action: ' + str(error)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--open', action='store_true')
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    server.daemon_threads = True
    server.store = Store(ROOT)
    url = f'http://127.0.0.1:{server.server_port}'
    print(f'Task board: {url}\nKeep this process running for live sync. Ctrl+C stops it.', flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
