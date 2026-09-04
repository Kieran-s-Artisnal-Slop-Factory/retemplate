# retemplate — Version 0.1.0 plan (phased)

What 0.1.0 builds, split into phases with checkpoints where the full test suite
must pass before proceeding. The feature list is [TODO](TODO); this file is the
reviewed version of it — the same asks with the folder layout chosen, the
technology settled, the parts that need a decision named, and the order it can
be built in. Where the two disagree, this file is the later thought.

Written 2026-09-03 against an empty scaffold: `VERSION` reads `0.1.0`,
`CHANGELOG.md` has the `0.1.0 Unreleased` skeleton, `LICENSE` is MIT, `README.md`
is empty, and `docs/` holds only this plan and a one-line index. Nothing has been
implemented.

**What this project is.** A set of complete, re-usable HTML + CSS templates and
themes that someone can take a folder of and use in their own project, with no
framework and no build step. Every template is also a
[retoken](https://kieranwood.ca/retoken/theme/) theme, so the palette drops
straight into a retoken site as well. The repo itself doubles as the showcase:
a landing page, and per-template demo, docs and example pages.

> **Status:** DRAFT. The folder structure and the open questions below are
> waiting on the owner's confirmation. No implementation phase has started.

---

## Standing checklist — applies to EVERY phase

Adapted from the TODO's *Per change* rules and the sibling repos' plans so a
phase can be worked from this file alone:

1. **TODO:** tick `docs/dev/plans/TODO` as each item lands — never batched at
   the end — so a usage-limit interruption leaves an honest trail. A subagent
   that finishes a template reports which boxes it earned; the orchestrator
   ticks them.
2. **CHANGELOG.md:** entries under `# 0.1.0 Unreleased` in **Features** /
   **Bug Fixes** / **Other**. Brief — 2–4 sentences per change. More than that
   needs the owner's approval first.
3. **Tests:** ordinary phases run the fast static checks (`npm run check`) plus
   the browser specs for the folders they touched
   (`npm test -- --grep <template>`). Only the checkpoints run everything:
   `npm run check`, `npm test`, and `npm run screenshots` (which must complete
   without a failed page).
4. **No build step, no framework.** Every page opens from disk and from any
   sub-path. All links and asset paths are *relative* — never root-absolute —
   because the same folder must work at `file://`, at
   `kieranwood.ca/retemplate/templates/neon/`, and dropped into someone's
   `public/`.
5. **JavaScript only from the allow-list** in the contract below. Anything new
   needs a sentence in the phase notes saying why CSS or native HTML could not
   do it.
6. **Semantic HTML.** `<details>` for accordions, `<dialog>` for modals,
   `<main>`, `<article>`, `<nav>`, `<aside>`, `<footer>`, `<figure>`. A `<div>`
   is a last resort for a purely presentational wrapper.
7. **Retoken compatible.** `theme.css` passes `tools/check-tokens.mjs`;
   `global.css` names no colour literal, only tokens.
8. **Both schemes, every page.** Light and dark are exercised by the specs; a
   page that only looks right in one scheme is not done.

## Decisions taken up front

Settled; the phases assume them. Each records why, because the reasons are the
part that ages.

1. **One folder per template, fully self-contained.** `templates/<name>/`
   carries its own CSS, JS, fonts and images and references nothing outside
   itself. The owner's brief is "take and use": copying one folder must be the
   whole install. The price is duplication (each template carries its own copy
   of the shared demo content); the parity checks in `tools/` keep the copies
   honest.
2. **A shared markup contract across all templates.** Every template uses the
   same element structure and the same class names (`.card`, `.fifty-fifty`,
   `.switch`, …) for the required components; only the CSS differs. Switching
   a site from Neon to Gothic is then a stylesheet swap, the specs are written
   once, and a template subagent builds against a fixed spec instead of
   inventing one. Template-specific *flare* is the deliberate exception and is
   namespaced (`.neon-glow`, `.glassy-waves`) so it reads as non-portable.
3. **`plain` is the eighth template and the reference implementation.** Not in
   the TODO's list. It is the contract written as code — every required page,
   component and doc — in an intentionally quiet style, and it is what a user
   starts from when none of the seven fits. The seven styled templates are
   built by copying `plain` and re-skinning it. Cheap to add (it is the
   skeleton the others need anyway) and it removes "which template is the
   canonical markup?" as a question forever.
4. **Two stylesheets per template, mirroring retoken:** `css/theme.css`
   (palette slots, semantic mapping, shared tokens — the retoken-droppable
   half) and `css/global.css` (base elements, utilities, components, flare).
   Same split, same names as retoken, so someone who knows one knows the
   other, and the theme half is a copy-paste into a retoken `theme.css`.
5. **Retoken compatibility means, concretely:** `theme.css` declares all 19
   `--pal-*` slots as `light-dark()` pairs under `:root, [data-theme='<name>']`
   (so it is the default when shipped alone *and* a discoverable named palette
   inside retoken), repeats retoken's semantic mapping under `:root, .themed`,
   declares every shared token retoken's editor lists (`--font-*`,
   `--space-1..6`, `--radius-*`, `--page-max-width`, `--sidebar-width`,
   `--panel-width`, `--toc-width`, `--navbar-height`, `--shadow-1/2`), ships
   retoken's utility classes (`.btn` + `-primary/-danger/-sm`, `.card`,
   `.banner` + variants, `.badge`, `.data-table`, `.prose`), and uses the
   `retoken-scheme` localStorage key so the scheme toggle and a retoken site
   agree. Template-only tokens are allowed, namespaced `--<name>-*`, and live
   in `theme.css` so `global.css` stays literal-free.
6. **Light/dark is `color-scheme` + `light-dark()`, pinned on `<html>`.** One
   declaration per colour covers both schemes; the toggle sets
   `html.style.colorScheme`; absent means follow the OS. Exactly retoken's
   mechanism. Neon's "light mode is only less dark" and Natural's dirt-texture
   dark are just what the two halves of each pair say.
7. **Browser baseline is Baseline 2024, no polyfills.** `light-dark()`,
   `:has()`, the Popover API, `<details name>` exclusive accordions, and
   `color-mix()` are all in every current engine. They are what let the JS
   budget be this small.
8. **The JS budget is an allow-list** (in the contract). Scheme boot + toggle,
   copy-to-clipboard on docs pages, a one-line `showModal()` on dialog
   openers, and the landing page's search/filter. Lightbox = Popover API;
   accordion groups = `<details name>`; sidebar toggle = a checkbox and
   `:has()`; switch = `<input type=checkbox role=switch>`; every animation =
   CSS. Nothing else.
9. **The scheme boot script is a classic synchronous `<script src>` in
   `<head>`,** not inline-per-page and not a module. Retoken inlines it
   because Astro owns the shell; here every page is hand-written, and a
   synchronous external script in `<head>` runs before first paint just the
   same (it is a *deferred* or *module* script that reintroduces the flash).
   One file, no duplication, no flash.
10. **Dev tooling is allowed; it is not a build step.** `package.json` holds
    devDependencies only (`@playwright/test`, `html-validate`,
    `node-html-parser`, `@axe-core/playwright`). Nothing in `templates/` needs
    them. A user who never runs `npm install` loses nothing.
11. **Shared demo content is a fixture, copied verbatim, checked for parity.**
    `fixtures/markdown-test.md` (the TEST.md-style torture document — it also
    satisfies the TODO's "page with an example of rendered markdown") and
    `fixtures/forms.html` are the canonical bodies; every template's
    `blogpost.html` and `forms.html` embed them. `tools/check-fixtures.mjs`
    compares the embedded article to the fixture so they cannot drift. This
    is how "no includes" and "no drift" coexist without a build.
12. **Docs snippets are checked against the live example.** Each component doc
    page shows the component and a `<pre><code>` of its markup with a copy
    button. A static check parses the page, unescapes the snippet, and
    compares it to the live example's markup, so the copy-paste can never lie.
13. **Images are local SVG, no external requests.** Placeholder art per
    template (patterns, illustrations, a texture or two) as inline or
    `assets/*.svg`. Offline demos, no licensing, no third-party fetch. Photos
    are not needed to show a layout.
14. **Fonts are self-hosted OFL `woff2` with a system fallback.** Vendored once
    from `@fontsource/*` packages (devDependencies) into
    `templates/<name>/fonts/` by `tools/vendor-fonts.mjs`, licence file
    alongside. Half the designs (art deco, gothic, brutalist newspaper) live or
    die on type, and "take and use" should not phone Google. The fallback
    stack keeps the page readable if a font is deleted.
15. **Previews are generated, not drawn.** `tools/screenshots.mjs` renders
    each template's `index.html` in both schemes to
    `templates/<name>/preview-light.png` / `preview-dark.png` for the landing
    page. Regenerated at every checkpoint; committed so the landing works
    without tooling.
16. **Checkpoints group templates into parallel batches.** Templates are
    disjoint folders, so subagents build them concurrently. The only shared
    files are `index.html` (landing), `CHANGELOG.md` and `TODO`; subagents
    return their landing card, changelog entries and earned TODO boxes as
    text and the orchestrator merges them. That makes the merge point
    explicit and un-trampleable.
17. **Accessibility: structural issues gate, colour contrast reports.**
    `html-validate` (labels, alt text, heading order, valid nesting) is a
    gate; axe runs in the specs and *reports* violations without failing, so
    Neon's glow text or Glassy's translucent panels can be judged by a human
    rather than blocked by a number. These are public templates, so the bar is
    higher than the sibling personal apps, but taste still has the last word.

## Folder structure

The thing to confirm. Everything under `templates/<name>/` is what a user takes.

```
retemplate/
├── index.html                      Landing page: every template, filter + title search
├── landing/
│   ├── landing.css                 The landing's own quiet style (it is not a template)
│   └── landing.js                  Search/filter + scheme toggle (JS allow-list item)
├── fixtures/                       Canonical shared demo content, copied into templates
│   ├── markdown-test.md            The markdown torture document (source)
│   ├── markdown-test.html          Rendered, browser-default styling — the TODO's test page
│   ├── forms.html                  The canonical form body (every input type)
│   └── README.md                   What is canonical, how parity is checked
├── templates/
│   ├── README.md                   Index of templates + link to the contract
│   ├── plain/                      Reference implementation of the contract (decision 3)
│   ├── neumorphic/
│   ├── brutal-news/
│   ├── glassy/
│   ├── neon/
│   ├── natural/
│   ├── detailed/                   Art deco
│   ├── gothic/
│   └── allegory/
│       ├── README.md               What it is, how to use it, fonts + licences, retoken notes
│       ├── index.html              Overview page: prose that ties the components together
│       ├── blogpost.html           Fixture article + author card, tags, date, reading time
│       ├── forms.html              Fixture form
│       ├── sidebar.html            Sidebar-layout variant of the overview
│       ├── css/
│       │   ├── theme.css           Retoken half: --pal-* slots, semantic map, shared tokens
│       │   └── global.css          Base elements, utilities, components, flare
│       ├── js/
│       │   ├── theme.js            Scheme boot (sync, in <head>) + toggle button wiring
│       │   └── copy.js             Docs only: copy-to-clipboard buttons
│       ├── fonts/                  Self-hosted woff2 + OFL.txt (may be empty for system stacks)
│       ├── assets/                 Local SVG art, icons, textures, favicon
│       ├── preview-light.png       Generated by tools/screenshots.mjs, used by the landing
│       ├── preview-dark.png
│       ├── docs/                   Sidebar layout throughout
│       │   ├── index.html          Get started: link the two stylesheets, the boot script, done
│       │   ├── defaults.html       Generic elements: headings, lists, tables, code, forms, media
│       │   ├── blog.html           The blog-post design, annotated
│       │   └── components/
│       │       ├── index.html      Library index (shadcn-style grid of every component)
│       │       ├── accordion.html  …one page per component; see the contract for the list
│       │       ├── cards.html
│       │       ├── fifty-fifty.html
│       │       ├── gallery.html
│       │       ├── switch.html
│       │       ├── page-break.html
│       │       ├── buttons.html
│       │       ├── forms.html
│       │       ├── dialog.html
│       │       ├── navbar.html
│       │       ├── sidebar.html
│       │       ├── banner.html
│       │       ├── badge.html
│       │       ├── table.html
│       │       ├── author-card.html
│       │       ├── footer.html
│       │       └── flare.html      This template's own extras
│       └── example/                A three-page "real" site in this template
│           ├── index.html
│           ├── <page-2>.html       Named per template (e.g. article.html, pricing.html)
│           └── <page-3>.html
├── tools/                          Dev-only, zero runtime dependencies where possible
│   ├── serve.mjs                   Static server for `npm run dev` and the specs
│   ├── check-structure.mjs         Every template has every contract file; links resolve
│   ├── check-tokens.mjs            Retoken contract audit of theme.css / global.css
│   ├── check-fixtures.mjs          Embedded article/form == fixture
│   ├── check-snippets.mjs          Docs code blocks == live examples
│   ├── screenshots.mjs             preview-*.png generation (Playwright)
│   └── vendor-fonts.mjs            Copy @fontsource woff2 + licence into templates/*/fonts
├── tests/
│   ├── helpers/                    Server fixture, page list discovery, scheme helpers
│   ├── templates.spec.ts           Per template × page × scheme: loads clean, no overflow, toggles work
│   ├── components.spec.ts          Accordion, lightbox, dialog, switch, sidebar behaviours
│   └── landing.spec.ts             Cards present, search/filter works
├── docs/
│   ├── README.md                   Documentation index
│   ├── dev/
│   │   ├── plans/                  TODO, this file
│   │   ├── template-contract.md    The contract, prose form (files, components, classes, JS, tokens)
│   │   ├── testing.md              What each check does and when it runs
│   │   └── adding-a-template.md    Copy plain, re-skin, register, run the checks
│   └── user/
│       ├── using-a-template.md     Take the folder, link two files, done
│       └── retoken.md              Paste the palette block into a retoken site
├── .github/workflows/pages.yml     Run `npm run check`, then deploy the repo root to Pages
├── .claude/launch.json             `npm run dev` for the in-app browser
├── package.json                    devDependencies + scripts only
├── CHANGELOG.md · VERSION · LICENSE · README.md
```

Naming notes, all deviations from the TODO's literal text:
- `templates/` (the TODO says `tempaltes/` — treated as a typo).
- `docs/components/` (plural, matching shadcn and retoken's `/components`) rather
  than the TODO's `docs/component/`. Open question 7.
- The "Detailed" art-deco template keeps the TODO's name `detailed` for its
  folder so the landing, the TODO and the folder agree.

## The template contract

Prose form goes to `docs/dev/template-contract.md` in Phase 0; the checks in
`tools/` enforce it; `templates/plain` is it in code.

### Pages

`index.html`, `blogpost.html`, `forms.html`, `sidebar.html`,
`docs/index.html`, `docs/defaults.html`, `docs/blog.html`,
`docs/components/index.html` + one page per component below, and three
`example/*.html` pages. `index.html`, `blogpost.html`, `forms.html` and the
example use the **navbar** layout; `sidebar.html` and everything under `docs/`
use the **sidebar** layout.

### Layout & tokens

- `<html lang="en">` with `<meta name="color-scheme" content="light dark">`;
  `<script src="…/js/theme.js"></script>` in `<head>` before the stylesheets;
  `theme.css` then `global.css`.
- Navbar: `<header class="navbar">` with brand, `<nav>`, scheme toggle
  (`<button class="scheme-toggle">`), and a mobile disclosure driven by a
  checkbox + `:has()`.
- Sidebar layout: `<div class="sidebar-layout">` wrapping `<aside class="sidebar">`
  (a `<nav>` of `<details>` groups), a top bar with the toggle checkbox, and
  `<main>`; drawer-with-scrim below 64rem, like retoken's `SidebarLayout`.
- `main.page`, `.container`, `.stack`, `.row`, `.grid-2`, `.grid-3`, `.muted`,
  `.small`, `.visually-hidden` utilities, matching retoken's names where they
  exist.

### Components (one docs page each)

| Component | Markup | Notes |
| --- | --- | --- |
| Accordion | `<details class="accordion"><summary>` | `.accordion-group` wraps several with a shared `name=` for exclusive open |
| Cards | `<article class="card">` with `.card-media`, `.card-body`, `.card-title`, `.card-text` | `.card-horizontal` (media left), `.card-horizontal.card-media-end` (media right), `.card-feature` = the template's dynamic card (per-template effect) |
| Fifty-fifty | `<section class="fifty-fifty"><figure>…</figure><div>…</div>` | `.fifty-fifty-reverse` puts the image right; stacks image-first on mobile per the UCalgary reference |
| Gallery + lightbox | `<ul class="gallery">` of `<li><figure><button popovertarget="lb-N">` + `<div id="lb-N" popover class="lightbox">` | Prev/next are `popovertarget` buttons to the neighbours; no JS |
| Switch | `<label class="switch"><input type="checkbox" role="switch"><span>` | Also used as the docs' scheme toggle where a template prefers it |
| Page break | `<hr>` (default) and `<hr class="page-break">` (ornamented) | The ornament is per-template flare |
| Buttons | `.btn`, `.btn-primary`, `.btn-danger`, `.btn-sm`, `.btn-lg`, `:disabled` | retoken's set plus `-lg` |
| Forms | native elements + `.field` (label, control, `.hint`, `.error`), `.form-grid`, `fieldset` | The fixture form: text, email, password, number, date, range, color, file, select, textarea, checkbox, radio, switch |
| Dialog | `<dialog class="modal">` | Opener carries the allowed one-liner |
| Navbar / Sidebar | as above | |
| Banner | `.banner` + `-success/-warning/-danger/-info` | retoken |
| Badge | `.badge` | retoken |
| Table | `.table-wrap > table.data-table` | retoken |
| Author card | `<aside class="author-card">` with avatar, name, bio, `.meta` (date, reading time), `.tags > .tag` | Blog post header/footer |
| Footer | `<footer class="footer">` columns | |
| Flare | `.<name>-*` | Whatever the template needs to sell itself; documented on `flare.html` |

Typography, images, blockquotes, code, lists, tables inside `.prose` are on
`defaults.html`, not separate pages.

### JavaScript allow-list

| File | Lines (target) | Why not CSS/HTML |
| --- | --- | --- |
| `js/theme.js` | ≤ 40 | Persisting a scheme choice needs storage; applying it before paint needs script |
| `js/copy.js` (docs only) | ≤ 25 | Clipboard access |
| inline `onclick="…showModal()"` on dialog openers | 1 | `<dialog>` modal mode has no declarative opener yet |
| `landing/landing.js` | ≤ 60 | Text search over cards |

### Tokens

`theme.css` = retoken's `:root, .themed` semantic block verbatim (brand,
surfaces, text, feedback, editor/syntax, typography, spacing, shape, elevation,
layout) + one palette block `:root, [data-theme='<name>']` with the 19 slots:
`--pal-bg0`, `--pal-bg0-soft`, `--pal-bg1`, `--pal-bg2`, `--pal-bg3`,
`--pal-fg`, `--pal-fg-muted`, `--pal-gray`, `--pal-red`, `--pal-green`,
`--pal-yellow`, `--pal-blue`, `--pal-purple`, `--pal-aqua`, `--pal-accent`,
`--pal-accent-strong`, `--pal-on-accent`, `--pal-shadow-1`, `--pal-shadow-2` —
each a `light-dark()` pair. Template-only tokens (`--neon-glow`,
`--glassy-blur`, …) follow in the same file. `global.css` references tokens
only; `tools/check-tokens.mjs` fails on any hex/rgb/hsl/oklch literal outside
`theme.css` (data-URI SVG inside `url()` is exempt).

## Open questions

Each has a default so a single "go with the defaults" is a complete answer.

| # | Question | Needed by | Default if unanswered |
| --- | --- | --- | --- |
| 1 | Shared markup contract across templates (decision 2) — same classes everywhere, swap CSS to swap template? | Phase 0 | Yes. |
| 2 | Add `plain` as an eighth, reference template (decision 3)? Shown on the landing as "Plain — the starting point". | Phase 1 | Yes. |
| 3 | Stylesheet split: `theme.css` + `global.css` (retoken mirror) vs three files (`theme` / `base` / `components`)? | Phase 1 | Two files. |
| 4 | Fonts: self-hosted OFL woff2 via `@fontsource` (decision 14) vs Google Fonts `<link>` vs system stacks only? | Phase 3 | Self-hosted. |
| 5 | Images: local SVG art only (decision 13) vs external photo placeholders (picsum)? | Phase 1 | Local SVG. |
| 6 | Dev tooling as devDependencies (Playwright, html-validate) — acceptable under "no build step"? | Phase 0 | Yes, dev-only. |
| 7 | `docs/components/` (plural) rather than the TODO's `docs/component/`? | Phase 1 | Plural. |
| 8 | GitHub Pages workflow deploying the repo root, at `kieranwood.ca/retemplate/` like retoken? | Phase 0 | Yes; relative links make the base irrelevant. |
| 9 | Accessibility bar (decision 17): structural gate + contrast report-only? | Phase 0 | As stated. |
| 10 | `CHANGELOG.md` currently has a `Developer / Internal` heading; the TODO's rule says `Other`. Rename? | Phase 0 | Rename to `Other`. |
| 11 | Gothic and Allegory have no reference links — are the briefs below the right direction? | Phases 9–10 | Proceed with the briefs. |
| 12 | Checkpoint batches of 3 / 2 / 3 templates built by parallel subagents (below)? | Phase 3 | As planned. |
| 13 | Example-site themes per template (in the briefs) — any you want different? | Phases 3–10 | As briefed. |

## Phase overview

| Phase | Goal | Touches | Parallel? |
| --- | --- | --- | --- |
| 0 | Scaffold: tooling, checks, fixtures, contract doc, CI | root, `tools/`, `tests/`, `fixtures/`, `docs/` | — |
| 1 | `templates/plain` — the contract as code, all pages + docs + example | `templates/plain/` | — |
| 2 | Landing page + preview generation | `index.html`, `landing/`, `tools/screenshots.mjs` | — |
| **A** | **Checkpoint** | | |
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
| 11 | Cross-template review, docs, README, TODO per-template section, release | everything, read-mostly | — |

## Phase 0 — Scaffold & tooling

**Goal:** a repo where `npm run check` and `npm test` mean something before any
template exists, and the contract is written down.

**Scope:**
1. `package.json` (devDependencies: `@playwright/test`, `html-validate`,
   `node-html-parser`, `@axe-core/playwright`; scripts: `dev`, `check`,
   `test`, `screenshots`, `vendor-fonts`), `.gitignore`, `.claude/launch.json`.
2. `tools/serve.mjs` — zero-dependency static server (`node:http`, mime map,
   directory `index.html`), used by `npm run dev` and the specs.
3. `tools/check-structure.mjs` — reads `templates/*/`, asserts every contract
   file exists, parses every `.html`, resolves every relative `href`/`src`,
   fails on a missing target or a root-absolute path, and asserts the landing
   lists every template folder.
4. `tools/check-tokens.mjs` — the retoken audit from the contract.
5. `tools/check-fixtures.mjs` and `tools/check-snippets.mjs` — parity checks.
6. `npm run check` = html-validate over `**/*.html` + the four scripts.
7. `fixtures/markdown-test.md` (every block and inline construct: h1–h6,
   paragraphs, emphasis/strong/strikethrough, inline code, inline and
   reference links, images with alt and title, nested blockquotes with lists
   and code inside, ordered/unordered/nested/task lists, fenced code in two
   languages plus indented code, tables with column alignment, hard breaks,
   footnotes, definition list, `<abbr>`, `<kbd>`, `<mark>`, `<sup>`/`<sub>`,
   `<details>` in markdown), `fixtures/markdown-test.html` (rendered once with
   `marked` at dev time, committed, browser-default styling), and
   `fixtures/forms.html`.
8. `tests/` harness: server fixture, page discovery (globs `templates/*/**/*.html`),
   `forEachScheme` helper, console/pageerror/failed-request collectors.
9. `docs/dev/template-contract.md`, `docs/dev/testing.md`, `docs/README.md`
   index; `templates/README.md`; a first pass at the root `README.md`.
10. `.github/workflows/pages.yml`: install, `npm run check`, upload the repo
    root (minus `node_modules`, `tests`, `tools`) to Pages.
11. Rename the CHANGELOG heading per open question 10.

**Tests:** the checks run green against an empty `templates/` (they must
not crash on nothing). **CHANGELOG:** *Other* — tooling and fixtures.

## Phase 1 — `templates/plain`, the contract as code

**Goal:** every required page, every component, every docs page and a
three-page example site, in a deliberately quiet style, passing every check.

**Scope:**
1. `css/theme.css`: retoken's semantic block verbatim; a `plain` palette
   (retoken's `neutral` values are the obvious seed); shared tokens.
2. `css/global.css`: reset, defaults for every element on `defaults.html`
   (retoken's `global.css` is the starting point — it already covers `.prose`,
   footnotes, `.data-table`, `.banner`, `.badge`, `.btn`), then each contract
   component, then the navbar and sidebar layouts.
3. `js/theme.js`, `js/copy.js`.
4. The four top-level pages, the docs tree (get-started, defaults, blog,
   components index + one page per component with live example, description,
   snippet with copy button, and variants), and `example/` — a small
   documentation-site as the "real" project (home, a guide page, an about page).
5. Local SVG placeholder art in `assets/` — a small set reused by all cards,
   the gallery (8 images), the fifty-fifty, and the author avatar.
6. `README.md` for the template.

**Tests:** `npm run check`; `npm test -- --grep plain` — the
`templates.spec.ts` matrix (every page × light/dark: zero console errors, zero
failed requests, no horizontal overflow at 375 / 768 / 1280, scheme toggle
flips `html.style.colorScheme` and survives reload) and `components.spec.ts`
(accordion opens, exclusive group closes siblings, lightbox opens via popover
and next/prev move, dialog opens and closes, switch toggles `checked`, sidebar
drawer opens at 375). Axe report attached, not gating.

**CHANGELOG:** *Features* — the plain template and the component library.

## Phase 2 — Landing page & previews

**Goal:** `index.html` at the root showing every template with a filter and
title search, and the tooling that makes its preview images.

**Scope:**
1. `index.html` + `landing/landing.css` + `landing/landing.js`: a card per
   template (preview image, name, one-line description, tag chips such as
   *dark-first*, *serif*, *animated*), filter chips by tag, a search box on
   title, links to each template's overview, docs, and example. Card data is
   the HTML itself — no JSON fetch, so it works from `file://`.
2. A link to `fixtures/markdown-test.html` from the landing (the TODO's test
   page) and to the project docs.
3. `tools/screenshots.mjs`: for each template, `index.html` at 1280×800 in
   both schemes → `preview-light.png` / `preview-dark.png`. The landing shows
   the one matching the viewer's scheme.
4. `tests/landing.spec.ts`: every template folder has a card; typing a title
   hides the others; a tag chip filters; the scheme toggle works.

**Tests:** `npm run check`, `npm test -- --grep landing`.
**CHANGELOG:** *Features* — landing page.

> ### CHECKPOINT A
> `npm run check` + `npm test` + `npm run screenshots` green with `plain` and
> the landing. This is the last point where the contract can change cheaply:
> anything the seven templates would all need must land here, because after
> this every contract change is ×8.

## Phases 3–10 — one phase per template

Every template phase has the **same scope**; only the design brief differs.
Subagents work these in the batches marked in the overview, each confined to
its own `templates/<name>/` folder plus the text it returns.

**Scope (identical per template):**
1. Copy `templates/plain` to `templates/<name>`. Re-skin: rewrite
   `theme.css` (palette + shared tokens + namespaced flare tokens) and
   `global.css` (every component restyled; flare added), keep the markup
   contract intact. Vendor the fonts (`npm run vendor-fonts -- <name>`).
2. Replace `assets/` art with pieces that suit the design (SVG).
3. Rewrite the **copy** of `index.html`, `sidebar.html`, `docs/index.html`,
   `docs/components/flare.html` and the three `example/` pages so they read
   in the template's voice; `blogpost.html` and `forms.html` keep the fixture
   bodies verbatim (only the surrounding chrome — author card, hero — changes).
4. `card-feature` gets the template's own effect; `hr.page-break` gets its
   ornament; `flare.html` documents whatever else was added.
5. `README.md` for the template: what it is, the fonts and their licences,
   the flare classes, the retoken paste-in.
6. Run `npm run check` and `npm test -- --grep <name>` until green; run
   `npm run screenshots -- <name>`.
7. **Return to the orchestrator** (do not edit these files directly): the
   landing card HTML, the CHANGELOG entry (*Features*, 2–4 sentences), and the
   TODO boxes earned.

**Done when:** both checks green for the folder; both previews generated; the
axe report read and anything structural fixed; card, changelog and TODO text
delivered.

### Design briefs

Measured values come from the references (computed styles read on
2026-09-03); everything else is the direction to take.

- **Phase 3 — Neumorphic.** Soft-UI: elements extruded from a single
  surface colour by paired light/dark box-shadows; inputs and the switch
  track are *inset*; buttons press flat on `:active`. Light: a cool grey
  `#e0e5ec`-family base with white and blue-grey shadows; dark: charcoal
  `#2a2d34`-family with near-black and lighter-charcoal shadows. Low-contrast
  by nature, so text stays high-contrast and the accent (a muted blue) is
  reserved for focus and primary actions. Radii generous (`--radius-md` 14px).
  Dynamic card: raises on hover, presses on click. Example site: a
  smart-home dashboard (home, a room page, settings).
- **Phase 4 — Brutal News.** From the reference: white paper, black ink,
  `2px solid #000` rules everywhere, one hot accent `#e6331a`, zero radius,
  zero shadows, Inter-class sans for body with JetBrains Mono for kickers and
  data; headlines huge with tight negative tracking (the reference runs
  152px at −7.6px), kickers small uppercase with +1.4px tracking. Masthead
  with volume/date line, multi-column body text (`column-count`) on the
  overview, drop caps, ruled tables. Dark: black paper, white ink, same red.
  Dynamic card: hover inverts to black-on-red. Fonts: Archivo Black (display),
  Inter (body), JetBrains Mono. Example site: a newspaper — front page,
  article, subscribe.
- **Phase 5 — Glassy.** From canadiancoding.ca: a gradient backdrop
  (`linear-gradient(310deg, #141727, #3a416f)` in dark; a light sky/lavender
  pair in light), panels of `rgba(255 255 255 / 0.8)` (light) or
  `rgba(20 23 39 / 0.55)` (dark) with `backdrop-filter: saturate(2) blur(30px)`,
  a 1px inset white border and a soft drop shadow, radii 12–16px, pill
  buttons. The signature: a fixed footer/hero strip of four layered SVG
  waves on a `move-forever` parallax keyframe (CSS only, `<use>` of one path
  at offset delays). Fonts: system-ui (Open Sans-class); no vendoring needed.
  Dynamic card: tilts a few degrees toward the cursor via `:hover` transform
  and brightens its glass. Example site: an agency — home, services,
  contact.
- **Phase 6 — Neon.** From the reference: near-black zinc
  `oklch(0.21 0.006 285)` surfaces, rose-red accent `oklch(0.645 0.246 16)`
  (≈ `#f43f5e`), glow as `0 30px 70px -25px rgb(244 63 94 / 0.5)`, 1px
  borders at 10–15 % white, radii 16 / 24 / pill. Light mode is *less dark*:
  `#26262c`-family surfaces, never white, with the same neon. Add a second
  neon (cyan) for `--pal-blue`/`--pal-aqua` so links and info banners glow
  differently from danger. Fonts: Space Grotesk (display), Inter (body).
  Dynamic card: a slow border-glow sweep on hover (`conic-gradient` mask).
  Example site: a SaaS — home, pricing, changelog.
- **Phase 7 — Natural.** From the reference: cream `#ece7d6` paper, ink
  `#2e2519`, rust accent `#a33b2a`, moss `#3d4a30`, muted `#6b6450`, border
  `#c6c0a8`, uppercase tracked kickers, a faint radial moss tint in the page
  corner. Dark: a dirt-textured backdrop (SVG `feTurbulence` data-URI, no
  image file) in deep brown `#1c150f` with light-green `#b9c9a0` and cream
  text, cream accent. Fonts: Fraunces (display serif), Source Sans 3 (body).
  Dynamic card: a pressed-flower "specimen" card whose label lifts like a
  paper tag on hover. Example site: a plant nursery — home, a field-guide
  entry, visit.
- **Phase 8 — Detailed (art deco).** From the Empire State lobby reference:
  brass and gold on deep navy/black, stepped and fanned geometry, sunburst
  radials, chevron borders, thin double rules. Light: cream `#f3ead8` with
  black ink and gold `#b8902e` accents; dark: `#0d1220` with gold `#d4af37`
  and brass. Ornament is CSS gradients and inline SVG (sunburst headers,
  chevron `hr.page-break`, stepped card corners via `clip-path`). Fonts:
  Poiret One or Limelight (display), Josefin Sans (body). Dynamic card: gold
  leaf sheen sweeping across on hover. Example site: a grand hotel — home,
  restaurant, reservations.
- **Phase 9 — Gothic.** Direction (no reference given): stone greys and
  charcoal with crimson `#7a1f2b` and a cold violet, pointed-arch shapes
  (`clip-path` on media and card tops), tracery rules, a blackletter display
  face used *sparingly* (headings only; body stays readable). Light: pale
  stone `#e9e5dc` with iron ink; dark: near-black with candle-gold
  `#c9a24c` accents. Fonts: UnifrakturMaguntia or Pirata One (display),
  Crimson Pro (body). Dynamic card: a stained-glass colour wash on hover.
  Example site: a cathedral archive — home, a chronicle entry, visiting.
- **Phase 10 — Allegory.** Direction (no reference given): two faces of
  one site. Light is angelic: white and ivory surfaces, gold `#c8a44a`
  accents, feathered/halo SVG ornaments, radiant soft shadows. Dark is
  demonic: black surfaces, red `#b3122e` accents, horn/flame ornaments,
  hard shadows. The `light-dark()` pairs are the mechanism; the flare
  ornaments swap via the same pairs on `content`/`background-image` tokens.
  Fonts: Cormorant Garamond (display), Inter (body). Dynamic card: flips
  between the two faces on hover regardless of scheme. Example site: a
  two-sided storytelling site — home, "the ascent", "the descent".

> ### CHECKPOINTS B, C, D
> After each batch: `npm run check` + `npm test` (all templates, both schemes)
> + `npm run screenshots` green; the orchestrator has merged every returned
> landing card, changelog entry and TODO box; a human-eye pass of each new
> template's overview and docs index in both schemes, noting anything for
> the TODO's **For human** list.

## Phase 11 — Cross-template review, docs, release

**Goal:** the eight templates read as one family, the documentation is
complete, and the repo is releasable.

**Scope:**
1. Contract sweep: `check-structure`, `check-tokens`, `check-snippets` green
   for all eight; a diff of each template's markup against `plain` to catch
   accidental drift beyond flare.
2. Consistency pass on docs copy (the descriptions of each component are the
   same across templates except where a template genuinely differs).
3. `docs/user/using-a-template.md`, `docs/user/retoken.md`,
   `docs/dev/adding-a-template.md`; root `README.md` finished (what it is,
   the landing link, the template list, take-and-use in three lines, retoken
   note, tooling section, licence).
4. Update the TODO's **Per Template** section with the final contract summary
   (the TODO asks for this) and tick the remaining boxes.
5. `CHANGELOG.md` tidied; release date stamped when the owner says so.

**Tests:** full suite green = the release gate.

## Ordering & parallelism

- **Phase 0 blocks everything.** Phase 1 blocks 2 (the landing needs a
  template to show) and blocks every template phase (they copy `plain`).
- **Checkpoint A is the contract freeze.** Changes after it fan out ×8.
- Templates within a batch are independent; the orchestrator runs them as
  parallel subagents, each given: this file, the contract doc, the fixture
  paths, its brief, and the rule that it edits only its own folder and
  returns the three merge texts.
- Batch order puts the simplest re-skins first (Neumorphic, Brutal News,
  Glassy exercise shadows, borders and backdrop effects respectively — three
  different stresses on the contract) so any contract gap surfaces at
  Checkpoint B rather than D.
- Suggested order alone: 0 → 1 → 2 → A → 3, 4, 5 → B → 6, 7 → C → 8, 9, 10 →
  D → 11.

## Deliberately out of scope for 0.1.0

- **A theme editor or picker inside the templates.** Retoken has one; the
  templates just need to be valid input to it.
- **Right-to-left, i18n, print stylesheets beyond sensible defaults.**
- **A component "registry" or CLI** (shadcn-style install). Take the folder.
- **Real photography.** SVG art only; a user swaps in their own images.
- **Polyfills for pre-2024 browsers.**
- **Search on docs pages** (per template). The docs are small enough to scan;
  the landing's search covers template discovery.
