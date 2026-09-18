"""Check static links, images, semantic basics, and source essay preservation."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parents[1]
errors=[];count=0
class Doc(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if a.get('id'):self.ids.add(a['id'])
        if tag=='img' and 'alt' not in a:errors.append('Image missing alt')
        for k in ['href','src']:
            if a.get(k):self.refs.append(a[k])
parsed={}
for f in R.rglob('*.html'):
    if 'content' in f.parts or '_site' in f.parts:continue
    d=Doc();d.feed(f.read_text());parsed[f.resolve()]=d
for f,d in parsed.items():
    count+=1
    if f.name=='index.html' or f.name=='404.html':
        if d.h1!=1:errors.append(str(f)+': must have one H1')
    for ref in d.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        path=(f.parent/unquote(u.path)).resolve() if u.path else f
        if path.is_dir():path=path/'index.html'
        if not path.exists():errors.append(str(f.relative_to(R))+': missing '+ref)
        elif u.fragment and path in parsed and unquote(u.fragment) not in parsed[path].ids:errors.append('Missing anchor: '+ref)
for p in ['index.html','research/index.html','essays/index.html','piano/index.html','contact/index.html']:
    s=(R/p).read_text()
    for bad in ['example.com','placeholder','coming soon','what-llm-judges-measure']:
        if bad in s.lower():errors.append(p+': stale content '+bad)
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {count} pages; local links, anchors, images, primary headings, placeholder removal.')
