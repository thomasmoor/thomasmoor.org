# thomasmoor.org — Thomas Moor Digital Services

Static, bilingual (EN / FR) website hosted on GitHub Pages at <https://thomasmoor.org>.

## Structure

```
index.html, about.html, privacy.html, 404.html   English pages (generated)
services/*.html                                  English service pages (generated)
fr/…                                             French pages (generated)
assets/css/style.css                             All styles
assets/js/config.js                              Google Analytics ID + Web3Forms key  ← edit me
assets/js/main.js                                Header, mobile menu, cookie consent, contact form
assets/img/                                      Optimised images
tools/content.py                                 All page copy (EN + FR)
tools/build.py                                   Generates every HTML page from content.py
tools/optimize_images.py                         Rebuilds assets/img from the source images
CNAME, .nojekyll, robots.txt, sitemap.xml        GitHub Pages / SEO
```

## Edit content

1. Change the text in `tools/content.py` (or the layout in `tools/build.py`).
2. Run `python tools/build.py` to regenerate all pages.
3. Commit and push. GitHub Pages republishes automatically.

Don't edit the generated `.html` files by hand: the next build overwrites them.

## Before going live

- **Contact form**: create a free access key at <https://web3forms.com> using contact@thomasmoor.org, then paste it into `web3formsKey` in `assets/js/config.js`.
- **Google Analytics**: create a GA4 property, then paste the Measurement ID (`G-…`) into `gaId` in `assets/js/config.js`. GA loads only after a visitor clicks “Accept” on the cookie banner (Consent Mode v2).

## Local preview

```
python -m http.server 8080
```

Then open <http://localhost:8080>.

## GitHub Pages and the domain

- Repository → Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
- The `CNAME` file sets the custom domain `thomasmoor.org`. At your DNS provider, add:
  - `A` records for `@` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - `CNAME` record for `www` → `thomasmoor.github.io`
- After DNS has propagated, tick **Enforce HTTPS** in Settings → Pages.
