# Alexander Kucherov — Personal Website

Bilingual (EN/RU) business-card site for Alexander Kucherov: positioning, expertise, consulting services, a catalogue
of 20 fixed-scope products/done-for-you services, career experience, case studies, and a contact form.

A static site — plain HTML, CSS and vanilla JavaScript. No build step is required to *run* the site, but content is
now generated from a small Python script so the two language versions never drift apart (see below).

## Project structure

```
.
├── index.html              # Generated file — do not hand-edit for content changes, see "Editing content" below
├── content.py               # All page text, EN + RU, as plain Python data (edit THIS to change copy)
├── build.py                  # Generates index.html from content.py
├── css/
│   └── style.css            # Design system + responsive layout + i18n toggle + icon styles
├── js/
│   └── script.js             # Nav menu, scroll reveal, language switch, contact form validation
└── assets/
    └── images/
        ├── portrait-placeholder.svg   # Replace with a real portrait photo
        ├── favicon.svg                 # Browser tab icon
        └── og-image.png                # Social share preview image (branded card — swap for a photo-based one if you like)
```

## Editing content (bilingual)

Text content lives in `content.py`, not directly in `index.html`. Every piece of copy is stored as an
`(english, russian)` pair. To change anything — fix a typo, add a product, update a number — edit `content.py`,
then regenerate the HTML:

```bash
python3 build.py
```

This overwrites `index.html`. If you ever hand-edit `index.html` directly, your changes will be lost the next time
someone runs `build.py` — treat `content.py` as the source of truth.

### How the language switch works

- The header has an **EN / RU** toggle. On load, a small inline script guesses the visitor's language from their
  browser (`navigator.language`) and shows that version by default — useful since LinkedIn visitors likely want
  English and profi.ru/Avito visitors likely want Russian.
- Every bilingual element in the HTML has two versions marked `data-lang="en"` / `data-lang="ru"`; CSS shows only
  the one matching `html[data-lang]`. No page reload, no external translation library.
- The choice is **not** saved between visits (no `localStorage`) — each visit re-detects from the browser. If you
  want the choice to persist, add a `localStorage` read/write in `js/script.js`'s `setLang()` function — it's a
  couple of lines, deliberately left out for a clean, dependency-free default.
- Search-engine metadata (`<title>`, `<meta description>`, Open Graph tags) stays in English, since LinkedIn is the
  primary link-sharing channel. If Russian marketplaces need their own preview text, that's normally set directly
  on the marketplace listing (profi.ru/Avito don't read your site's `<meta>` tags anyway).

## Running locally

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploying

- **GitHub Pages** (current setup): Settings → Pages → deploy from the `main` branch, root folder. Your current
  URL: `https://alexandrkucherovinfo-glitch.github.io/personal-website/`.
- **Custom domain on GitHub Pages (paid)**: buy a domain (e.g. from Cloudflare Registrar, Reg.ru, or Namecheap), add
  a `CNAME` file to the repo root containing just your domain (e.g. `alexanderkucherov.com`), then point the
  domain's DNS at GitHub Pages (an `A`/`ALIAS` record to GitHub's IPs, or a `CNAME` record to
  `alexandrkucherovinfo-glitch.github.io` for a subdomain like `www.`). GitHub's own docs walk through this exact
  flow: Settings → Pages → Custom domain.
- **Free domain via DuckDNS (what this repo is currently set up for — done)**: a `CNAME` file sits in the repo root
  containing `citiservice.duckdns.org`, DuckDNS's `citiservice` subdomain is pointed at GitHub Pages' IP
  `185.199.108.153`, and the custom domain is already set in Settings → Pages with a successful DNS check. GitHub
  is issuing the HTTPS certificate automatically (can take up to ~15 minutes, occasionally longer) — once it's
  ready, tick **Enforce HTTPS** in Settings → Pages.
  - Use the site at `https://citiservice.duckdns.org` — **not** `www.citiservice.duckdns.org`. DuckDNS gives you
    exactly one hostname per subdomain you register; it doesn't support adding a `www.` in front of it for free, so
    that address won't resolve.
  4. Worth knowing before you commit to this: the address will always visibly end in `duckdns.org`, which reads as
     a free dynamic-DNS service to anyone who looks closely — fine for links on profi.ru/Avito/LinkedIn, less
     "official" than a real domain for, say, a corporate proposal. A handful of corporate networks also filter
     `*.duckdns.org` more aggressively (it's commonly used for home servers), which can occasionally affect
     recipients on strict work networks. Neither is a real blocker — just the trade-off for €0/year versus ~$10–15
     for a domain of your own later, if you ever want to.

## Where to update things

- **All text (EN + RU)** — `content.py`, then run `python3 build.py`.
- **Portrait photo** — replace `assets/images/portrait-placeholder.svg` with a real photo (any format), then update
  the `src` on the `<img>` inside the `hero-portrait` block in `index.html`... but remember `index.html` is
  regenerated from `content.py`/`build.py` and doesn't currently template the image path — if you change the image
  filename, update the `TEMPLATE` string's `<img src=...>` line in `build.py` too, so it survives regeneration.
- **Favicon** — replace `assets/images/favicon.svg`.
- **Social share image** — replace `assets/images/og-image.png` (1200×630). The current one is a generated branded
  card, not a photo — swap it for something more personal if you like.
- **Contact details** — email and LinkedIn are set directly in `build.py`'s `main()` function (search for the
  email address) since they're identical in both languages.
- **Contact form** — front-end only, same as before: see the comment block in `js/script.js` for wiring it up to
  Formspree, EmailJS, or a custom backend.
- **Product prices** — the 20 items in the *Products* section intentionally show a *format* tag (e.g. "Fixed price
  · 3–5 days") instead of a dollar amount, since pricing wasn't specified when this was built. Add real prices in
  `content.py` (the `tag_en` / `tag_ru` fields in `PRODUCT_GROUPS`) once you've decided on them.

## Notes

- Built mobile-first and fully responsive.
- Uses [Google Fonts](https://fonts.google.com) (Fraunces + Inter) — swap or self-host if you prefer not to depend
  on Google Fonts.
- Icons are a small hand-built inline SVG sprite (`build_sprite()` in `build.py` / `ICONS` in `content.py`) — no
  external icon library or network request involved.
- All copy is grounded in Alexander's real professional experience; figures and achievements are not invented. The
  20 "Products" are new packaged offerings suggested from that same experience — review the copy before publishing,
  especially anything implying a specific delivery time or price format.
