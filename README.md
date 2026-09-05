# retemplate

Complete, re-usable HTML + CSS website templates and themes. Take a folder,
drop it in your project, write HTML. No build step, no framework, no
dependencies, light and dark in every one. Every template's palette is also
a [retoken](https://kieranwood.ca/retoken/theme/) theme.

- **Landing page:** `index.html`, every template with previews, a title
  search and tag filters.
- **Templates:** [`templates/`](templates/README.md), one folder each: Plain,
  Neumorphic, Brutal News, Glassy, Neon, Natural, Detailed, Gothic, Allegory.
- **Docs:** [`docs/`](docs/README.md): using a template, using its theme in
  retoken, the contract every template follows, testing, adding a template.

## Take and use

1. Copy `templates/<name>/`.
2. Keep `css/`, `js/theme.js`, `fonts/` (if present) and `assets/`; delete
   the demo pages, `docs/` and `example/`. Or start from `example/`, a
   complete three-page site.
3. Paste the head block from the template's README into your pages and
   write HTML with the classes its docs describe.

Every template uses the same markup and class names, so switching templates
later is a swap of `css/`, `assets/` and one `data-theme` attribute. Each
one also has its own structure, component variants and voice; the shared
contract is the floor, not the ceiling.

Browser floor: Baseline 2024 (`light-dark()`, `:has()`, popovers,
`<details name>`, `color-mix()`). No polyfills.

## Repository

```
index.html      landing page
landing/        its assets and the template previews
templates/      the templates, one folder each
fixtures/       the shared demo content every template embeds verbatim
tools/check.py  the structural checker (python, standard library only)
docs/           documentation and plans
```

Checks: `python tools/check.py` (add `--template <name>` for one template).
Serve locally: `python -m http.server 8080`. The GitHub Pages workflow runs
the checker and publishes the repository root; there is nothing to build.

## Licence

MIT (see `LICENSE`). Fonts, when a template links Google Fonts, are under
their own licences (SIL OFL); each template's README lists them. The
placeholder art in every `assets/` folder is original and free to reuse.
