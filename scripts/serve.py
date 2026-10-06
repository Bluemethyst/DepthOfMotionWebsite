"""Local preview, including a repository-subdirectory URL; Python standard library only."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class SiteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self._strip_prefix()
        super().do_GET()

    def do_HEAD(self):
        self._strip_prefix()
        super().do_HEAD()

    def _strip_prefix(self):
        prefix = '/DepthOfMotionWebsite'
        if urlsplit(self.path).path == prefix:
            self.path = '/'
        elif self.path.startswith(prefix + '/'):
            self.path = self.path[len(prefix):]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    handler = partial(SiteHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    print(f'Preview: http://127.0.0.1:{args.port}/DepthOfMotionWebsite/', flush=True)
    print('Press Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
