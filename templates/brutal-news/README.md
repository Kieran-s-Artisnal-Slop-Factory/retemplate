# Brutal News

A brutalist newspaper. White paper and black ink, rules never thinner than
three pixels, no rounded corners anywhere, hard offset shadows, and a
handful of harsh colours used at full strength: hot red for the brand, acid
yellow, cobalt, signal green. The overview is a front page: a masthead with
a dateline, a lead story whose headline runs the full width in Archivo Black,
ruled columns with a drop cap, story cards with kickers and bylines, a
scoreboard table. Body in Inter, data in JetBrains Mono. Dark mode is the
same paper printed in reverse. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** (`css/`, `js/theme.js`,
`assets/`, this file) and delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page weekly paper (the Ashcombe Bugle: front page, story,
subscribe), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="brutal-news">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`. No polyfills.
- **Fonts:** [Archivo Black](https://fonts.google.com/specimen/Archivo+Black),
  [Inter](https://fonts.google.com/specimen/Inter) and
  [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono), all
  SIL Open Font License, from Google Fonts. Remove the three `<link>` lines
  and the template falls back to Arial Black, your system sans and your
  system mono.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

The newspaper furniture, all under `/* == flare == */` in `global.css`:
`.hero.brutal-news-lead` (the front-page story: full-width headline, three
ruled columns, byline), `.brutal-news-masthead` with `.brutal-news-dateline`
(inside a `<div class="brutal-news-flare">`), `.brutal-news-columns` with
`.brutal-news-dropcap`, `.brutal-news-ruled` on a grid, `.brutal-news-pullquote`,
`.brutal-news-byline`, `.brutal-news-box` and `.brutal-news-red`. Variants of
contract components, each documented on that component's page:
`.card.brutal-news-story`, `.table-wrap.brutal-news-scoreboard`,
`.btn.brutal-news-stamp` and `.banner.brutal-news-breaking`. See
`docs/components/flare.html` for the list. Everything else is the shared
contract markup.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Brutal
News to another template, replace `css/` and `assets/`, change `data-theme`
on `<html>`, drop the fonts `<link>`s, remove any
`<div class="brutal-news-flare">` wrappers and the `brutal-news-*` classes.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="brutal-news">`. Note that the border
slots are the ink colour and the shadow slots are opaque ink: retoken's
components will draw in the same hard style. The rule weights, the fonts and
the zero radius stay in this template.

```css
:root[data-theme='brutal-news'],
[data-theme='brutal-news'] {
  --pal-bg0: light-dark(#ffffff, #000000);
  --pal-bg0-soft: light-dark(#ffffff, #000000);
  --pal-bg1: light-dark(#f2f2f2, #161616);
  --pal-bg2: light-dark(#000000, #ffffff);
  --pal-bg3: light-dark(#000000, #ffffff);
  --pal-fg: light-dark(#000000, #ffffff);
  --pal-fg-muted: light-dark(#333333, #d4d4d4);
  --pal-gray: light-dark(#6b6b6b, #9a9a9a);
  --pal-red: light-dark(#d42a12, #ff5a3c);
  --pal-green: light-dark(#00a651, #3ddc84);
  --pal-yellow: light-dark(#ffe600, #ffe600);
  --pal-blue: light-dark(#0033ff, #6b8cff);
  --pal-purple: light-dark(#ff00aa, #ff5fc1);
  --pal-aqua: light-dark(#00b5c2, #4de1e8);
  --pal-accent: light-dark(#d42a12, #ff5a3c);
  --pal-accent-strong: light-dark(#a81e0a, #ff8a72);
  --pal-on-accent: light-dark(#ffffff, #000000);
  --pal-shadow-1: light-dark(#000000, #ffffff);
  --pal-shadow-2: light-dark(#000000, #ffffff);
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace.
