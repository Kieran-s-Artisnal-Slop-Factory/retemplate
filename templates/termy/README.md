# Termy

A terminal. By day a dark green screen: near-black green ground, phosphor
green text and accent, a glow on the letters and scanlines over the page.
By night the same terminal printed on paper: black on white, deep green
accent, no glow. JetBrains Mono for everything, no corners anywhere,
brackets around every button, a prompt before every kicker and a hash
before every heading, a cursor blinking after the hero. The CRT overlay is
one class on `<body>` and two tokens, so it can be turned down, or off.
Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** — `css/`, `js/theme.js`,
`assets/`, this file — and delete the **showcase** — `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page site, and start
from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="termy">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>My page</title>
  <link rel="icon" href="assets/favicon.svg">
  <script src="js/theme.js"></script>
  <link rel="stylesheet" href="css/theme.css">
  <link rel="stylesheet" href="css/global.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,600;0,800;1,400&display=swap">
</head>
<body class="termy-crt">
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024 — `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`. No polyfills.
- **Fonts:** JetBrains Mono (OFL), from Google Fonts by the three `<link>`s
  above; without it the fallback stack in `theme.css` gives the system's
  monospace face. To self-host, put the files in `fonts/`, add `@font-face`
  rules at the top of `css/global.css` and drop the three `<link>`s.
- **CRT:** `class="termy-crt"` on `<body>` switches the scanlines, vignette,
  glow and flicker on. `--termy-crt-strength` (0 to 1, default 0.5) sets
  how strong the overlay is; `--termy-crt-flicker: 0` keeps the lines and
  stops the flicker. Reduced motion stops the flicker and the cursor.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Termy to
another template, replace `css/`, `assets/` and (if present) `fonts/`, change
`data-theme` on `<html>`, and remove any `<div class="<name>-flare">`
wrappers the old template added.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="termy">` (or in the theme editor).
Colours carry over; fonts, radii and spacing are set in the editor.

```css
:root[data-theme='termy'],
[data-theme='termy'] {
  --pal-bg0: light-dark(#0a1f13, #ffffff);
  --pal-bg0-soft: light-dark(#0d2618, #fafafa);
  --pal-bg1: light-dark(#12301f, #f0f0f0);
  --pal-bg2: light-dark(#1c4530, #d6d6d6);
  --pal-bg3: light-dark(#2f6a4a, #a8a8a8);

  --pal-fg: light-dark(#c9f5d3, #111111);
  --pal-fg-muted: light-dark(#7fcf9a, #555555);
  --pal-gray: light-dark(#5a9a72, #8a8a8a);

  --pal-red: light-dark(#ff7b72, #b3001b);
  --pal-green: light-dark(#5cff8a, #0b6e2a);
  --pal-yellow: light-dark(#ffd75e, #7a5200);
  --pal-blue: light-dark(#6ec6ff, #0b4fa8);
  --pal-purple: light-dark(#d3a6ff, #6b2fb3);
  --pal-aqua: light-dark(#5ff2e0, #007a70);

  --pal-accent: light-dark(#5cff8a, #0b6e2a);
  --pal-accent-strong: light-dark(#9dffb8, #084f1f);
  --pal-on-accent: light-dark(#0a1f13, #ffffff);

  --pal-shadow-1: light-dark(rgb(92 255 138 / 0.35), rgb(17 17 17 / 0.2));
  --pal-shadow-2: light-dark(rgb(92 255 138 / 0.55), rgb(17 17 17 / 0.85));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace.
