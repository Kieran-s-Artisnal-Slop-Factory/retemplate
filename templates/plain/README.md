# Plain

The reference template of [retemplate](../../README.md): every component the
contract asks for, in a quiet style. The other templates are copies of this
one, re-skinned.

## Take and use

Copy this folder. Keep the **install set** — `css/`, `js/theme.js`,
`assets/`, this file — and delete the **showcase** — `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page site, and start
from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="plain">
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

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024 — `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`. No polyfills.
- **Fonts:** none. Plain uses the system font stacks.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Plain to
another template, replace `css/`, `assets/` and (if present) `fonts/`, change
`data-theme` on `<html>`, and remove any `<div class="<name>-flare">`
wrappers the old template added.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="plain">` (or in the theme editor).
Colours carry over; fonts, radii and spacing are set in the editor.

```css
:root[data-theme='plain'],
[data-theme='plain'] {
  --pal-bg0: light-dark(#fafafa, #131316);
  --pal-bg0-soft: light-dark(#ffffff, #1b1b1f);
  --pal-bg1: light-dark(#f4f4f5, #232329);
  --pal-bg2: light-dark(#e4e4e7, #34343c);
  --pal-bg3: light-dark(#c9c9d0, #4a4a55);
  --pal-fg: light-dark(#1c1c1f, #ececef);
  --pal-fg-muted: light-dark(#6b6b73, #9d9da8);
  --pal-gray: light-dark(#8b8b95, #74747f);
  --pal-red: light-dark(#c62828, #f87171);
  --pal-green: light-dark(#1a7f37, #4ade80);
  --pal-yellow: light-dark(#b45309, #d9a441);
  --pal-blue: light-dark(#1d6fe0, #6ea8fe);
  --pal-purple: light-dark(#6d3fc0, #b18cf0);
  --pal-aqua: light-dark(#00838f, #3ec9d6);
  --pal-accent: light-dark(#4056c9, #8fa2ff);
  --pal-accent-strong: light-dark(#32449f, #aab8ff);
  --pal-on-accent: light-dark(#ffffff, #101223);
  --pal-shadow-1: light-dark(rgb(28 28 31 / 0.08), rgb(0 0 0 / 0.4));
  --pal-shadow-2: light-dark(rgb(28 28 31 / 0.14), rgb(0 0 0 / 0.55));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace.
