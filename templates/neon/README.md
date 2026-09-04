# Neon

Black zinc, hairline borders and two neon tubes: a rose one for what matters
and a cyan one for what is merely true. Everything glows rather than fills.
The light mode is only *less dark* — the ground lifts to a warm grey and the
text stays off-white, so the glow keeps working and nothing is ever white.
Headings in Space Grotesk, body in Inter. Part of
[retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** — `css/`, `js/theme.js`,
`assets/`, this file — and delete the **showcase** — `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page SaaS site (home,
pricing, changelog), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="neon">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024 — `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, and `@property` for the feature card's
  animated border. No polyfills.
- **Fonts:** Inter (body) and Space Grotesk (headings), from Google Fonts by
  the `<link>` above. To self-host instead, download the two families from
  [Google Fonts](https://fonts.google.com/) (both are OFL), put the `woff2`
  files in a `fonts/` folder beside `css/`, add `@font-face` rules at the top
  of `css/global.css` pointing at `../fonts/…`, and drop the three lines
  above. `theme.css` already names the families with a system fallback, so
  the page reads fine while they load or if they never do.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Native controls:** both halves are dark, so `global.css` pins `select`,
  `input`, `textarea`, `dialog` and open popovers to `color-scheme: dark`
  and sets `scrollbar-color` on `:root`. The browser never paints a white
  dropdown, date picker or scrollbar; inside those elements the palette
  resolves to its dark half in either scheme, so a form field is always a
  black well.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare

`.neon-haze` (two blurred tubes fixed behind the page; put it right after
`<body>` inside `<div class="neon-flare">`), `.neon-text` /
`.neon-text-cyan` (lit words), `.neon-sign` / `.neon-sign-cyan` (a lit pill
label) and `.neon-glow` / `.neon-glow-cyan` (the glow shadow on any block).
See `docs/components/flare.html`. The haze's breathing, the sign's flicker
and the feature card's border sweep all stop under `prefers-reduced-motion`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Neon to
another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>` lines, and remove the
`<div class="neon-flare">` wrapper and any `.neon-*` classes.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="neon">`. Colours carry over — including
the never-white light half; the glows, the hairlines and the haze are this
template's own tokens and stay here.

```css
:root[data-theme='neon'],
[data-theme='neon'] {
  --pal-bg0: light-dark(#3a3a42, #18181b);
  --pal-bg0-soft: light-dark(#43434c, #1f1f23);
  --pal-bg1: light-dark(#4b4b55, #26262b);
  --pal-bg2: light-dark(#525259, #343436);
  --pal-bg3: light-dark(#6a6a76, #4b4b4d);
  --pal-fg: light-dark(#f5f5f7, #f4f4f5);
  --pal-fg-muted: light-dark(#c4c4cc, #a1a1aa);
  --pal-gray: light-dark(#9a9aa6, #71717a);
  --pal-red: light-dark(#ff8a8a, #f87171);
  --pal-green: light-dark(#4ade80, #34d399);
  --pal-yellow: light-dark(#fcd34d, #fbbf24);
  --pal-blue: light-dark(#22d3ee, #22d3ee);
  --pal-purple: light-dark(#c4b5fd, #a78bfa);
  --pal-aqua: light-dark(#67e8f9, #67e8f9);
  --pal-accent: light-dark(#ff8fa3, #f43f5e);
  --pal-accent-strong: light-dark(#fda4af, #fb7185);
  --pal-on-accent: light-dark(#18181b, #18181b);
  --pal-shadow-1: light-dark(rgb(0 0 0 / 0.35), rgb(0 0 0 / 0.5));
  --pal-shadow-2: light-dark(rgb(0 0 0 / 0.5), rgb(0 0 0 / 0.7));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace. The fonts are Google's under the SIL
Open Font License.
