#!/usr/bin/env python3
"""Generate every HTML page of thomasmoor.org (English at the root, French under /fr/).

Usage:  python tools/build.py
Edit the copy in tools/content.py, the styles in assets/css/style.css,
and the Google Analytics ID / Web3Forms key in assets/js/config.js.
"""
import json
from datetime import date
from pathlib import Path

from content import CONTENT, SERVICES

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://thomasmoor.org"
EMAIL = "contact@thomasmoor.org"
LINKEDIN = "https://www.linkedin.com/in/tmoor"
GITHUB = "https://github.com/thomasmoor"
YEAR = date.today().year
LANGS = ("en", "fr")

# --------------------------------------------------------------------- icons
_P = {
    "web": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/><path d="m9.5 7.5-2.5 2.5 2.5 2.5M14.5 7.5l2.5 2.5-2.5 2.5"/>',
    "terminal": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-6"/><path d="M16 8h4v4"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M10 10h4v4h-4z"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
}
_FILLED = {
    "linkedin": '<path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/>',
    "github": '<path d="M12 .3a12 12 0 0 0-3.8 23.38c.6.12.83-.26.83-.57l-.02-2.04c-3.34.72-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.08-.74.09-.73.09-.73 1.2.09 1.83 1.24 1.83 1.24 1.07 1.83 2.8 1.3 3.49 1 .1-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.14-.3-.54-1.52.1-3.18 0 0 1-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.28-1.55 3.29-1.23 3.29-1.23.64 1.66.24 2.88.12 3.18a4.65 4.65 0 0 1 1.23 3.22c0 4.61-2.8 5.63-5.48 5.92.42.36.81 1.1.81 2.22l-.01 3.29c0 .31.2.69.82.57A12 12 0 0 0 12 .3"/>',
}


def icon(name: str, cls: str = "icon") -> str:
    if name in _FILLED:
        return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{_FILLED[name]}</svg>'
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[name]}</svg>')


# --------------------------------------------------------------------- paths
class Ctx:
    """Everything a template needs to know about the page being rendered."""

    def __init__(self, lang: str, path: str):
        self.lang, self.path = lang, path            # path relative to the language root
        self.t = CONTENT[lang]
        depth = path.count("/") + (1 if lang == "fr" else 0)
        self.root = "../" * depth                    # to the site root
        self.lroot = self.root + ("fr/" if lang == "fr" else "")   # to this language's root
        self.other = "fr" if lang == "en" else "en"
        self.other_href = self.root + ("fr/" if self.other == "fr" else "") + path
        self.is_home = path == "index.html"

    def home(self, anchor: str = "") -> str:
        if self.is_home:
            return f"#{anchor}" if anchor else "#top"
        return self.lroot + "index.html" + (f"#{anchor}" if anchor else "")

    def url(self, lang: str | None = None) -> str:
        lang = lang or self.lang
        p = "" if self.path == "index.html" else self.path
        return f"{SITE}/{'fr/' if lang == 'fr' else ''}{p}"

    def asset(self, p: str) -> str:
        return self.root + "assets/" + p

    def service(self, slug: str) -> str:
        return f"{self.lroot}services/{slug}.html"


# --------------------------------------------------------------------- shared parts
def head(c: Ctx, title: str, desc: str, extra: str = "", noindex: bool = False) -> str:
    alts = "" if noindex else (
        f'<link rel="canonical" href="{c.url()}">\n'
        f'<link rel="alternate" hreflang="en" href="{c.url("en")}">\n'
        f'<link rel="alternate" hreflang="fr" href="{c.url("fr")}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{c.url("en")}">\n')
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f"""<!doctype html>
<html lang="{c.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}{alts}<meta property="og:type" content="website">
<meta property="og:site_name" content="Thomas Moor — Digital Services">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{c.url()}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:locale" content="{'fr_FR' if c.lang == 'fr' else 'en_GB'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1E2240">
<link rel="icon" href="{c.root}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{c.asset('img/favicon-32.png')}">
<link rel="icon" type="image/png" sizes="192x192" href="{c.asset('img/favicon-192.png')}">
<link rel="apple-touch-icon" href="{c.asset('img/apple-touch-icon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap">
<link rel="stylesheet" href="{c.asset('css/style.css')}">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'}});</script>
<script src="{c.asset('js/config.js')}"></script>
<script src="{c.asset('js/main.js')}" defer></script>
{extra}</head>
"""


def header(c: Ctx) -> str:
    n = c.t["nav"]
    return f"""<a class="skip-link" href="#main">{n['skip']}</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{c.home()}"><img src="{c.asset('img/logo.png')}" width="220" height="46" alt="Thomas Moor — Digital Services"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{n['menu']}">{icon('menu', 'icon icon-open')}{icon('close', 'icon icon-close')}</button>
    <nav id="site-nav" class="site-nav" aria-label="{n['main']}">
      <ul class="nav-links">
        <li><a href="{c.home('services')}">{n['services']}</a></li>
        <li><a href="{c.home('service-areas')}">{n['areas']}</a></li>
        <li><a href="{c.home('about')}">{n['about']}</a></li>
      </ul>
      <a class="header-email" href="mailto:{EMAIL}">{icon('mail')}<span>{EMAIL}</span></a>
      <a class="lang-switch" href="{c.other_href}" hreflang="{c.other}" lang="{c.other}" title="{CONTENT[c.other]['lang_name']}">{c.other.upper()}</a>
    </nav>
  </div>
</header>
"""


def footer(c: Ctx) -> str:
    f, ck = c.t["footer"], c.t["cookie"]
    services = "\n".join(
        f'          <li><a href="{c.service(s["slug"])}">{c.t["services"][s["slug"]]["name"]}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <p class="footer-brand">Thomas Moor Digital Services</p>
      <a class="footer-email" href="mailto:{EMAIL}">{icon('mail')}<span>{EMAIL}</span></a>
      <div class="social">
        <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{icon('linkedin')}</a>
        <a href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub">{icon('github')}</a>
      </div>
    </div>
    <div>
      <h2 class="footer-title">{f['services']}</h2>
      <ul class="footer-list">
{services}
      </ul>
    </div>
    <div>
      <h2 class="footer-title">{f['info']}</h2>
      <ul class="footer-list">
        <li><a href="{c.home('about')}">{f['about']}</a></li>
        <li><a href="{c.lroot}privacy.html">{f['privacy']}</a></li>
        <li><button type="button" class="link-button" data-cookie-settings>{f['cookies']}</button></li>
        <li><a href="{c.other_href}" hreflang="{c.other}" lang="{c.other}">{f['other_lang']}</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© {YEAR} Thomas Moor Consulting. {f['rights']}</p>
    <p><a href="{SITE}">thomasmoor.org</a></p>
  </div>
</footer>
<div class="cookie-banner" id="cookie-banner" role="dialog" aria-label="{ck['label']}" hidden>
  <p>{ck['text']} <a href="{c.lroot}privacy.html">{ck['more']}</a></p>
  <div class="cookie-actions">
    <button type="button" class="btn btn-ghost" data-consent="denied">{ck['decline']}</button>
    <button type="button" class="btn btn-primary" data-consent="granted">{ck['accept']}</button>
  </div>
</div>
</body>
</html>
"""


def cta_band(c: Ctx) -> str:
    sp = c.t["service_page"]
    return f"""<section class="cta-band">
        <div>
          <h2>{sp['cta_title']}</h2>
          <p>{sp['cta_text']}</p>
        </div>
        <a class="btn btn-light" href="{c.home('contact')}">{sp['cta_btn']} {icon('arrow')}</a>
      </section>"""


def write(c: Ctx, html: str) -> None:
    out = ROOT / ("fr" if c.lang == "fr" else "") / c.path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")
    print("wrote", out.relative_to(ROOT).as_posix())


def picture(c: Ctx, stem: str, alt: str, w: int, h: int, cls: str = "", lazy: bool = True) -> str:
    loading = ' loading="lazy" decoding="async"' if lazy else ""
    return (f'<picture><source srcset="{c.asset(f"img/{stem}.webp")}" type="image/webp">'
            f'<img src="{c.asset(f"img/{stem}.jpg")}" width="{w}" height="{h}" alt="{alt}"{loading}'
            f'{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}></picture>')


# --------------------------------------------------------------------- pages
def home_page(lang: str) -> None:
    c = Ctx(lang, "index.html")
    t, fm = c.t, c.t["form"]
    privacy = f"{c.lroot}privacy.html"

    svc_opts = "\n".join(
        f'              <option value="{CONTENT["en"]["services"][s["slug"]]["name"]}">{t["services"][s["slug"]]["name"]}</option>'
        for s in SERVICES)
    when_opts = "\n".join(f'              <option value="{v}">{label}</option>' for v, label in fm["when_opts"])
    msgs = json.dumps(fm["msg"], ensure_ascii=False).replace('"', "&quot;")

    cards = "\n".join(f"""        <a class="service-card" href="{c.service(s['slug'])}">
          <span class="service-icon">{icon(s['icon'])}</span>
          <h3>{t['services'][s['slug']]['name']}</h3>
          <p>{t['services'][s['slug']]['short']}</p>
          <span class="card-link">{t['services_section']['more']} {icon('arrow')}</span>
        </a>""" for s in SERVICES)

    a = t["areas"]
    chips = "".join(f'<li class="chip">{icon("globe")}{r}</li>' for r in a["regions"])
    features = "\n".join(f"""          <div class="feature">
            <span class="feature-icon">{icon(ic)}</span>
            <div><h3>{title}</h3><p>{text}</p></div>
          </div>""" for ic, title, text in a["features"])

    ab = t["about_section"]
    stats = "".join(f'<div class="stat"><strong>{n}</strong><span>{label}</span></div>' for n, label in ab["stats"])
    about_p = "\n".join(f"          <p>{p}</p>" for p in t["about"][:2])

    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "Thomas Moor — Digital Services", "legalName": "Thomas Moor Consulting",
        "url": SITE, "email": EMAIL, "image": f"{SITE}/assets/img/og-image.jpg",
        "logo": f"{SITE}/assets/img/logo.png", "areaServed": "Worldwide",
        "founder": {"@type": "Person", "name": "Thomas Moor"},
        "sameAs": [LINKEDIN, GITHUB], "knowsLanguage": ["en", "fr"],
    }, ensure_ascii=False)
    extra = (f'<link rel="preload" as="image" href="{c.asset("img/hero.webp")}" type="image/webp">\n'
             f'<script type="application/ld+json">{jsonld}</script>\n')

    body = f"""<body class="page-home">
{header(c)}<main id="main">
  <section class="hero" id="contact">
    <div class="container hero-grid">
      <div class="hero-text">
        <h1 class="eyebrow">{t['h1']}</h1>
        <h2 class="hero-title">{t['hero']['title']}</h2>
        <p class="hero-lead">{t['hero']['lead']}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#services">{t['hero']['cta1']} {icon('arrow')}</a>
          <a class="btn btn-ghost" href="mailto:{EMAIL}">{icon('mail')} {EMAIL}</a>
        </div>
      </div>
      <div class="form-card">
        <h3>{fm['title']}</h3>
        <p class="form-intro">{fm['intro']}</p>
        <form id="contact-form" class="contact-form" action="https://api.web3forms.com/submit" method="POST" novalidate data-messages="{msgs}">
          <input type="hidden" name="access_key" value="">
          <input type="hidden" name="subject" value="{fm['subject']}">
          <input type="hidden" name="from_name" value="thomasmoor.org">
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="field">
            <label for="f-name">{fm['name']} <span class="req" title="{fm['required']}">*</span></label>
            <input id="f-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-phone">{fm['phone']}</label>
              <input id="f-phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div class="field">
              <label for="f-email">{fm['email']}</label>
              <input id="f-email" name="email" type="email" autocomplete="email">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-service">{fm['service']}</label>
              <select id="f-service" name="service">
              <option value="">{fm['service_ph']}</option>
{svc_opts}
              </select>
            </div>
            <div class="field">
              <label for="f-when">{fm['when']}</label>
              <select id="f-when" name="when_needed">
              <option value="">{fm['when_ph']}</option>
{when_opts}
              </select>
            </div>
          </div>
          <div class="field">
            <label for="f-message">{fm['message']}</label>
            <textarea id="f-message" name="message" rows="4" placeholder="{fm['message_ph']}"></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-block">{fm['submit']} {icon('arrow')}</button>
          <p class="form-status" role="status" aria-live="polite"></p>
          <p class="form-note">{fm['note'].format(privacy=privacy)}</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section" id="services">
    <div class="container">
      <div class="section-head">
        <p class="kicker">{t['services_section']['kicker']}</p>
        <h2 class="section-title">{t['services_section']['title']}</h2>
        <p>{t['services_section']['intro']}</p>
      </div>
      <div class="cards">
{cards}
      </div>
    </div>
  </section>

  <section class="section section-alt" id="service-areas">
    <div class="container areas-grid">
      <div class="areas-text">
        <p class="kicker">{a['kicker']}</p>
        <h2 class="section-title">{a['title']}</h2>
        <p>{a['text']}</p>
        <ul class="chips">{chips}</ul>
      </div>
      <div class="features">
{features}
      </div>
    </div>
  </section>

  <section class="section" id="about">
    <div class="container about-grid">
      <div class="portrait">{picture(c, 'thomas-moor', 'Thomas Moor', 640, 800)}</div>
      <div class="about-text">
        <p class="kicker">{ab['kicker']}</p>
        <h2 class="section-title">{ab['title']}</h2>
{about_p}
        <div class="stats">{stats}</div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{c.lroot}about.html">{ab['more']} {icon('arrow')}</a>
          <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">{icon('linkedin')} LinkedIn</a>
        </div>
      </div>
    </div>
  </section>
</main>
{footer(c)}"""
    write(c, head(c, t["meta"]["home_title"], t["meta"]["home_desc"], extra) + body)


def about_page(lang: str) -> None:
    c = Ctx(lang, "about.html")
    t, ap = c.t, c.t["about_page"]
    paras = "\n".join(f"        <p>{p}</p>" for p in t["about"])
    rows = "\n".join(f"          <div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in ap["rows"])
    steps = "\n".join(f"""        <div class="step"><span class="step-num">0{i}</span><h3>{h}</h3><p>{p}</p></div>"""
                      for i, (h, p) in enumerate(ap["approach"], 1))
    body = f"""<body class="page-about">
{header(c)}<main id="main">
  <section class="page-hero">
    <div class="container">
      <h1 class="eyebrow">{t['h1']}</h1>
      <h2 class="page-subtitle">{t['h2']}</h2>
      <a class="email-link" href="mailto:{EMAIL}">{icon('mail')}<span>{EMAIL}</span></a>
    </div>
  </section>

  <section class="section">
    <div class="container about-grid">
      <div class="portrait">{picture(c, 'thomas-moor', 'Thomas Moor', 640, 800, lazy=False)}</div>
      <div class="prose">
{paras}
        <div class="glance">
          <h2 class="glance-title">{ap['glance']}</h2>
          <dl>
{rows}
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head"><h2 class="section-title">{ap['approach_title']}</h2></div>
      <div class="steps">
{steps}
      </div>
      {cta_band(c)}
    </div>
  </section>
</main>
{footer(c)}"""
    write(c, head(c, t["meta"]["about_title"], t["meta"]["about_desc"]) + body)


def service_page(lang: str, svc: dict) -> None:
    slug = svc["slug"]
    c = Ctx(lang, f"services/{slug}.html")
    t, sp, s = c.t, c.t["service_page"], c.t["services"][slug]
    intro = "\n".join(f"        <p>{p}</p>" for p in s["intro"])
    why = "\n".join(f"        <p>{p}</p>" for p in s["why"])
    expect = "\n".join(f'          <li><span class="check">{icon("check")}</span><span>{e}</span></li>' for e in s["expect"])
    others = "\n".join(
        f'          <li><a href="{c.service(o["slug"])}"{" aria-current=" + chr(34) + "page" + chr(34) if o["slug"] == slug else ""}>'
        f'{icon(o["icon"])}<span>{t["services"][o["slug"]]["name"]}</span></a></li>' for o in SERVICES)
    plain_name = s["name"].replace("&amp;", "&")
    body = f"""<body class="page-service">
{header(c)}<main id="main">
  <section class="page-hero">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="{c.home()}">{sp['breadcrumb_home']}</a> <span aria-hidden="true">/</span> <a href="{c.home('services')}">{sp['breadcrumb_services']}</a></nav>
      <div class="service-hero">
        <span class="service-icon service-icon-lg">{icon(svc['icon'])}</span>
        <div>
          <h1 class="page-title">{s['name']}</h1>
          <p class="page-lead">{s['short']}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container content-grid">
      <article class="prose">
{intro}
        <h2>{sp['why']}</h2>
{why}
        <h2>{sp['expect']}</h2>
        <ul class="check-list">
{expect}
        </ul>
      </article>
      <aside class="aside-card">
        <h2 class="aside-title">{sp['others']}</h2>
        <ul>
{others}
        </ul>
        <a class="btn btn-primary btn-block" href="{c.home('contact')}">{sp['cta_btn']}</a>
      </aside>
    </div>
    <div class="container">
      {cta_band(c)}
    </div>
  </section>
</main>
{footer(c)}"""
    title = f"{s['name']} | Thomas Moor — {'Services numériques' if lang == 'fr' else 'Digital Services'}"
    desc = s["short"].replace("&amp;", "&").replace('"', "&quot;")
    write(c, head(c, title, desc) + body)


def privacy_page(lang: str) -> None:
    c = Ctx(lang, "privacy.html")
    t, p = c.t, c.t["privacy"]
    secs = "\n".join(
        f"        <h2>{h}</h2>\n" + "\n".join(f"        <p>{x}</p>" for x in paras) for h, paras in p["sections"])
    body = f"""<body class="page-privacy">
{header(c)}<main id="main">
  <section class="page-hero">
    <div class="container">
      <h1 class="page-title">{p['title']}</h1>
      <p class="page-lead">{p['updated']}</p>
    </div>
  </section>
  <section class="section">
    <div class="container narrow">
      <article class="prose">
{secs}
        <p><button type="button" class="btn btn-ghost" data-cookie-settings>{t['footer']['cookies']}</button></p>
      </article>
    </div>
  </section>
</main>
{footer(c)}"""
    write(c, head(c, t["meta"]["privacy_title"], t["meta"]["privacy_desc"]) + body)


def not_found_page() -> None:
    # GitHub Pages serves /404.html for every missing URL, so it uses absolute paths.
    c = Ctx("en", "404.html")
    c.root, c.lroot, c.other_href = "/", "/", "/fr/"
    en, fr = CONTENT["en"]["notfound"], CONTENT["fr"]["notfound"]
    body = f"""<body class="page-404">
{header(c)}<main id="main">
  <section class="page-hero page-hero-full">
    <div class="container narrow center">
      <p class="big-404">404</p>
      <h1 class="page-title">{en['title']}</h1>
      <p class="page-lead">{en['text']}</p>
      <p class="page-lead" lang="fr">{fr['text']}</p>
      <div class="hero-actions center">
        <a class="btn btn-primary" href="/">{en['btn']}</a>
        <a class="btn btn-ghost" href="/fr/" lang="fr">{fr['btn']}</a>
      </div>
    </div>
  </section>
</main>
{footer(c)}"""
    write(c, head(c, f"{en['title']} | Thomas Moor — Digital Services", en["text"], noindex=True) + body)


def sitemap() -> None:
    paths = ["index.html", "about.html", "privacy.html"] + [f"services/{s['slug']}.html" for s in SERVICES]
    today = date.today().isoformat()
    items = []
    for p in paths:
        c = Ctx("en", p)
        for lang in LANGS:
            items.append(f"""  <url>
    <loc>{c.url(lang)}</loc>
    <lastmod>{today}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{c.url('en')}"/>
    <xhtml:link rel="alternate" hreflang="fr" href="{c.url('fr')}"/>
  </url>""")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(items) + "\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8", newline="\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    for lang in LANGS:
        home_page(lang)
        about_page(lang)
        privacy_page(lang)
        for s in SERVICES:
            service_page(lang, s)
    not_found_page()
    sitemap()
