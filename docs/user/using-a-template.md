# Using a template

Every template is a folder you copy. There is no build step, no framework
and nothing to install; the folder works from disk, from a sub-path on a
host, or dropped into another project's `public/`. The get-started page
inside each template, `templates/<name>/docs/index.html`, says the same
things with live examples in that template's own style.

## 1. Pick one

Open [the landing page](../../index.html) (or `templates/README.md`), filter
by scheme, type, motion, fonts or feel, and read the overview, the docs and
the example site. Every template has the same pages, so once you know one
you know them all.

## 2. Copy the folder

Copy `templates/<name>/` into your project. Two sets of files are inside:

- **The install set**, which you keep: `css/`, `js/theme.js`, `assets/`,
  `fonts/` (only if the template self-hosts fonts) and `README.md`. Nothing
  in it points outside the folder.
- **The showcase**, which you delete: `index.html`, `blogpost.html`,
  `forms.html`, `sidebar.html`, `docs/`, `example/` and `js/copy.js`.

Or keep `example/`: it is a complete three-page site in the template's
voice, and a reasonable place to start.

## 3. Put the head block on every page

Copy it from the template README (or from `docs/index.html`). Adjust the
relative paths for pages in sub-folders.

```html
<!doctype html>
<html lang="en" data-theme="<name>">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>My page</title>
  <link rel="icon" href="assets/favicon.svg">
  <script src="js/theme.js"></script>
  <link rel="stylesheet" href="css/theme.css">
  <link rel="stylesheet" href="css/global.css">
</head>
```

Three things matter here. `data-theme="<name>"` selects the palette.
`theme.js` is a plain synchronous script *before* the stylesheets so a
saved light or dark choice applies before the first paint. Templates that
use Google Fonts add their `<link>` (and two `preconnect` hints) after
`global.css`; the README lists the families and how to self-host them
instead.

## 4. Write HTML

Use the classes documented under `docs/components/`. Each component page
shows the live component, its markup with a copy button, its variants, a
table of classes and notes on behaviour and keyboard use. The same markup
works in every template, so switching later is a swap of `css/`, `assets/`
and the `data-theme` value. Template-specific flourishes are namespaced
`.<name>-*` classes and, when they need markup, sit inside a
`<div class="<name>-flare">` so they can be stripped mechanically.

## Light and dark

Every template ships both. Colours follow the visitor's system preference
through `color-scheme` and `light-dark()`. The `.scheme-toggle` button
cycles auto, light, dark and stores the choice under the `retoken-scheme`
key, which retoken sites read too, so a template page and a retoken page on
the same origin agree. Everything that is not a colour (a texture, an
ornament image) keys off `<html data-scheme>`, which `theme.js` keeps equal
to the effective scheme.

## JavaScript

Almost none. `theme.js` (the toggle, about 45 lines) and a one-line
`onclick="…showModal()"` on buttons that open a dialog or the lightbox.
Under a strict Content-Security-Policy, move those one-liners into a script
of your own. Menus, drawers, accordions and the lightbox slides are native
HTML: popovers, `<details name>`, `<dialog>` and `:target`.

## Browsers

Baseline 2024: `light-dark()`, `:has()`, the Popover API, `<details name>`,
`color-mix()` and `::backdrop`. No polyfills are shipped.

## Related

- [Using a template's theme in retoken](retoken.md)
- The contract every template follows: [template-contract.md](../dev/template-contract.md)
