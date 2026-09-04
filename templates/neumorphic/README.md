# Neumorphic

Soft UI: every surface is pushed out of one background colour by a pair of
shadows, one light and one dark. Controls you act on are raised; places you
type into are sunken; a pressed button sinks. Cool grey by day, charcoal by
night. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** — `css/`, `js/theme.js`,
`assets/`, this file — and delete the **showcase** — `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page smart-home site, and
start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="neumorphic">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024 — `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`. No polyfills.
- **Fonts:** [Nunito](https://fonts.google.com/specimen/Nunito) (SIL Open
  Font License) from Google Fonts, for display and body. Remove the three
  `<link>` lines and the template falls back to your system's sans.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare

`.neumorphic-well` (a sunken panel) and `.neumorphic-knob` (a decorative
raised dial, inside `<div class="neumorphic-flare">`). See
`docs/components/flare.html`. Everything else is the shared contract markup.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
Neumorphic to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, drop the fonts `<link>`s, and remove any
`<div class="neumorphic-flare">` wrappers.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="neumorphic">`. Colours carry over; the
shadows that make it neumorphic do not — they live in this template's own
tokens.

```css
:root[data-theme='neumorphic'],
[data-theme='neumorphic'] {
  --pal-bg0: light-dark(#e0e5ec, #2a2d34);
  --pal-bg0-soft: light-dark(#e4e9f0, #2e3239);
  --pal-bg1: light-dark(#d5dbe4, #343841);
  --pal-bg2: light-dark(#c7cfda, #3f444e);
  --pal-bg3: light-dark(#aab4c2, #565c69);
  --pal-fg: light-dark(#2b3444, #e6e9ef);
  --pal-fg-muted: light-dark(#5b6677, #a9b0bc);
  --pal-gray: light-dark(#8791a1, #7f8794);
  --pal-red: light-dark(#b23a30, #e57373);
  --pal-green: light-dark(#2e7d4f, #7fc98f);
  --pal-yellow: light-dark(#a86b12, #e0b46a);
  --pal-blue: light-dark(#2b64a8, #7fb2ff);
  --pal-purple: light-dark(#6a48b5, #b39ddb);
  --pal-aqua: light-dark(#257577, #4dd0e1);
  --pal-accent: light-dark(#3b5c8f, #8fb3ff);
  --pal-accent-strong: light-dark(#2f4a75, #a9c4ff);
  --pal-on-accent: light-dark(#ffffff, #1b2230);
  --pal-shadow-1: light-dark(rgb(163 177 198 / 0.5), rgb(0 0 0 / 0.45));
  --pal-shadow-2: light-dark(rgb(163 177 198 / 0.7), rgb(0 0 0 / 0.6));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace.
