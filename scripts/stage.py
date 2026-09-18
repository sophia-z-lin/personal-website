"""Copy only public files to _site for GitHub Pages."""
from pathlib import Path
import shutil
R=Path(__file__).resolve().parents[1];out=R/'_site';out.mkdir(exist_ok=True)
for item in ['assets','research','essays','piano','contact']:
    shutil.copytree(R/item,out/item,dirs_exist_ok=True)
for item in ['index.html','404.html','styles.css','site.js','cv.pdf','sitemap.xml','robots.txt','.nojekyll','research.html','essays.html','piano.html','contact.html']:
    shutil.copy2(R/item,out/item)
print('Public files staged in _site')
