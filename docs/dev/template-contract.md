# The template contract

Every folder under `templates/` follows this contract. `templates/plain` is
the contract as code; `tools/check.py` enforces the parts a script can see;
this page is the prose. When the three disagree, fix all three.

The point of a contract: every template uses the **same markup and class
names**, so switching a site from one template to another is a swap of
`css/`, `fonts/` and `assets/`, and someone who has learned one template has
learned them all.

## 1. Files

```
templates/<name>/
├── README.md              install set vs showcase set, browsers, fonts, the retoken paste-in
├── index.html             overview — navbar layout — uses every component at least once
├── blogpost.html          the fixture article inside the post shell — navbar layout
├── forms.html             the fixture form inside a page — navbar layout
├── sidebar.html           the overview again in the sidebar layout
├── css/theme.css          tokens (see §5)
├── css/global.css         everything else, in marked sections (see §6)
├── js/theme.js            scheme boot + tri-state toggle + data-scheme mirror
├── js/copy.js             copy buttons — docs pages only
├── fonts/                 only when fonts are self-hosted; otherwise absent
├── assets/                favicon.svg, avatar.svg, fixture-photo-1.svg, fixture-photo-2.svg, and the template's own art
├── docs/                  sidebar layout throughout
│   ├── index.html         get started
│   ├── theme.html         tokens and the palette block
│   ├── defaults.html      bare native elements
│   ├── blog.html          anatomy of the post shell
│   └── components/        index.html + one page per component (§4)
└── example/               index.html + exactly two more pages — navbar layout
```

**Install set** (what a user keeps): `css/`, `js/theme.js`, `fonts/`,
`assets/`, `README.md`. Nothing in it references anything outside it.

**Showcase set** (what a user deletes): the four top-level pages, `docs/`,
`example/`, `js/copy.js`.

`<name>` is the folder name: lowercase, hyphens. It is also the value of
`data-theme` and the prefix of every template-specific class and token.

## 2. The head block

Every page, verbatim except for the relative prefix (`../` per level of
depth) and the title:

```html
<!doctype html>
<html lang="en" data-theme="<name>">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>Page — Template</title>
  <link rel="icon" href="assets/favicon.svg">
  <script src="js/theme.js"></script>
  <link rel="stylesheet" href="css/theme.css">
  <link rel="stylesheet" href="css/global.css">
</head>
```

Rules: `theme.js` is a plain synchronous script (no `defer`, `async` or
`type="module"`) and comes **before** the stylesheets, so the stored scheme
is applied before first paint. A template that uses Google Fonts adds, after
`global.css`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">
```

That is the only external resource a template may load. Hyperlinks (`<a>`)
may point anywhere.

## 3. Links and paths

- Relative only. Never root-absolute (`/css/…`), never a directory
  (`docs/`): point at the file (`docs/index.html`). The same folder must
  work at `file://`, at a sub-path on a host, and inside someone's `public/`.
- A page may not link outside its template folder, with one exception: a
  single `<a class="site-link" href="…/index.html">All templates</a>` in the
  navbar and in the sidebar footer, pointing at the repo landing. The
  get-started page tells users to delete it.
- `css/` and `js/theme.js` reference only `css/`, `assets/` and `fonts/`.
- Example pages link back to `../index.html`.

## 4. Pages, layouts and navigation

| Page | Layout | Role |
| --- | --- | --- |
| `index.html` | navbar | Overview in the template's voice. Must use: `.card`, `.card-horizontal`, `.card-feature`, `.fifty-fifty`, `.gallery` + `.lightbox`, `.accordion`, `.switch`, `hr.page-break`, `dialog.modal`, `.banner`, `.badge`, `.data-table`, `.btn`, `.navbar`, `.footer`. Links to every other page. |
| `blogpost.html` | navbar | The post shell (`article.post` with `.post-header`, `.author-card`, `.meta`, `.tags`) around `fixtures/markdown-test.html`'s article, verbatim. |
| `forms.html` | navbar | `fixtures/forms.html`'s form, verbatim, inside a page. |
| `sidebar.html` | sidebar | The overview content in the sidebar layout. |
| `docs/index.html` | sidebar | Get started: the head block, the install set, the deletable set, the browser floor, fonts, the `site-link` line to delete. |
| `docs/theme.html` | sidebar | The 19 swatches rendered twice (a `.themed` subtree with `style="color-scheme: light"` and one with `dark`), semantic and shared token tables, template tokens, the palette block as `<code data-snippet="palette">`, the retoken adoption line. |
| `docs/defaults.html` | sidebar | Bare native elements — headings, text, lists, tables, code, media, controls — with no component classes, inside `.prose`. |
| `docs/blog.html` | sidebar | Anatomy: a labelled skeleton of the post shell and its snippet; links to `blogpost.html`. |
| `docs/components/index.html` | sidebar | Grid of every component with a one-line description. |
| `docs/components/<c>.html` | sidebar | See §4.3. |
| `example/*.html` | navbar | A small real site: `index.html` + exactly two more. Must use the navbar, a hero or a fifty-fifty, a card grid, a `.field` form, a dialog or an accordion, and the footer. |

### 4.1 Navbar layout

```html
<header class="navbar">
  <a class="brand" href="index.html">Template</a>
  <button class="nav-toggle" type="button" popovertarget="site-nav" aria-label="Menu">☰</button>
  <nav id="site-nav" popover>
    <a href="index.html" aria-current="page">Overview</a>
    <a href="blogpost.html">Blog post</a>
    <a href="forms.html">Forms</a>
    <a href="sidebar.html">Sidebar</a>
    <a href="docs/index.html">Docs</a>
    <a href="example/index.html">Example</a>
  </nav>
  <button class="scheme-toggle" type="button" data-scheme="auto" aria-label="Theme: auto"></button>
  <a class="site-link" href="../../index.html">All templates</a>
</header>
<main class="page">…</main>
<footer class="footer">…</footer>
```

The toggle button is empty: its glyph is CSS generated content keyed to
`data-scheme`. Below the breakpoint (`48rem`) the `<nav>` is a popover opened by the real
button — ESC and light-dismiss come free, `::backdrop` is the scrim. Above
it a media query makes the nav static and hides the button. The same link
set appears on `index.html`, `blogpost.html` and `forms.html`; the checker
compares them. Example pages carry their own site nav.

### 4.2 Sidebar layout

```html
<div class="sidebar-layout">
  <header class="topbar">
    <button class="sidebar-toggle" type="button" popovertarget="sidebar" aria-label="Navigation">☰</button>
    <span class="topbar-title">Docs</span>
    <button class="scheme-toggle" type="button" data-scheme="auto" aria-label="Theme: auto"></button>
  </header>
  <aside class="sidebar" id="sidebar" popover>
    <nav>
      <details open><summary>Pages</summary>
        <a href="../index.html">Overview</a> …
      </details>
      <details open><summary>Docs</summary> … </details>
      <details open><summary>Components</summary> … </details>
      <details open><summary>Example</summary> … </details>
    </nav>
    <p class="sidebar-footer"><a class="site-link" href="../../index.html">All templates</a></p>
  </aside>
  <main class="page">…</main>
</div>
```

Groups and their links, in this order — identical on every sidebar page:
**Pages** (Overview, Blog post, Forms, Sidebar variant) · **Docs** (Get
started, Theme, Defaults, Blog anatomy) · **Components** (Index, then the 17
in §4.3 order) · **Example** (the example home). The link to the current
page carries `aria-current="page"`. Below `64rem` the aside is a popover
drawer; above it, static. There is no desktop collapse in 0.1.0.

### 4.3 Component pages

Order: accordion, cards, hero, fifty-fifty, gallery, switch, page-break, buttons,
forms, dialog, navbar, sidebar, banner, badge, table, author-card, footer,
flare. Each page, in this order:

1. **Preview** — `<figure class="example" data-snippet="<key>">` holding the
   live component.
2. **Markup** — `<pre><code data-snippet="<key>">` with the same markup,
   escaped, plus a copy button. The checker compares the two.
3. **Variants** — each variant is its own preview + snippet pair with its own
   key (and its own ids).
4. **Classes** — a table: class, purpose; the heading names the section of
   `global.css` where the rules live (`global.css § cards`).
5. **Notes** — behaviour, keyboard, whether any JavaScript is involved.
6. Prev / next links to the neighbouring component pages.

Page-level components (navbar, sidebar, footer) cannot be shown live inside
a sidebar page, so their pages embed the real page in an
`<iframe src="../../index.html" title="…">` and pair the snippet by
reference: `<code data-snippet="navbar" data-source="../../index.html"
data-select="header.navbar">`.

## 5. Components

| Component | Markup |
| --- | --- |
| Accordion | `<details class="accordion"><summary>Title</summary><div class="accordion-body">…</div></details>`. A group: `<div class="accordion-group">` of accordions sharing `name="faq"` (exclusive open). |
| Cards | `<article class="card"><figure class="card-media"><img …></figure><div class="card-body"><h3 class="card-title">…</h3><p class="card-text">…</p></div></article>`. Media may be an `<img>` or an inline `<svg class="card-icon">`. What is drawn inside the `<svg>` is content, not contract. Variants: `.card-horizontal` (media left), `.card-horizontal.card-media-end` (media right), `.card-feature` (the template's dynamic card). |
| Hero | `<section class="hero"><div class="stack"><p class="kicker">…</p><h1>…</h1><p>…</p><div class="row"><a class="btn btn-primary btn-lg">…</a></div></div><img …></section>`. The picture may be an `<img>` or the template's flare. The hero's shape is the template's own (decision 21); the contract asks only for `.hero` with a `.stack`. Each template documents two variants on `docs/components/hero.html`: its own hero, and one animated `.<name>-*` modifier that stops under `prefers-reduced-motion`. |
| Fifty-fifty | `<section class="fifty-fifty"><figure><img …></figure><div class="fifty-fifty-body"><h2>…</h2><p>…</p><a class="btn btn-primary" href="…">…</a></div></section>`. `.fifty-fifty-reverse` puts the image on the right. Stacks image-first below `48rem`. |
| Gallery + lightbox | `<ul class="gallery">` of `<li><figure><a href="#lb-1" onclick="document.getElementById('lightbox').showModal()"><img …></a><figcaption>…</figcaption></figure></li>` and, after the list, one `<dialog class="lightbox" id="lightbox">` holding `<figure class="lightbox-slide" id="lb-1"><img …><figcaption>…</figcaption><nav class="lightbox-nav"><a href="#lb-8">‹</a><a href="#lb-2">›</a></nav></figure>` per image and a `<form method="dialog"><button class="lightbox-close" type="submit" aria-label="Close">×</button></form>`. `:target` shows a slide; the first slide shows when nothing is targeted. |
| Switch | `<label class="switch"><input type="checkbox" role="switch"><span>Label</span></label>` |
| Page break | `<hr>` (plain) and `<hr class="page-break">` (the template's ornament). |
| Buttons | `<button class="btn" type="button">`, `.btn-primary`, `.btn-danger`, `.btn-sm`, `.btn-lg`, `:disabled`. Every button that is not a submit carries `type="button"`. `<a class="btn">` is allowed. |
| Forms | `<div class="field"><label for="x">…</label><input id="x" …><p class="hint">…</p></div>`; invalid: `.field.field-invalid` with `aria-invalid="true"` and `<p class="error" id="…">` referenced by `aria-describedby`; groups: `<span class="field-label">` + `<label class="check"><input type="checkbox|radio"> …</label>`; `.form-grid` on the form; `.field-wide` spans the grid; `.form-actions` holds the buttons. |
| Dialog | `<dialog class="modal" id="m1"><h2>…</h2><p>…</p><form method="dialog" class="modal-actions"><button class="btn" type="submit">Close</button></form></dialog>`; opener: `<button class="btn" type="button" onclick="document.getElementById('m1').showModal()">`. |
| Banner | `<div class="banner banner-success" role="status">…</div>`; `-warning`, `-danger` (`role="alert"`), `-info`. |
| Badge | `<span class="badge">…</span>`; `.badge-done`, `.badge-active`. |
| Table | `<div class="table-wrap"><table class="data-table">…</table></div>` |
| Author card | `<aside class="author-card"><img class="avatar" src="assets/avatar.svg" alt=""><div><strong class="author-name">…</strong><p class="author-bio">…</p><p class="meta"><time datetime="…">…</time> · <span>5 min read</span></p><p class="tags"><a class="tag" href="#">…</a></p></div></aside>` |
| Footer | `<footer class="footer"><div class="footer-columns"><section><h2>…</h2><ul>…</ul></section>…</div><p class="footer-note">…</p></footer>` |
| Flare | Anything else the template needs. Classes are `.<name>-*`; when flare needs markup it sits inside `<div class="<name>-flare">` so a template swap can strip it. Documented on `docs/components/flare.html`. |

Utilities, from retoken: `.page`, `.page-header`, `.stack`, `.row`,
`.grid-2`, `.muted`, `.small`, `.check`, `.visually-hidden`, `.prose`.
Retemplate adds `.grid-3`, `.container`, `.btn-lg`, `.banner-info`.

Plain `.prose` styles every markdown construct in the fixture: h1–h6,
paragraphs, `em`/`strong`/`del`, `code` and `pre`, `blockquote` (nested),
lists (nested, `.task-list`), tables (`.align-left/center/right`), images,
`hr`, `dl`, `details`, `abbr`, `kbd`, `mark`, `sub`/`sup`, `.footnotes`.

## 6. Tokens — `css/theme.css`

In this order:

1. `:root, .themed { … }` — retoken's **colour mapping, verbatim** (from
   retoken's `theme.css`: `color-scheme: light dark`, `--color-*`,
   `--bg-color`, `--surface-color`, `--surface-raised-color`,
   `--border-color`, `--text-color`, `--text-muted-color`, `--editor-*`,
   `--syntax-*`, `--shadow-1`, `--shadow-2`), then the **23 shared tokens**
   retoken's editor lists (`--font-body`, `--font-mono`, `--font-size-sm`,
   `-base`, `-lg`, `-xl`, `-2xl`, `--line-height`, `--space-1` … `-6`,
   `--radius-sm`, `-md`, `-lg`, `-full`, `--page-max-width`,
   `--sidebar-width`, `--panel-width`, `--toc-width`, `--navbar-height`)
   with the template's own values, then retemplate's four extra shared
   tokens: `--font-display`, `--font-weight-display`, `--font-size-3xl`,
   `--font-size-hero`.
2. The **palette block**, in retoken's named form and nothing else:
   ```css
   :root[data-theme='<name>'], [data-theme='<name>'] {
     --pal-bg0: light-dark(#…, #…);
     /* … all 19 slots … */
   }
   ```
   Slots: `--pal-bg0`, `--pal-bg0-soft`, `--pal-bg1`, `--pal-bg2`,
   `--pal-bg3`, `--pal-fg`, `--pal-fg-muted`, `--pal-gray`, `--pal-red`,
   `--pal-green`, `--pal-yellow`, `--pal-blue`, `--pal-purple`, `--pal-aqua`,
   `--pal-accent`, `--pal-accent-strong`, `--pal-on-accent`,
   `--pal-shadow-1`, `--pal-shadow-2`. Each a `light-dark()` pair.
   `--pal-bg0` is a flat colour (it feeds `color-mix()`).
3. Template tokens, `--<name>-*`, in a second `:root, .themed` block or in
   the palette block's company — gradients, textures, glows, ornament
   colours. These may hold literals.

Never a bare `:root { --pal-… }`: pasted into a retoken site it would tie
with retoken's default palette and win by source order. Never `@font-face`
in `theme.css` (its `url()`s would break in the paste-in; if fonts are ever
self-hosted the rules go at the top of `global.css`).

Contrast, both halves, checked by the script: `--pal-fg` on `--pal-bg0`,
`--pal-accent` on `--pal-bg0`, `--pal-on-accent` on `--pal-accent` — all
≥ 4.5:1. Other pairs are reported.

The **retoken deliverable** is the palette block exactly as written: the
README prints it in a ```css fence and `docs/theme.html` prints it as
`<code data-snippet="palette">`; the checker compares both to the file.

### `css/global.css`

Tokens only — no colour literal, no `--pal-*` reference. Sections, each
opened by a marker comment the docs can name:

```
/* == reset == */  /* == base == */  /* == prose == */  /* == utilities == */
/* == buttons == */  /* == forms == */  /* == accordion == */  /* == cards == */
/* == fifty-fifty == */  /* == gallery == */  /* == switch == */
/* == page-break == */  /* == dialog == */  /* == banner == */  /* == badge == */
/* == table == */  /* == author-card == */  /* == navbar == */
/* == sidebar == */  /* == footer == */  /* == docs == */  /* == flare == */
/* == print == */
```

Honour `prefers-reduced-motion: reduce` for every animation.

Per-template exception (decision 20 of the plan): a design whose light half
keeps dark surfaces may set `scrollbar-color` and
`color-scheme: dark` on `select, input, textarea, dialog, [popover]`.

## 7. Light and dark

- Colours: `light-dark()` pairs in `theme.css`. `color-scheme: light dark`
  on `:root` lets the OS decide; `theme.js` pins `html.style.colorScheme`
  from the stored choice.
- Everything that is not a colour (`background-image`, `mask-image`,
  `content`, preview images): key off `:root[data-scheme='dark']`, which
  `theme.js` keeps equal to the *effective* scheme. Prefer a colour-driven
  form where one exists (a texture veiled by a
  `light-dark(var(--pal-bg0), transparent)` gradient; an ornament as a
  `mask-image` with a `light-dark()` fill) because it survives the paste-in.
- The toggle: `<button class="scheme-toggle" type="button">`, cycling
  auto → light → dark → auto; `data-scheme` and `aria-label` show the state;
  `'light'`/`'dark'` are written to `localStorage['retoken-scheme']`, auto
  removes the key. Exactly retoken's model, so a template page and a retoken
  site on the same origin agree.

## 8. JavaScript

| Allowed | Budget | Why not HTML or CSS |
| --- | --- | --- |
| `js/theme.js` | ≤ 50 lines | persisting a choice needs storage; applying it before paint needs script; all storage access in `try/catch` |
| `js/copy.js` (docs only) | ≤ 25 lines | clipboard |
| `onclick="document.getElementById('…').showModal()"` on dialog and lightbox openers | one statement | modal mode has no declarative opener at our browser floor (`commandfor` is Baseline 2025) |
| `landing/landing.js` (the landing, not a template) | ≤ 60 lines | search |

No other script, no inline `<script>` content, no other handler attribute.
Popovers, `<details name>`, `:target`, `:has()` and `<form method="dialog">`
do the rest. A user under a strict Content-Security-Policy moves the
one-liners into `theme.js`; the README says so.

## 9. Fixtures and snippets

- `blogpost.html` embeds `fixtures/markdown-test.html`'s
  `<article data-fixture="markdown-test">` verbatim; `forms.html` embeds
  `fixtures/forms.html`'s `<form data-fixture="forms">` verbatim. The
  fixture's images are `assets/fixture-photo-1.svg` and `-2.svg`, so every
  template ships files by those names. Every template also ships
  `assets/avatar.svg` for the author card.
- Docs examples and snippets pair by `data-snippet` key (§4.3). Comparison
  ignores whitespace between elements and attribute order; nothing else.

## 10. Browser floor

Baseline 2024 newly available: `light-dark()` for colours, `:has()`, the
Popover API, `<details name>`, `color-mix()`, `::backdrop`. No polyfills.
Every README states it.

## 11. The landing card

Every template has one card in the repo's `index.html`, inside
`<section class="cards">`, and one row in `templates/README.md`. The card,
verbatim except for the values:

```html
<article class="template-card" data-template="<name>" data-title="<Title>" data-tags="<tags>">
  <a class="preview" href="templates/<name>/index.html" aria-label="<Title>: overview">
    <img class="preview-light" src="landing/previews/<name>-light.svg" alt="" width="400" height="250">
    <img class="preview-dark" src="landing/previews/<name>-dark.svg" alt="" width="400" height="250">
  </a>
  <div class="template-body">
    <h2><a href="templates/<name>/index.html"><Title></a></h2>
    <p>One or two sentences.</p>
    <p class="tags"><span>…</span></p>
    <p class="links"><a href="templates/<name>/index.html">Overview</a><a href="templates/<name>/docs/index.html">Docs</a><a href="templates/<name>/example/index.html">Example site</a></p>
  </div>
</article>
```

The previews are hand-drawn SVG wireframes of the overview page, 400 × 250,
one per scheme, in the template's own colours; the landing swaps them on
`html[data-scheme]`. `data-tags` drives the filter chips and `data-title` the
search; the visible `.tags` spans repeat the tags for people.

Tags, one or more from each group: **scheme** `light-first | dark-first |
balanced` · **type** `serif | sans | display | mono` · **motion**
`animated | still` · **fonts** `google-fonts | system-fonts` · **feel**
`minimal | ornate | playful | editorial`.

## 12. Checks

`python tools/check.py --template <name>` runs everything above that a
script can see; `python tools/check.py` adds the landing, the fixture pages
and the bookkeeping. `docs/dev/testing.md` lists each check and the visual
pass that complements them.
