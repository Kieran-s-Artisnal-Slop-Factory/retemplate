# Breathe

Air, not paper. A white-green ground with a lot of room, white panels on
soft shadows, sage for the raised surfaces and a mint that is a surface
and never a text colour; links and buttons are a deep leaf green that
clears 4.5:1. By night the ground is forest, a deep blue-green that never
turns brown, with pale sage text and a pale lime accent. Manrope, set light
and wide, for everything that has to be read; Instrument Serif italic for
one word in a heading and nothing else. Pictures take a leaf cut, two
corners round and two sharp. One thing moves: a frond in the hero that
sways in a slow breeze. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page plant-care app
(today, a plant, the week), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="breathe">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Manrope:wght@400;500;600;700&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, and `transform-box` on SVG for the
  frond. No polyfills.
- **Fonts:** Manrope (body and display) and Instrument Serif (the italic
  accent), both OFL, loaded from Google Fonts by the three `<link>`s
  above. Without them the fallback stacks in `theme.css` give Segoe UI or
  Helvetica for the body and Georgia for the italic word. To self-host,
  download the two families, put the files in `fonts/`, add `@font-face`
  rules at the top of `css/global.css` (not `theme.css`, whose palette
  block is pasted elsewhere) and drop the three `<link>`s. Instrument
  Serif is loaded in italic only; the stylesheet never asks it for roman.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those
  calls into a script of your own.
- **Motion:** the frond sways 2.4 degrees from its base over seven seconds
  and each leaf lags a little behind; `--breathe-sway` and
  `--breathe-breath` set both. Under `prefers-reduced-motion: reduce` it
  stands still and every transition shortens to nothing. Nothing else in
  the template animates on its own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.breathe-frond`, an inline SVG with `.breathe-sways`, `.breathe-leaf-l`
  and `.breathe-leaf-r` groups: the plant in the breeze. Draw your own with
  the same class names and it moves the same way.
- `.breathe-pot`: a mint panel with the leaf cut, for the frond or a
  picture.
- `.breathe-stats` on a `.row` of `<dl>`s: big numbers over small labels.
- `.breathe-aside`: one line in Instrument Serif italic.

Five contract components get a variant, each an extra class documented on
its component page:

- `.card.breathe-leaf`, `.fifty-fifty.breathe-leaf`: the picture takes the
  leaf cut (`docs/components/cards.html`, `fifty-fifty.html`).
- `.stack.breathe-stem`: a list of cards becomes a sequence down one thin
  stem with a leaf node per card; `.breathe-now` and `.breathe-done` mark
  the due and the finished (`cards.html`).
- `.btn.breathe-quiet`: a text button with an arrow, for the second action
  beside a primary (`buttons.html`).
- `.badge.breathe-mint`: a filled mint pill with a dot, for the one state
  to notice (`badge.html`).
- `.table-wrap.breathe-week` with `.breathe-drop`, `.breathe-done` and
  `.breathe-today` on cells: a week, one column per day, a drop per task
  (`table.html`).

Markup that is only flare sits inside `<div class="breathe-flare">`
wrappers. The leaf cut is one token, `--breathe-leaf-radius`; the mint is
`--breathe-mint` with `--breathe-mint-deep` and `--breathe-mint-ink`; the
greens of the frond are `--breathe-stem`, `--breathe-leaf` and
`--breathe-leaf-light`; the soft green at the top right of every page is
`--breathe-sage-wash`, a `light-dark()` gradient on `body`. All of them
live in `theme.css`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
Breathe to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, remove the fonts `<link>`s, remove the
`<div class="breathe-flare">` wrappers, and drop the `breathe-*` classes
(the elements that carried them stay valid without them).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="breathe">`. Colours carry
over; the fonts, the leaf cut, the mint and the breeze are this template's
own tokens and stay here. The light accent is the deep green `#2c6b46`,
which passes on the white-green ground where the mint would not; the dark
accent is a pale lime with forest text on it.

```css
:root[data-theme='breathe'],
[data-theme='breathe'] {
  --pal-bg0: light-dark(#f3f7f0, #15231b);
  --pal-bg0-soft: light-dark(#ffffff, #1c2c22);
  --pal-bg1: light-dark(#e6eee1, #26392c);
  --pal-bg2: light-dark(#cfdcc9, #3a5041);
  --pal-bg3: light-dark(#a3b89d, #57705d);

  --pal-fg: light-dark(#1e2b23, #e6ece0);
  --pal-fg-muted: light-dark(#586a5d, #a9baa5);
  --pal-gray: light-dark(#83958a, #7e9282);

  --pal-red: light-dark(#b0432f, #e8957f);
  --pal-green: light-dark(#2e7a4a, #8fd0a0);
  --pal-yellow: light-dark(#8f6400, #dfbe6c);
  --pal-blue: light-dark(#2f6a95, #8fc0e2);
  --pal-purple: light-dark(#6a4f95, #b9a5dc);
  --pal-aqua: light-dark(#227a76, #86ccc6);

  --pal-accent: light-dark(#2c6b46, #c2d9a4);
  --pal-accent-strong: light-dark(#1f5234, #d6e6bf);
  --pal-on-accent: light-dark(#ffffff, #15231b);

  --pal-shadow-1: light-dark(rgb(30 43 35 / 0.06), rgb(0 0 0 / 0.35));
  --pal-shadow-2: light-dark(rgb(30 43 35 / 0.16), rgb(0 0 0 / 0.55));
}
```

## Licence

MIT, like the rest of retemplate. The plant drawings and other art in
`assets/` are original and free to reuse or replace. Manrope and
Instrument Serif are licensed under the SIL Open Font License by their
authors.
