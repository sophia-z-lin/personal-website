"""Build static pages from editable content. Python 3 standard library only."""
from pathlib import Path
from html import escape as esc
import json, re, shutil
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'content/site.json').read_text())
E=json.loads((R/'content/essay.json').read_text())
BASE=D['url'].rstrip('/')
def page(path,title,body,active='home',desc=None):
    depth=len(Path(path).parts)-1;p=BASE+'/' if path=='404.html' else '../'*depth
    nav=''.join(f'<a href="{p}{url}"'+(' aria-current="page"' if key==active else '')+f'>{label}</a>' for key,label,url in [('home','About','index.html'),('research','Research','research/'),('piano','Piano','piano/'),('essays','Essays','essays/'),('contact','Contact','contact/')])
    description=desc or D['description']
    html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — Sophia Lin</title><meta name="description" content="{esc(description,quote=True)}"><meta name="theme-color" content="#050505">
<link rel="canonical" href="{BASE}/{path.replace('index.html','')}"><meta property="og:title" content="{esc(title,quote=True)} — Sophia Lin"><meta property="og:description" content="{esc(description,quote=True)}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}/assets/portrait.png">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{p}styles.css"><script src="{p}site.js" defer></script>
</head><body><a class="skip" href="#main">Skip to content</a><div class="reading-progress" aria-hidden="true"></div>
<header class="masthead"><nav aria-label="Main navigation">{nav}<a class="nav-cv" href="{p}cv.pdf">CV ↗</a></nav></header>
<main id="main">{body.replace('@@',p)}</main>
<footer><div class="footer-bottom"><span>Sophia Lin · {2026}</span><div><a href="https://www.linkedin.com/in/szlin-harvard">LinkedIn ↗</a><a href="{p}cv.pdf">CV ↗</a><a href="{p}contact/">Contact ↗</a></div><span class="pigments" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span></div></footer></body></html>'''
    out=R/path;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(html)
def heading(n,title,note='',href=None):
    return f'<div class="section-head"><span class="folio">{n}</span><h2>{title}</h2>'+ (f'<a href="{href}">{note} ↗</a>' if href else f'<span class="meta">{note}</span>')+'</div>'
def title(n,name,desc):
    return f'<div class="page-opening"><p class="kicker">{n} / Sophia Lin</p><h1>{name}<span class="title-stop">.</span></h1><p class="page-deck">{desc}</p></div>'
def project(x,short=False):
    link=f'<a href="{x["url"]}">Paper ↗</a>' if x.get('url') else ''
    return f'<article class="project"><div class="project-context"><span>{x["institution"]}</span><span>{x["date"]}</span></div><div><h3>{x["title"]}</h3><p>{x["text"]}</p><div class="project-end"><span>{x["role"]}</span>{link}</div></div></article>'
def publications():
    return ''.join(f'<article class="publication"><span class="pub-year">{x["year"]}</span><div><h3><a href="{x["url"]}">{x["title"]} ↗</a></h3><p>{x["authors"].replace("Sophia Lin","<strong>Sophia Lin</strong>")}</p><span class="meta">{x["venue"]}</span></div></article>' for x in D['publications'])
def essayfeature():
    return f'''<article class="essay-feature"><div class="essay-date">29 April<br>2026</div><div><p class="kicker">Essay 001</p><h3><a href="@@essays/fenris/">Flop Incest Nazis<span class="arrow">↗</span></a></h3><p class="essay-subtitle">Why the visual representation of neo-Nazism in X-Men’s Fenris succeeds</p><p>How an image can make an ideology legible without making it appealing—and why the distinction matters when images circulate without their original context.</p><a class="text-link" href="@@essays/fenris/">Read the essay <span>→</span></a></div></article>'''
def performance(x,i,full=True):
    img=f'https://i.ytimg.com/vi/{x["id"]}/hqdefault.jpg'
    return f'''<article class="performance"><div class="performance-number">{i:02d}<span>{x['year']}</span></div><div class="performance-body"><p class="kicker">{x['composer']}</p><h2>{x['title']}</h2><p class="meta">{x['subtitle']}</p><div class="video" data-video="{x['id']}"><a href="https://www.youtube.com/watch?v={x['id']}" class="video-cover" aria-label="Play {esc(x['title'],quote=True)}"><img src="{img}" alt="" loading="lazy" onerror="this.style.opacity=0"><span class="play">▶</span><span class="video-caption">Play recording <span>↗</span></span></a></div><div class="video-links"><a href="https://www.youtube.com/watch?v={x['id']}">Watch on YouTube ↗</a><a href="{x['source']}">Programme / source ↗</a></div></div></article>'''
intro=f'''<section class="opening"><div class="opening-top"><p class="kicker">Research, essays, and performances</p><span class="meta">Cambridge, MA</span></div><h1>Sophia Lin<span class="title-stop">.</span></h1><div class="biography"><div><p class="intro-line">{D['intro']}</p><p>My <a href="@@research/">research</a> is at NIST, where I study LLM judges and adversarial verification: whether evaluators measure what they claim to measure, and whether independent verifiers improve the factual grounding of AI systems. Previously, I worked on Bayesian models of censoring and interpretable prediction from clinical records.</p><p>I also <a href="@@piano/">play piano</a> and <a href="@@essays/">write essays</a> — technical, personal, philosophical.</p></div><figure class="portrait"><img src="@@assets/portrait.png" width="1536" height="1024" alt="Sophia Lin speaking during a recorded conversation"><figcaption>Sophia Lin</figcaption></figure></div></section>'''
home=intro
page('index.html','Research, essays & performances',home)
research=title('01','Research','Evaluation validity, uncertainty, and evidence that can be inspected.')+'<div class="section-introduction"><p>I work on the reliability of AI systems and the methods used to judge them. Across language-model evaluation and clinical prediction, I am interested in what a measurement captures, what it misses, and which conclusions it can support.</p><a class="text-link" href="@@cv.pdf">Curriculum vitae ↗</a></div><section class="archive-section">'+heading('01.1','Projects')+''.join(project(x) for x in D['projects'])+'</section><section class="archive-section" id="publications">'+heading('01.2','Selected publications')+publications()+'<p><a href="https://scholar.google.com/citations?user=iws3sEUAAAAJ&amp;hl=en">Google Scholar ↗</a></p></section>'
page('research/index.html','Research',research,active='research')
page('essays/index.html','Essays',title('02','Essays','On evidence, representation, and the ideas that survive their context.')+essayfeature(),active='essays')
text=(R/'content/fenris.html').read_text().replace('../../assets/','@@assets/')
heads=re.findall(r'<h2 id="(section-\d+)">(.*?)</h2>',text)
toc=''.join(f'<a href="#{a}">{b}</a>' for a,b in heads)
article=f'''<article class="longform"><header class="essay-opening"><a class="kicker" href="@@essays/">← Essays / 001</a><p class="meta">29 April 2026 · Sophia Lin</p><h1>Flop Incest Nazis</h1><p class="essay-deck">Why the visual representation of neo-Nazism in X-Men’s Fenris succeeds</p></header><details class="contents"><summary>In this essay</summary><nav aria-label="Essay contents">{toc}<a href="#appendices">Illustrated appendices</a><a href="#references">Works cited</a></nav></details><div class="essay-text">{text}</div></article>'''
page('essays/fenris/index.html','Flop Incest Nazis',article,active='essays',desc="Why the visual representation of neo-Nazism in X-Men’s Fenris succeeds. An essay by Sophia Lin.")
piano=title('03','Piano','Selected performances. Solo and with orchestra.')+'<p class="section-introduction">I studied with Dr. Marjorie Lee and performed chamber music through the National Symphony Orchestra Youth Fellowship. These recordings span solo recital and concerto performance. <a href="https://www.alfred.edu/mostarts/young-pianist-competition/2023-finalists.cfm">Biography ↗</a></p>'+''.join(performance(x,i+1) for i,x in enumerate(D['performances']))+'<p class="archive-link"><a href="https://www.youtube.com/@sophialin1802">Complete YouTube archive ↗</a></p>'
page('piano/index.html','Piano',piano,active='piano')
contact=title('04','Contact','Good questions are a good place to start.')+f'''<section class="contact-body"><p>For research, writing, music, or a conversation:</p><a class="contact-email" href="mailto:{D['email']}">{D['email']} ↗</a><div class="contact-row"><span>Research</span><a href="https://scholar.google.com/citations?user=iws3sEUAAAAJ&amp;hl=en">Google Scholar ↗</a></div><div class="contact-row"><span>Code</span><a href="https://github.com/sophia-z-lin">GitHub ↗</a></div><div class="contact-row"><span>Professional</span><a href="https://www.linkedin.com/in/szlin-harvard">LinkedIn ↗</a></div><div class="contact-row"><span>Performances</span><a href="https://www.youtube.com/@sophialin1802">YouTube ↗</a></div><div class="contact-row"><span>Background</span><a href="@@cv.pdf">Curriculum vitae (PDF) ↗</a></div></section>'''
page('contact/index.html','Contact',contact,active='contact')
page('404.html','Page not found',title('404','Not here','This page may have moved.')+f'<p><a href="{BASE}/">Return home →</a></p>')
# Preserve legacy links, including the old fabricated draft URL, without publishing the draft.
for old,new in [('essays.html','essays/'),('piano.html','piano/'),('research.html','research/'),('contact.html','contact/'),('essays/what-llm-judges-measure.html','./')]:
    (R/old).write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={new}"><title>Moved — Sophia Lin</title><a href="{new}">Continue →</a></html>')
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}/{p}</loc></url>' for p in ['', 'research/','essays/','essays/fenris/','piano/','contact/'])+'</urlset>')
(R/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
print('Built 6 pages, 404, legacy redirects, sitemap.')
