"""Validate static pages, navigation, fragments and local assets without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'index.html', 'childrens-dance.html', 'adult-dance.html',
            'womens-movement.html', 'creative-work.html', 'about.html'}
EXTERNAL_LINKS = {'https://www.instagram.com/elemental_dancer_',
                  'https://www.facebook.com/ReAliTyDance5/'}
errors = []


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs, self.active = path, set(), [], []
        self.h1s = self.titles = self.descriptions = 0
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        self.h1s += tag == 'h1'
        self.titles += tag == 'title'
        self.descriptions += tag == 'meta' and attrs.get('name') == 'description'
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'{self.path.name}: image missing alt')
        if attrs.get('aria-current') == 'page':
            self.active.append(attrs.get('href'))
        for key in ('href', 'src', 'poster'):
            if key in attrs:
                self.refs.append(attrs[key])


docs = {p.name: Document(p) for p in ROOT.glob('*.html')}
if set(docs) != EXPECTED:
    errors.append('Expected exactly the six requested HTML pages.')
for name, doc in docs.items():
    if (doc.h1s, doc.titles, doc.descriptions) != (1, 1, 1):
        errors.append(f'{name}: expected one H1, title and meta description')
    if doc.active != [name, name]:
        errors.append(f'{name}: active header/footer links incorrect')
    for ref in doc.refs:
        parts = urlsplit(ref)
        if parts.scheme in ('tel', 'mailto') or ref in EXTERNAL_LINKS:
            continue
        if parts.scheme or parts.netloc or ref.startswith('/'):
            errors.append(f'{name}: non-relative website reference {ref}')
            continue
        target = ROOT / unquote(parts.path) if parts.path else doc.path
        if not target.is_file():
            errors.append(f'{name}: missing {ref}')
        elif parts.fragment and target.suffix == '.html':
            if unquote(parts.fragment) not in docs[target.name].ids:
                errors.append(f'{name}: missing fragment in {ref}')
for css in (ROOT / 'assets').rglob('*.css'):
    for ref in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text(encoding='utf-8-sig')):
        if not (css.parent / ref).is_file():
            errors.append(f'{css.name}: missing asset {ref}')
titles = [re.search(r'<title>(.*?)</title>', d.path.read_text(encoding='utf-8')).group(1) for d in docs.values()]
descriptions = [re.search(r'name="description" content="(.*?)"', d.path.read_text(encoding='utf-8')).group(1) for d in docs.values()]
if len(set(titles)) != 6 or len(set(descriptions)) != 6:
    errors.append('Page titles and descriptions must be unique.')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(docs)} pages; links, fragments, assets, navigation and metadata verified.')
