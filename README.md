# Sophia Lin — personal website

A continuous academic archive with dedicated Research, Essays, Piano, and Contact pages. Near-black ground, self-hosted Instrument Sans, narrow prose, straight rules, restrained cobalt / brick / saffron accents. Original implementation informed by the supplied design brief; no al-folio code dependencies.

## Local preview on Windows

Extract this archive's contents directly into `C:\Users\sophi\Documents\Harvard\Sophomore\personal-website` (the folder containing your repository, not an additional nested folder). Preserve your existing `.git` directory. This archive contains no Git history.

In PowerShell, from that directory:

```powershell
py scripts/fetch_fonts.py
py scripts/build.py
py scripts/check.py
py -m http.server 8000
```

Open http://localhost:8000. The font setup downloads Instrument Sans and its SIL Open Font License from Google Fonts' repository, saves them to `assets/fonts`, and validates the font bytes. It requires internet access once. No visitor font requests go to Google. If the download fails, the script stops with an error; pages remain readable using the system fallback.

## Publish with your own commits

Repository: https://github.com/sophia-z-lin/personal-website

In **Settings → Pages → Source**, choose **GitHub Actions**. Commit and push your changes to `main` yourself. The included workflow fetches and self-hosts the font, builds and checks the site, stages public files only, and deploys to:

https://sophia-z-lin.github.io/personal-website/

No commit or push was made for this redesign.

## Edit content

- `content/site.json`: biography, email, projects, publications, ordered performances, canonical URL.
- `content/fenris.html`: full essay, formatting, illustrated appendices, works cited. The private instructor letter and course header were excluded. Essay wording was retained; it has not been fact-checked or editorially revised.
- `content/essay.json`: essay metadata (classification remains internal).
- `scripts/build.py`: shared layouts and page templates. Rebuild after editing content.
- `styles.css`: typography, geometry, pigments, mobile rules, focus and reduced-motion behavior.
- `site.js`: reading progress and click-to-load YouTube privacy-enhanced embeds. Regular YouTube links remain available with JavaScript disabled or when embedding is unavailable.
- `assets/portrait.png`: supplied photograph, displayed in a CSS crop without retouching.
- `cv.pdf`: supplied CV, unchanged, including its contact information.

URLs use directory indexes and relative assets, so the site works under the GitHub project prefix. Legacy `.html` links redirect to the new pages. The earlier fabricated LLM-judge essay has been replaced by a redirect to the real essay index.

## Content sourcing and limits

Research and publication metadata come from the supplied September 2026 CV. The Bayesian paper was checked against https://arxiv.org/abs/2511.11684. The malformed third DOI in the CV was replaced with the IEEE document URL https://ieeexplore.ieee.org/document/9941764.

Selected recordings: Mozart with Capital City Symphony (J1erOy6uP-U), MostArts solo recital (qWtZ5nAy-Dw), and Knabe competition (duUCiAjTV_g). The first two events were cross-checked against the presenters' websites; the third uses its indexed YouTube title. YouTube throttled the channel listing in the build environment, so this is a selection of indexed recordings, not a verified complete channel import. Change order or selection in `content/site.json`.

External thumbnails load from YouTube; playback loads youtube-nocookie.com only after a click. The site has no analytics. If a thumbnail is blocked, the play control and title remain usable.

The authoring archive contains the essay's 36 supplied illustrations. These support its criticism and analysis; they are not used as decorative branding.
