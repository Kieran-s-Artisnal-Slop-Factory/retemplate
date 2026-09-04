# retemplate

Complete, re-usable HTML + CSS website templates and themes. Take a folder,
drop it in your project, write HTML. No build step, no framework, no
dependencies — and every template's palette is a
[retoken](https://kieranwood.ca/retoken/theme/) theme.

- **Landing page:** `index.html` — every template, with previews and a filter.
- **Templates:** [`templates/`](templates/README.md), one folder each.
- **Docs:** [`docs/`](docs/README.md) — using a template, the contract, testing.

## Take and use

1. Copy `templates/<name>/`.
2. Keep `css/`, `js/theme.js`, `fonts/` (if present) and `assets/`; delete
   the demo pages, `docs/` and `example/` — or start from `example/`, a
   complete three-page site.
3. Paste the head block from the template's README into your pages.

Browser floor: Baseline 2024 (`light-dark()`, `:has()`, popovers).

## Repository

```
index.html      landing page
landing/        its assets and the template previews
templates/      the templates
fixtures/       the shared demo content every template embeds
tools/check.py  the structural checker (python, standard library only)
docs/           documentation and plans
```

Checks: `python tools/check.py`. Serve locally: `python -m http.server 8080`.

## Licence

MIT (see `LICENSE`). Fonts, when a template links Google Fonts, are under
their own licences (SIL OFL); each template's README lists them.
