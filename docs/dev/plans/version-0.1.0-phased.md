# retemplate — Version 0.1.0 plan (phased)

What 0.1.0 builds, split into phases with checkpoints where the full check
suite must pass before proceeding. The feature list is [TODO](TODO); this file
is the reviewed version of it — the same asks with the folder layout chosen,
the technology settled, the parts that need a decision named, and the order it
can be built in. Where the two disagree, this file is the later thought.

Written 2026-09-03 against an empty scaffold (`VERSION` 0.1.0, a CHANGELOG
skeleton, MIT `LICENSE`, empty `README.md`). Revised 2026-09-04 after an
eight-lens review of the first draft and the owner's two corrections: **no
npm, no JavaScript test suite** — this is plain files, and the only tooling is
a zero-dependency Python script for structural checks.

**What this project is.** A set of complete, re-usable HTML + CSS templates and
themes that someone can take a folder of and use in their own project, with no
framework and no build step. Every template is also a
[retoken](https://kieranwood.ca/retoken/theme/) theme, so its palette drops
straight into a retoken site. The repo doubles as the showcase: a landing
page, and per-template demo, docs and example pages.

## Progress

Updated when a phase starts, when a template finishes, and at every
checkpoint. This table, not the TODO, is where a takeover agent reads the
state of the build; the TODO records which *asks* have landed.

| Phase | Status | Date | Note |
| --- | --- | --- | --- |
| 0 — Scaffold | done | 2026-09-04 | checker, fixtures, contract + testing docs, CI, launch config; owner confirmed layout with the no-npm correction |
| 1 — plain | done | 2026-09-04 | 29 pages, checker green |
| 2 — Landing | done | 2026-09-04 | search + filters, previews, plain card |
| A — Checkpoint | passed | 2026-09-04 | unfiltered checker 0/0; programmatic pass at 1280 and 375 in both schemes (overflow, images, lightbox, dialog, accordion, popovers, toggle, console) clean; screenshots partial — owner eyeball requested in the TODO |
| 3 — Neumorphic | not started | | |
| 4 — Brutal News | not started | | |
| 5 — Glassy | not started | | |
| B — Checkpoint | not started | | |
| 6 — Neon | not started | | |
| 7 — Natural | not started | | |
| C — Checkpoint | not started | | |
| 8 — Detailed | not started | | |
| 9 — Gothic | not started | | |
| 10 — Allegory | not started | | |
| D — Checkpoint | not started | | |
| 11 — Release | not started | | |

---

## Standing checklist — applies to EVERY phase

1. **Progress:** update the table above when a phase starts, when each
   template (or subagent) finishes, and at every checkpoint.
2. **TODO:** tick `docs/dev/plans/TODO` as each item lands — never batched.
   When a batch of templates is dispatched, annotate each template's line
   *in progress*; tick it the moment that template is done, not at the
   checkpoint.
3. **CHANGELOG.md:** entries under `# 0.1.0 Unreleased` in **Features** /
   **Bug Fixes** / **Other**. Brief — 2–4 sentences per change; more needs the
   owner's approval.
4. **Checks:** ordinary phases run `python tools/check.py --template <name>`
   (or the unfiltered run when working outside a template). Checkpoints run
   the unfiltered `python tools/check.py` **and** the visual pass described
   under *Checkpoints*.
5. **No build step, no framework, no npm.** Every page opens from disk and from
   any sub-path. Links and asset paths are *relative* and point at files, never
   directories (`docs/index.html`, not `docs/`), because the same folder must
   work at `file://`, at `kieranwood.ca/retemplate/templates/neon/`, and dropped
   into someone's `public/`.
6. **JavaScript only from the allow-list** in the contract. Anything new needs
   a sentence in the phase notes saying why CSS or native HTML could not do it.
7. **Semantic HTML.** `<details>` for accordions, `<dialog>` for modals and the
   lightbox, `<main>`, `<article>`, `<nav>`, `<aside>`, `<footer>`, `<figure>`.
   A `<div>` is a last resort for a purely presentational wrapper.
8. **Retoken compatible** as the contract defines it, enforced by the checker.
9. **Both schemes, every page.** A page that only looks right in one scheme is
   not done.

## Decisions taken up front

Settled; the phases assume them. Each records why.

1. **One folder per template, fully self-contained.** `templates/<name>/`
   references nothing outside itself except one whitelisted "All templates"
   link (decision 18). Copying the folder is the whole install.
2. **Two sets inside every template folder.** The **install set** — `css/`,
   `js/theme.js`, `fonts/` (if any), `assets/`, `README.md` — is what a user
   keeps; nothing in it references anything outside it. The **showcase set** —
   `index.html`, `blogpost.html`, `forms.html`, `sidebar.html`, `docs/`,
   `example/`, `js/copy.js` — is what sells the template and can be deleted.
   The README says so in its first paragraph; the checker enforces the
   isolation of the install set.
3. **A shared markup contract across all templates.** Same element structure,
   same class names for every required component; only CSS differs. Switching
   templates is a swap of `css/`, `fonts/` and `assets/`. Template flare is
   namespaced (`.neon-*`, `.glassy-*`) and, when it needs markup, sits inside a
   single `<div class="<name>-flare">` wrapper so a swap can strip it
   mechanically. The checker compares every template's page skeletons to
   `plain`'s (tags, non-flare classes, key attributes) so drift is caught the
   day it happens, not at release.
4. **`plain` is the eighth template and the reference implementation.** The
   contract as code, in a quiet style; the seven styled templates are built by
   copying it and re-skinning. The landing shows it as "Plain — the starting
   point".
5. **Two stylesheets per template:** `css/theme.css` (tokens) and
   `css/global.css` (base elements, utilities, components, layouts, flare),
   mirroring retoken's split and names. `global.css` is organised in marked
   sections (`/* == cards == */`) that the component docs name, so a reader
   can find a component's rules without a per-component file.
6. **What "retoken compatible" means, exactly.**
   - The **palette block** uses retoken's named-palette form verbatim:
     `:root[data-theme='<name>'], [data-theme='<name>'] { … }` with the 19
     `--pal-*` slots, each a `light-dark()` pair. Never a bare `:root`: a bare
     `:root` pasted into a retoken site ties with retoken's default `ember`
     block on specificity and wins by source order, hijacking the site.
   - Consequently **every template page sets `<html data-theme="<name>">`**
     (the folder name). The checker asserts it.
   - `theme.css` also carries the `:root, .themed` block with retoken's
     **colour mapping copied verbatim** (`color-scheme: light dark`,
     `--color-*`, `--bg-color`, `--surface-*`, `--border-color`, `--text-*`,
     `--editor-*`, `--syntax-*`, `--shadow-1/2`) and the **23 shared tokens
     retoken's editor lists** (`SHARED_VARS` in retoken's `theme.ts`:
     `--font-body`, `--font-mono`, `--font-size-sm/base/lg/xl/2xl`,
     `--line-height`, `--space-1..6`, `--radius-sm/md/lg/full`,
     `--page-max-width`, `--sidebar-width`, `--panel-width`, `--toc-width`,
     `--navbar-height`) with **values owned by the template**.
   - Retemplate adds three shared tokens of its own, non-namespaced because
     every template needs them: `--font-display` (default `var(--font-body)`),
     `--font-weight-display`, `--font-size-3xl`, plus `--font-size-hero` (a
     `clamp()`). Retoken's editor ignores them harmlessly.
   - Template-only tokens are namespaced `--<name>-*` and live in `theme.css`.
   - `global.css` names no colour literal and no `--pal-*` slot; only tokens.
   - The **retoken deliverable is exactly the palette block**, printed in the
     template README and on `docs/theme.html` followed by the one adoption
     line (`<html data-theme="neon">`). Fonts, radii, spacing and flare tokens
     are not carried; the README says so. The checker compares the printed
     block to `theme.css`.
   - Ships retoken's utility classes: `.btn` (+ `-primary`, `-danger`, `-sm`),
     `.card`, `.banner` (+ `-success`, `-warning`, `-danger`), `.badge`
     (+ `-done`, `-active`), `.data-table`, `.prose`, `.check`, `.page-header`,
     `.stack`, `.row`, `.grid-2`, `.muted`, `.small`, `.visually-hidden`.
     Retemplate additions: `.banner-info`, `.btn-lg`, `.grid-3`, `.container`.
   - Uses the `retoken-scheme` localStorage key with retoken's exact
     semantics: `'light'` | `'dark'` | absent (follow the OS).
7. **Light/dark is `color-scheme` + `light-dark()` for colours, and a
   `data-scheme` hook for everything else.** `theme.js` pins
   `html.style.colorScheme` from the stored key and mirrors the *effective*
   scheme to `<html data-scheme="light|dark">` (stored pin, else
   `matchMedia`, with a change listener). Colours use `light-dark()` pairs.
   Anything that is not a colour — `background-image`, `mask-image`,
   `content`, the landing's preview images — keys off
   `:root[data-scheme='dark']`, because `light-dark()` only takes colours in
   the browsers we target. Where a swap *can* be expressed as colour (a
   texture veiled by `light-dark(var(--pal-bg0), transparent)`, an ornament as
   a `mask-image` with a `light-dark()` fill) that form is preferred, since it
   also survives the retoken paste-in.
8. **The scheme control is tri-state**, matching retoken: a
   `<button class="scheme-toggle" type="button">` cycling auto → light → dark
   → auto, exposing the state as `data-scheme` and `aria-label`, writing
   `'light'`/`'dark'` to `retoken-scheme` and *removing* the key for auto.
   The `.switch` component is a form control, not the scheme toggle.
9. **Browser floor: Baseline 2024 newly available, no polyfills.**
   `light-dark()` (colours), `:has()`, the Popover API, `<details name>`,
   `color-mix()`, `::backdrop`. Recorded in every template README.
10. **The JS allow-list.** `js/theme.js` (≤ 50 lines: boot, tri-state toggle,
    `data-scheme` mirror, all storage access in `try/catch` so `file://` and
    private mode degrade to OS-follow); `js/copy.js` (docs only, ≤ 25 lines,
    clipboard); `landing/landing.js` (≤ 60 lines, search and filters); and
    one inline `onclick="…showModal()"` statement on dialog and lightbox
    openers (the declarative `commandfor` opener is Baseline 2025, outside
    our floor; a strict-CSP user moves the one-liners into `theme.js`, the
    README says how). Everything else is HTML or CSS:
    - Lightbox: one `<dialog class="lightbox">` per gallery holding every
      figure; thumbnails are `<a href="#lb-3" onclick="…showModal()">`,
      figures show via `:target`, prev/next are plain `<a href="#lb-2">`
      anchors, close is `<form method="dialog">`. Modal mode gives ESC, focus
      trapping and the backdrop. (Popovers were rejected: a popover opened
      from inside an open popover *nests* rather than replaces, so prev/next
      stacked the images.)
    - Exclusive accordions: `<details name="…">`.
    - Mobile navbar menu and the narrow-screen sidebar drawer: the `<nav>` /
      `<aside>` carries `popover`, opened by a real
      `<button popovertarget>` — ESC and light-dismiss come free and
      `::backdrop` is the scrim; above the breakpoint a media query makes
      them static. No desktop collapse in 0.1.0 (a known gap).
    - Switch: `<input type="checkbox" role="switch">`.
    - Every animation, tilt, glow and sheen: CSS. Nothing follows the cursor.
11. **Fonts come from Google Fonts by `<link>`, with real fallback stacks.**
    Without npm there is no vendoring pipeline, and downloading font files
    by script is a step the owner should approve explicitly. So: each
    template that needs a face adds one `<link rel="stylesheet">` (plus
    `preconnect`) to its showcase pages, `theme.css` names the family with a
    system fallback, and the README shows how to self-host instead. `plain`
    uses system stacks only. Open question 4 offers the self-hosting script.
12. **Images are local SVG, no external requests** (the fonts link is the one
    exception). Placeholder art per template in `assets/`, tiny, licence-free.
13. **Shared demo content is a fixture, hand-authored, copied verbatim,
    checked for parity.** `fixtures/markdown-test.html` is a complete page in
    browser-default styling (the TODO's test page); its
    `<article data-fixture="markdown-test">` is the fragment every
    `blogpost.html` embeds. `fixtures/markdown-test.md` is the same document
    as markdown, kept for humans. `fixtures/forms.html` likewise carries
    `<form data-fixture="forms">`. The checker compares the embedded subtree
    to the fixture, normalised.
14. **Docs snippets are checked against the live example.** Every docs
    example is `<figure class="example" data-snippet="<key>">…</figure>`
    paired with `<pre><code data-snippet="<key>">`; the checker parses both,
    normalises whitespace and attribute order, and compares. Variants use
    distinct keys and distinct ids.
15. **Previews are hand-drawn SVG, two per template**, at
    `landing/previews/<name>-light.svg` and `<name>-dark.svg`: an abstract
    page wireframe in the template's own colours and type. The landing swaps
    them on `data-scheme`. Small, deterministic, no tooling.
16. **Checkpoints are the checker plus eyes.** No browser automation. A
    checkpoint runs `python tools/check.py` unfiltered and then a **visual
    pass** in the in-app browser: for every template, `index.html`,
    `blogpost.html`, `forms.html`, `sidebar.html`, `docs/index.html`,
    `docs/components/cards.html`, `docs/theme.html` and `example/index.html`,
    each in both schemes, at a desktop and a phone width; noting anything for
    the TODO's **For human** list. Recorded in the Progress table.
17. **Template phases may run as parallel subagents, or sequentially.** The
    checker is per-template filterable and needs no server, so nothing
    collides. Subagents edit only their own folder and **return** five texts
    for the orchestrator to merge: the landing card, the `templates/README.md`
    row, the CHANGELOG entry, the TODO boxes earned, and *contract gaps*
    (anything `plain` or the contract must change — a subagent never works
    around a gap inside its own copy). Accepted gaps are applied to `plain`
    and to every already-built template at the next checkpoint, before the
    next batch starts.
18. **One whitelisted outside link.** Showcase pages carry exactly one
    `<a class="site-link" href="…/index.html">All templates</a>` (depth
    adjusted) in the navbar and sidebar footer. The checker allows only that
    selector to leave the folder; the get-started page lists it as the line
    to delete. Nothing in the install set references it.
19. **Contrast is a hard check for the pairs that carry text.** In both
    halves: `--pal-fg` on `--pal-bg0` ≥ 4.5:1, `--pal-accent` on `--pal-bg0`
    ≥ 4.5:1 (it is the link and focus colour), `--pal-on-accent` on
    `--pal-accent` ≥ 4.5:1. The checker computes them from `theme.css`. Other
    pairs are reported, not gated, so taste has the last word on ornament.
20. **Per-template UA-chrome override is permitted** where a design keeps dark
    surfaces in its light half (Neon): `scrollbar-color` on `:root` and
    `color-scheme: dark` on `select, input, textarea, dialog, [popover]` so
    native controls do not paint white on dark.

## Folder structure

Confirmed by the owner on 2026-09-04 (with the no-npm correction).

```
retemplate/
├── index.html                      Landing: every template, filter chips + title search
├── landing/
│   ├── landing.css                 The landing's own quiet style (it is not a template)
│   ├── landing.js                  Search/filter (JS allow-list)
│   ├── theme.js                    Copy of plain's theme.js (the landing has no template)
│   └── previews/<name>-{light,dark}.svg   Hand-drawn wireframe previews
├── fixtures/
│   ├── markdown-test.md            The markdown torture document (source, for humans)
│   ├── markdown-test.html          Same, hand-rendered; browser-default styling; the TODO's test page
│   ├── forms.html                  The canonical form, every control
│   └── README.md                   What is canonical, how parity is checked
├── templates/
│   ├── README.md                   One row per template + link to the contract
│   ├── plain/                      Reference implementation
│   ├── neumorphic/ brutal-news/ glassy/ neon/ natural/ detailed/ gothic/ allegory/
│   └── <name>/
│       ├── README.md               Install set vs showcase set, browsers, fonts, retoken paste-in
│       ├── index.html              Overview: prose that ties the components together
│       ├── blogpost.html           Fixture article inside the post shell (author card, meta, tags)
│       ├── forms.html              Fixture form inside a full page
│       ├── sidebar.html            Sidebar-layout variant of the overview
│       ├── css/theme.css           Tokens (the retoken half)
│       ├── css/global.css          Base, utilities, components, layouts, flare — marked sections
│       ├── js/theme.js             Boot + tri-state toggle + data-scheme mirror
│       ├── js/copy.js              Docs only
│       ├── fonts/                  Only if self-hosted (open question 4); else absent
│       ├── assets/                 favicon.svg + local SVG art
│       ├── docs/                   Sidebar layout throughout
│       │   ├── index.html          Get started: the head block, the install set, the deletable set
│       │   ├── theme.html          Tokens: swatches in both schemes, shared tokens, palette block to copy
│       │   ├── defaults.html       Bare native elements: headings, text, lists, tables, code, media, controls
│       │   ├── blog.html           Anatomy of the post shell (labelled skeleton + snippet)
│       │   └── components/
│       │       ├── index.html      Library index (grid of every component)
│       │       ├── accordion.html  cards.html  fifty-fifty.html  gallery.html  switch.html
│       │       ├── page-break.html buttons.html forms.html dialog.html navbar.html
│       │       ├── sidebar.html    banner.html  badge.html  table.html  author-card.html
│       │       ├── footer.html     flare.html
│       └── example/
│           ├── index.html          A three-page "real" site in this template
│           ├── <page-2>.html       Exactly two more pages, names per template
│           └── <page-3>.html
├── tools/
│   └── check.py                    Zero-dependency structural checker (stdlib only)
├── docs/
│   ├── README.md                   Documentation index
│   ├── dev/plans/                  TODO, this file
│   ├── dev/template-contract.md    The contract in prose (files, markup, tokens, JS, nav, checks)
│   ├── dev/testing.md              What check.py checks, how to run it, what the visual pass covers
│   ├── dev/adding-a-template.md    Copy plain, re-skin, register, run the checks
│   ├── user/using-a-template.md    Take the folder, keep the install set, delete the rest
│   └── user/retoken.md             Paste the palette block into a retoken site
├── .github/workflows/pages.yml     python tools/check.py, then deploy the repo root to Pages
├── .claude/launch.json             python -m http.server for the in-app browser
├── .gitignore
├── CHANGELOG.md · VERSION · LICENSE · README.md
```

Deviations from the TODO's literal text, all deliberate:
- `templates/` for the TODO's `tempaltes/`.
- `docs/components/` (plural) for the TODO's `docs/component/`.
- `plain` added as an eighth template (decision 4).
- `docs/theme.html` added (retoken's `/theme` page is the model the TODO cites).
- Allegory: the TODO reads *white on gold* / *black on red*. Taken literally
  for body text that fails contrast (white on `#c8a44a` is 2.4:1). The brief
  keeps the literal pairing for display type on hero bands, navbar and footer
  strips and the feature card, and uses gold-on-ivory / red-on-black for body
  surfaces. Open question 11.
- No test suite, no npm: the owner's correction of 2026-09-04.

## The template contract

Prose form: `docs/dev/template-contract.md` (Phase 0). Enforced by
`tools/check.py`. Reference implementation: `templates/plain`.

### Head block (every page, verbatim modulo the relative prefix)

```html
<!doctype html>
<html lang="en" data-theme="<name>">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>…</title>
  <link rel="icon" href="…/assets/favicon.svg">
  <script src="…/js/theme.js"></script>          <!-- sync, before the CSS: no flash -->
  <link rel="stylesheet" href="…/css/theme.css">
  <link rel="stylesheet" href="…/css/global.css">
  <!-- optional: the template's Google Fonts <link>, after preconnect -->
</head>
```

### Pages and roles

| Page | Layout | Role |
| --- | --- | --- |
| `index.html` | navbar | Overview in the template's voice; uses every component at least once; links to every other page |
| `blogpost.html` | navbar | The full live post: shell + the fixture article, verbatim |
| `forms.html` | navbar | The fixture form inside a full page, with the template's form styling |
| `sidebar.html` | sidebar | The overview content again, in the sidebar layout |
| `docs/index.html` | sidebar | Get started: head block, install set, deletable set, browsers, fonts, the `site-link` line to delete |
| `docs/theme.html` | sidebar | Tokens: 19 swatches rendered twice (a `.themed` subtree pinned light and one pinned dark), semantic + shared token tables, template tokens, the palette block as a copy snippet, the retoken adoption line |
| `docs/defaults.html` | sidebar | Bare native elements, no component classes |
| `docs/blog.html` | sidebar | Anatomy: labelled post-shell skeleton and its snippet; links to `blogpost.html` |
| `docs/components/index.html` | sidebar | Grid of every component with a one-line description |
| `docs/components/<c>.html` | sidebar | Preview → Markup (copy) → Variants (each a preview + snippet pair) → Classes (table, naming the `global.css` section) → Notes (behaviour, keyboard, JS if any); prev/next links |
| `example/*.html` | navbar | `index.html` + exactly two more; must use the navbar, a hero or fifty-fifty, a card grid, a `.field` form, a dialog or accordion, and the footer; links back to the overview |

### Navigation

Navbar: brand → overview, links to Blog post, Forms, Sidebar, Docs, Example,
then the scheme toggle and the `site-link`. Mobile: the `<nav>` is a popover
opened by a `<button popovertarget>`.

Sidebar (docs and `sidebar.html`): `<nav>` of `<details>` groups — **Pages**
(Overview, Blog post, Forms, Sidebar variant), **Docs** (Get started, Theme,
Defaults, Blog anatomy), **Components** (all 17 in the table order below),
**Example** — with `aria-current="page"` on the current link and the
`site-link` in the sidebar footer. Component pages end with prev/next links.
The checker asserts every sidebar page carries the same link set.

### Components (one docs page each, in this order)

| Component | Markup | Notes |
| --- | --- | --- |
| Accordion | `<details class="accordion"><summary>` | `.accordion-group` wraps several sharing a `name` for exclusive open |
| Cards | `<article class="card">` with `.card-media`, `.card-body`, `.card-title`, `.card-text` | `.card-horizontal` (media left), `.card-horizontal.card-media-end` (media right), `.card-feature` = the template's dynamic card |
| Fifty-fifty | `<section class="fifty-fifty"><figure>…</figure><div>…</div>` | `.fifty-fifty-reverse` = image right; stacks image-first on narrow screens |
| Gallery + lightbox | `<ul class="gallery">` of `<li><figure><a href="#lb-N" onclick="…showModal()">` + one `<dialog class="lightbox">` of `<figure id="lb-N">` slides | `:target` picks the slide; prev/next anchors; `<form method="dialog">` closes |
| Switch | `<label class="switch"><input type="checkbox" role="switch"><span>` | A form control |
| Page break | `<hr>` and `<hr class="page-break">` | The ornament is per-template |
| Buttons | `.btn`, `-primary`, `-danger`, `-sm`, `-lg`, `:disabled`; every non-submit button has `type="button"` | |
| Forms | native controls + `.field` (label, control, `.hint`, `.error`), `.form-grid`, `fieldset` | This page shows the `.field` patterns and states; the fixture form lives in `forms.html` |
| Dialog | `<dialog class="modal">` with `<form method="dialog">` | Opener carries the allowed one-liner |
| Navbar | `<header class="navbar">` | Page-level: the docs page embeds `../../index.html` in an `<iframe>` and shows the snippet with `data-source` |
| Sidebar | `<div class="sidebar-layout">` + `<aside class="sidebar" popover>` + `<main>` | Page-level, same treatment (`../../sidebar.html`) |
| Banner | `.banner` + `-success`, `-warning`, `-danger`, `-info` | |
| Badge | `.badge` + `-done`, `-active` | |
| Table | `.table-wrap > table.data-table` | |
| Author card | `<aside class="author-card">` with avatar, name, bio, `.meta`, `.tags > .tag` | The component only; the shell is on `docs/blog.html` |
| Footer | `<footer class="footer">` columns | Page-level (iframe of `../../index.html`) |
| Flare | `.<name>-*` inside `<div class="<name>-flare">` when it needs markup | Documented on `flare.html`; `plain` has the page with none |

Typography, images, blockquotes, code, lists and tables inside `.prose` are on
`defaults.html`.

### Tokens

As decision 6. `theme.css` order: `@font-face` never (fonts are linked);
`:root, .themed` block (colour mapping verbatim, shared tokens with template
values, retemplate's four extra shared tokens); the palette block
`:root[data-theme='<name>'], [data-theme='<name>']` with the 19 slots; then
`--<name>-*` tokens. `--pal-bg0` is always a flat colour (it feeds
`color-mix()`); gradients and textures are `--<name>-*` `background-image`
tokens layered on `body`.

### The checker — `python tools/check.py [--template <name>]`

Python 3 standard library only (`html.parser`, `re`, `pathlib`, `json`,
`argparse`, `colorsys`-free contrast maths). Exits non-zero on any error;
prints `path:line: message`. Checks, per template unless noted:

1. **structure** — every contract file exists; `example/` has `index.html` +
   exactly two more `.html`; no stray files in the install set.
2. **head** — the head block on every page: charset, viewport, color-scheme
   meta, `data-theme` equal to the folder name, favicon, `theme.js` as a sync
   script before both stylesheets.
3. **links** — every `href`/`src`/`srcset`/CSS `url()` is relative, resolves
   to a file, is not a directory, and does not leave the folder (except
   `.site-link`); install-set files never reference the showcase set;
   external URLs only on the fonts `<link>` and `preconnect`.
4. **tokens** — `theme.css`: the colour-mapping declarations present under
   `:root, .themed`; all 23 shared tokens + the 4 retemplate tokens present;
   the palette block uses the named form with the folder name and exactly
   the 19 slots, each starting `light-dark(`; contrast rules of decision 19.
   `global.css`: no colour literal (hex, `rgb()`/`hsl()`/`oklch()`/`color()`
   functions, and the named colours except `transparent`/`currentColor`),
   no `--pal-*` reference; checked in declaration values only, ignoring
   comments and `url()` contents.
5. **fixtures** — the `[data-fixture]` subtrees in `blogpost.html` and
   `forms.html` equal the fixtures, normalised (whitespace collapsed,
   attributes sorted).
6. **snippets** — every `data-snippet` pair matches; the palette snippet on
   `docs/theme.html` and in the README equals the palette block.
7. **nav** — every sidebar page carries the canonical link set; every navbar
   page carries the navbar link set; `aria-current` on the page's own link.
8. **js** — only the allow-listed script files; inline scripts none;
   inline handlers only `onclick` containing `showModal()`.
9. **contract** — page skeletons (tag, class names minus `.<name>-*`, `name`,
   `role`, `popover`, `popovertarget`, `data-*` attributes) match `plain`'s
   for every contract page, modulo `.<name>-flare` subtrees.
10. **landing** (unfiltered runs only) — a card per template folder, tags
    from the vocabulary, previews present, `templates/README.md` has a row
    per folder.

Landing tag vocabulary: scheme `light-first | dark-first | balanced`; type
`serif | sans | display | mono`; motion `animated | still`; fonts
`google-fonts | system-fonts`; feel `minimal | ornate | playful | editorial`.

## Open questions

Each has a default so a single "go with the defaults" is a complete answer.
Questions 1–3, 5–9 and 12 from the first draft were accepted by the owner's
"begin" (their defaults now appear as decisions above).

| # | Question | Needed by | Default if unanswered |
| --- | --- | --- | --- |
| 4 | Fonts: Google Fonts `<link>` (decision 11) — or approve `tools/vendor_fonts.py` (stdlib `urllib`) that downloads OFL woff2 files into `fonts/` so templates work offline? | Phase 3 | Google Fonts link. |
| 10 | Rename the CHANGELOG's `Developer / Internal` heading to `Other` (the TODO's rule)? | Phase 0 | Rename. |
| 11 | Allegory: the hybrid reading above (literal white-on-gold / black-on-red only for large display type on bands) — or the literal reading for body surfaces, accepting sub-AA body text? | Phase 10 | Hybrid. |
| 13 | Example-site themes per template (in the briefs) — any you want different? | Phases 3–10 | As briefed. |
| 14 | Brutal News: the TODO says thick borders and harsh colours; the reference is 2px rules and one red. The brief goes with the TODO (≥ 3px rules, a harsh hue set). Confirm? | Phase 4 | The TODO's words. |
| 15 | Desktop sidebar collapse is out for 0.1.0 (mobile drawer only). OK? | Phase 1 | Out. |

## Phase overview

| Phase | Goal | Touches | Parallel? |
| --- | --- | --- | --- |
| 0 | Scaffold: checker, fixtures, contract doc, TODO rewrite, CI, launch | root, `tools/`, `fixtures/`, `docs/` | — |
| 1 | `templates/plain` — every page, component and doc | `templates/plain/` | — |
| 2 | Landing + previews | `index.html`, `landing/` | — |
| **A** | **Checkpoint: contract freeze** | | |
| 3 | Neumorphic | `templates/neumorphic/` | with 4, 5 |
| 4 | Brutal News | `templates/brutal-news/` | with 3, 5 |
| 5 | Glassy | `templates/glassy/` | with 3, 4 |
| **B** | **Checkpoint** | | |
| 6 | Neon | `templates/neon/` | with 7 |
| 7 | Natural | `templates/natural/` | with 6 |
| **C** | **Checkpoint** | | |
| 8 | Detailed (art deco) | `templates/detailed/` | with 9, 10 |
| 9 | Gothic | `templates/gothic/` | with 8, 10 |
| 10 | Allegory | `templates/allegory/` | with 8, 9 |
| **D** | **Checkpoint** | | |
| 11 | Cross-template review, docs, release | everything, read-mostly | — |

## Phase 0 — Scaffold

**Goal:** the checker exists and passes on an empty `templates/`, the
fixtures and the contract are written, and the TODO reflects the layout.

**Scope:**
1. `tools/check.py` as specified above; `python tools/check.py` with no
   templates exits 0 (and says so).
2. `fixtures/markdown-test.md` + `fixtures/markdown-test.html` (h1–h6,
   paragraphs, emphasis/strong/strikethrough, inline code, inline and
   reference links, images with alt and title, nested blockquotes with lists
   and code inside, ordered/unordered/nested/task lists, fenced code in two
   languages plus indented code, tables with alignment via
   `class="align-*"`, hard breaks, footnotes, a definition list, `<abbr>`,
   `<kbd>`, `<mark>`, `<sup>`/`<sub>`, `<details>`), `fixtures/forms.html`,
   `fixtures/README.md`.
3. `docs/dev/template-contract.md`, `docs/dev/testing.md`,
   `docs/dev/adding-a-template.md` (stub), `docs/user/*` (stubs),
   `docs/README.md` index, `templates/README.md`, root `README.md` first pass.
4. Rewrite the TODO's **Per Template** section to the confirmed layout with a
   pointer to the contract; add sub-boxes under *Scaffold* for the checker,
   fixtures, contract and landing; tick *Determine project layout*.
5. `.gitignore`, `.claude/launch.json` (`python -m http.server 8080`),
   `.github/workflows/pages.yml` (checkout → `python tools/check.py` →
   upload the repo root minus `tools/` and `.github/` → deploy).
6. CHANGELOG: heading rename (question 10) and an *Other* entry.

**Done when:** `python tools/check.py` exits 0; the docs above exist.

## Phase 1 — `templates/plain`

**Goal:** every contract page and component in a quiet style, passing the
checker, looking right in both schemes.

**Scope:**
1. `css/theme.css` per the token contract (retoken's `neutral` values seed
   the palette); `css/global.css` in marked sections: reset, base elements,
   `.prose`, utilities, then one section per component in table order, then
   navbar, sidebar layout, footer, print basics; `prefers-reduced-motion`
   honoured.
2. `js/theme.js`, `js/copy.js`.
3. The four top-level pages; `docs/` in full; `example/` — a small town
   library site (`index.html`, `events.html`, `membership.html`).
4. `assets/`: favicon, eight gallery SVGs, card art, avatar, fifty-fifty art.
5. `README.md` (install set, browsers, fonts: none, the palette block).

**Checks:** `python tools/check.py --template plain`; a visual pass of the
eight pages listed in decision 16 in both schemes and at a phone width.
**CHANGELOG:** *Features* — the plain template and the component library.

## Phase 2 — Landing & previews

**Scope:**
1. `index.html` + `landing/`: a card per template — preview (both SVGs,
   swapped on `data-scheme`), name, one line, tag chips from the vocabulary,
   links to overview / docs / example; filter chips (AND with the search),
   a title search, an empty-state message; links to
   `fixtures/markdown-test.html` and `docs/README.md`. Card data is the
   HTML itself.
2. `landing/previews/plain-{light,dark}.svg`.
3. The canonical card snippet goes into `docs/dev/template-contract.md`.

**Checks:** unfiltered `python tools/check.py`.
**CHANGELOG:** *Features* — landing page.

> ### CHECKPOINT A — contract freeze
> Unfiltered checker green; visual pass of `plain` and the landing in both
> schemes at desktop and phone widths; the TODO's Per Template section
> re-read against the frozen contract. After this, every contract change is
> applied to `plain` **and** to every built template at the next checkpoint
> (decision 17), so anything all seven need must land here.

## Phases 3–10 — one phase per template

Identical scope; only the brief differs.

1. Copy `templates/plain` → `templates/<name>` (except `README.md`, rewritten).
   Re-skin `theme.css` and `global.css`; keep the markup contract intact;
   add the fonts `<link>` to the showcase pages if the brief names faces.
2. Replace `assets/` art with pieces that suit the design.
3. Rewrite the **copy** of `index.html`, `sidebar.html`, `docs/index.html`,
   `docs/components/flare.html` and the three `example/` pages in the
   template's voice; `blogpost.html` and `forms.html` keep the fixture bodies
   verbatim (only the surrounding chrome changes).
4. `.card-feature` gets the template's effect; `hr.page-break` its ornament;
   `flare.html` documents the rest.
5. `README.md`; `landing/previews/<name>-{light,dark}.svg`.
6. `python tools/check.py --template <name>` green; a visual pass of the
   eight pages in both schemes.
7. Return (or, when working alone, apply) the five merge texts of decision 17.

**Done when:** the filtered checker is green; the visual pass is done; the
five texts are merged; the template's TODO box is ticked.

### Design briefs

Measured values come from the references (computed styles read on
2026-09-03); everything else is the direction to take. Every brief must keep
`--pal-bg0` flat and satisfy the contrast rules of decision 19.

- **Phase 3 — Neumorphic.** Soft-UI: elements extruded from one surface
  colour by paired light/dark box-shadows; inputs and the switch track are
  *inset*; buttons press flat on `:active`. Light: cool grey `#e0e5ec` base
  with white and blue-grey shadows; dark: charcoal `#2a2d34` with near-black
  and lighter-charcoal shadows. Text stays high-contrast; the accent is a
  muted blue (`#4a6fa5` light / `#8fb3ff` dark) for links, focus and primary
  actions. `--radius-md` 14px. Fonts: Nunito (display + body). Dynamic card:
  raises on hover, presses on click. Example: a smart-home dashboard (home,
  a room, settings).
- **Phase 4 — Brutal News.** The TODO's words over the reference's
  restraint (open question 14): rules never thinner than 3px
  (`--brutal-rule: 3px`; 6px on masthead, navbar and card outlines), zero
  radius, zero shadows, white paper and black ink, hot red `#e6331a` as
  `--pal-accent` with black `--pal-on-accent`, and a harsh hue set for the
  slots: acid yellow `#ffe600`, cobalt `#0033ff`, signal green `#00a651`,
  magenta purple, cyan aqua. Headlines huge with tight negative tracking
  (the reference: 152px at −7.6px); kickers small uppercase with +1.4px
  tracking; masthead with volume/date line; `column-count` body text on the
  overview; drop caps; ruled tables. Dark: black paper, white ink, same hues.
  Fonts: Archivo Black (display), Inter (body), JetBrains Mono. Dynamic card:
  hover inverts to black-on-red. Example: a newspaper (front page, article,
  subscribe).
- **Phase 5 — Glassy.** From canadiancoding.ca: `--glassy-backdrop` =
  `linear-gradient(310deg, #141727, #3a416f)` in dark and a sky/lavender pair
  in light, layered on a flat `--pal-bg0`; panels `rgb(255 255 255 / 0.8)`
  (light) or `rgb(20 23 39 / 0.55)` (dark) with
  `backdrop-filter: saturate(2) blur(30px)`, a 1px inset white border token
  and a soft drop shadow; radii 12–16px; pill buttons. Signature: four
  layered SVG waves in a `<div class="glassy-flare">` on the hero and footer,
  animated by a `move-forever` parallax keyframe (`<use>` of one path at
  offset delays), paused under `prefers-reduced-motion`. Fonts: system-ui.
  Dynamic card: a fixed perspective tilt on hover
  (`perspective(800px) rotateX(4deg)`) with brighter glass. Example: an
  agency (home, services, contact).
- **Phase 6 — Neon.** Dark half: zinc `#18181b` surfaces, rose accent
  `#f43f5e`, glow `0 30px 70px -25px rgb(244 63 94 / 0.5)`, 1px borders at
  10–15 % white, radii 16 / 24 / pill. Light half is *less dark, never
  white*: bg0 `#3a3a42` stepping lighter through bg1–bg3, off-white text,
  `--pal-accent-strong` a lighter rose `#fb7185` for links so both halves
  clear 4.5:1, `--pal-on-accent: #18181b`. A cyan second neon for
  `--pal-blue`/`--pal-aqua` so info and links glow differently from danger.
  Decision 20's UA-chrome override applies. Fonts: Space Grotesk (display),
  Inter (body). Dynamic card: a slow border-glow sweep on hover
  (`conic-gradient` mask). Example: a SaaS (home, pricing, changelog).
- **Phase 7 — Natural.** Light: cream `#ece7d6` paper, ink `#2e2519`, rust
  accent `#a33b2a`, moss `#3d4a30`, muted `#6b6450`, border `#c6c0a8`,
  uppercase tracked kickers, a faint radial moss tint in one corner. Dark:
  deep brown `#1c150f` bg0 with a soil texture (`--natural-soil`, an SVG
  `feTurbulence` data-URI) layered on `body` and veiled in light by a
  `light-dark(var(--pal-bg0), transparent)` gradient; light-green `#b9c9a0`
  and cream text; cream accent. Fonts: Fraunces (display), Source Sans 3
  (body). Dynamic card: a pressed-flower specimen card whose paper tag lifts
  on hover. Example: a plant nursery (home, a field-guide entry, visit).
- **Phase 8 — Detailed (art deco).** Brass and gold on deep navy/black;
  stepped and fanned geometry, sunburst radials, chevron borders, thin double
  rules. Light: cream `#f3ead8`, black ink, `--pal-accent` a bronze
  `#7a5a12` (bright gold `#b8902e` is the ornament token `--deco-gold`, for
  rules, sunbursts and large display type only); dark: `#0d1220` with gold
  `#d4af37` accent and brass. Ornament is CSS gradients and inline SVG inside
  `.detailed-flare` (sunburst headers, chevron `hr.page-break`, stepped card
  corners via `clip-path`). Fonts: Limelight (h1 and masthead), Josefin Sans
  (kickers, nav, small caps), Jost (body). Dynamic card: a gold-leaf sheen
  sweeping across on hover. Example: a grand hotel (home, restaurant,
  reservations).
- **Phase 9 — Gothic.** Stone greys and charcoal with crimson `#7a1f2b`
  and a cold violet; pointed-arch shapes (`clip-path` on media and card
  tops); tracery rules; blackletter for headings only. Light: pale stone
  `#e9e5dc` with iron ink; dark: near-black with candle-gold `#c9a24c`
  accents. Fonts: UnifrakturMaguntia (h1–h2 only), Crimson Pro (body).
  Dynamic card: a stained-glass colour wash on hover. Example: a cathedral
  archive (home, a chronicle entry, visiting).
- **Phase 10 — Allegory.** Two faces of one site (open question 11). Light,
  angelic: ivory surfaces, `--pal-accent` an antique gold dark enough for
  text (`#8a6d1f`), `--allegory-gold` `#c8a44a` for bands that carry white
  display type ≥ 24px bold, feather/halo SVG ornaments, radiant soft
  shadows. Dark, demonic: black surfaces, `--pal-accent` `#e0334f`,
  `--allegory-red` `#b3122e` for bands carrying black display type,
  horn/flame ornaments, hard shadows. Ornaments swap on
  `:root[data-scheme='dark']` (decision 7). Fonts: Cormorant Garamond
  (display), Inter (body). Dynamic card: flips between the two faces on
  hover regardless of scheme. Example: a two-sided storytelling site (home,
  "the ascent", "the descent").

> ### CHECKPOINTS B, C, D
> Unfiltered checker green; the visual pass for every new template; the
> five merge texts merged; accepted contract gaps applied to `plain` and to
> every built template before the next batch starts; Progress updated.

## Phase 11 — Cross-template review, docs, release

1. Unfiltered checker green for all eight; a read of every README.
2. Consistency pass on docs copy (component descriptions identical across
   templates except where a template genuinely differs).
3. `docs/user/using-a-template.md`, `docs/user/retoken.md`,
   `docs/dev/adding-a-template.md` finished; root `README.md` finished.
4. TODO re-verified and ticked; `CHANGELOG.md` tidied; release date when
   the owner says so.

## Ordering & parallelism

- Phase 0 blocks everything; Phase 1 blocks 2 and every template phase.
- Checkpoint A is the contract freeze; later changes propagate per decision 17.
- Batch order puts the three most different stresses first (shadows,
  borders, backdrop effects) so contract gaps surface at B, not D.
- Alone: 0 → 1 → 2 → A → 3, 4, 5 → B → 6, 7 → C → 8, 9, 10 → D → 11.

## Deliberately out of scope for 0.1.0

- A theme editor or picker inside the templates (retoken has one).
- Desktop sidebar collapse; RTL; i18n; print beyond sensible defaults.
- A component registry or CLI. Take the folder.
- Real photography. SVG art only.
- Polyfills for pre-2024 browsers.
- Per-template docs search. The landing's search covers discovery.
- Browser automation of any kind.
