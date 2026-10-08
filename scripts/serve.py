"""Local preview, including a repository-subdirectory URL; Python standard library only."""
import argparse
import re
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

    def send_head(self):
        path = Path(self.translate_path(self.path))
        self._range_remaining = None
        if path.suffix.lower() != '.mp4' or not path.is_file():
            return super().send_head()
        media = path.open('rb')
        size = path.stat().st_size
        requested = self.headers.get('Range')
        start, end = 0, size - 1
        if requested:
            match = re.fullmatch(r'bytes=(\d*)-(\d*)', requested.strip())
            if not match or not any(match.groups()):
                media.close()
                self.send_error(416, 'Unsupported byte range')
                return None
            first, last = match.groups()
            if first:
                start = int(first)
                end = min(int(last), end) if last else end
            else:
                start = max(0, size - int(last))
            if start >= size or start > end:
                media.close()
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{size}')
                self.send_header('Content-Length', '0')
                self.end_headers()
                return None
            media.seek(start)
            self._range_remaining = end - start + 1
        self.send_response(206 if requested else 200)
        self.send_header('Content-Type', 'video/mp4')
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Last-Modified', self.date_time_string(path.stat().st_mtime))
        if requested:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        return media

    def copyfile(self, source, outputfile):
        remaining = getattr(self, '_range_remaining', None)
        if remaining is None:
            return super().copyfile(source, outputfile)
        while remaining:
            data = source.read(min(64 * 1024, remaining))
            if not data:
                break
            outputfile.write(data)
            remaining -= len(data)

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
