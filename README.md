# Alexander Kucherov — Personal Website

Personal executive website for Alexander Kucherov: professional positioning, expertise, consulting/coaching/training
services, career experience, case studies, and a contact form.

A static site — plain HTML, CSS and vanilla JavaScript. No build step, no framework, no dependencies to install.

## Project structure

```
.
├── index.html              # All page content and structure (single page, anchor-linked sections)
├── css/
│   └── style.css           # Design system + responsive layout
├── js/
│   └── script.js           # Nav menu, scroll reveal, contact form validation/submission
└── assets/
    └── images/
        ├── portrait-placeholder.svg   # Replace with a real portrait photo
        ├── favicon.svg                 # Browser tab icon
        └── og-image-placeholder.png    # Social share preview image
```

## Running locally

No build tools are required. Any static file server works. From the project root:

```bash
# Python 3
python3 -m http.server 8000

# or Node (if you have it)
npx serve .
```

Then open `http://localhost:8000` in a browser. Opening `index.html` directly by double-clicking also works, though
a local server better matches how the site behaves once deployed.

## Deploying

Because it's a static site, any static host works out of the box — just upload the whole folder:

- **GitHub Pages**: enable Pages on this repository (Settings → Pages → deploy from the `main` branch, root folder).
- **Netlify / Vercel / Cloudflare Pages**: create a new site from this repo — no build command needed, publish
  directory is `/` (the repo root).
- **Any static host** (S3, Nginx, etc.): copy the contents of this folder to the web root.

## Where to update content

- **Text content** — everything (bio, services, experience, case studies) lives directly in `index.html`, organised
  into clearly commented `<section>` blocks. Section order matches the on-page navigation.
- **Portrait photo** — replace `assets/images/portrait-placeholder.svg` with a real photo. Either keep the same file
  name, or add your new file and update the `src` on the `<img>` inside the `hero-portrait` block in `index.html`
  (search for `REPLACE:`).
- **Favicon** — replace `assets/images/favicon.svg` with your own monogram or logo.
- **Social share image (Open Graph)** — replace `assets/images/og-image-placeholder.png` with a real 1200×630
  JPG/PNG for the best appearance when the site is shared on LinkedIn, Twitter/X, etc.
- **Contact details** — email and LinkedIn appear in the hero, contact section and footer of `index.html`. Update
  all three spots if they change.
- **Contact form** — the form (`#contactForm` in `index.html`) is front-end only: it validates input but does not
  send anything anywhere yet. `js/script.js` has a clearly marked block explaining how to wire it up to:
  - [Formspree](https://formspree.io) (set the form's `action` to your Formspree endpoint),
  - [EmailJS](https://www.emailjs.com) (send straight from the browser), or
  - a custom backend/API endpoint (`fetch()` to your own server).

## Notes

- Built mobile-first and fully responsive; tested down to small mobile widths.
- Uses [Google Fonts](https://fonts.google.com) (Fraunces + Inter) loaded via `<link>` in `index.html` — swap or
  self-host if you prefer not to depend on Google Fonts.
- All copy is grounded in Alexander's real professional experience; figures and achievements are not invented.
