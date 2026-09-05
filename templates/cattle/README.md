# Cattle

Pale maple by day, dark oiled leather by night. The headings are branded
into the board: charred lettering in Alfa Slab One with a scorched halo
that bleeds a few pixels into the grain, and thick burnt rules above and
below the hero headline. Everything that frames the board, the navbar, the
sidebar, the footer and the author card, is saddle leather with a running
stitch in thread and lettering tooled into it. Bitter for everything that
has to be read, tracked capitals for labels, buttons and the maker's mark.
Brass rivets on the switch, the accordion and the rivet button; a steer
mark on the page break; a menu list with burnt prices; and a feature card
whose title burns in when you rest on it. Part of
[retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page smokehouse (home,
menu, book a table), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="cattle">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bitter:ital,wght@0,400;0,600;0,700;1,400&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `mask-image`, SVG filters in
  `background-image`. No polyfills.
- **Fonts:** Alfa Slab One (display) and Bitter (body), both OFL, loaded
  from Google Fonts by the three `<link>`s above. Without them the fallback
  stacks in `theme.css` give Rockwell or Roboto Slab where one exists and
  Georgia for the body; the burn is a `text-shadow` and works on any face.
  To self-host, download the two families, put the files in `fonts/`, add
  `@font-face` rules at the top of `css/global.css` (not `theme.css`, whose
  palette block is pasted elsewhere) and drop the three `<link>`s. Alfa
  Slab One has one weight and no italic; the stylesheet never asks it for
  either.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those
  calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.cattle-brand` on anything: burnt lettering, the way `h1` and `h2`
  already are.
- `.cattle-leather` on any block: a stitched saddle-leather panel. Inside
  it the semantic tokens are re-pointed, so text comes out cream, links
  thread, and burnt headings tooled. The navbar, sidebar, footer and
  author card are the same panel.
- `.cattle-mark`: the steer mark, drawn from a token, scorched.
- `.cattle-menu` with `.cattle-menu-name`, `-price`, `-note`: a menu list
  with a dotted leader and a burnt price.
- `.card.cattle-stitched`: a leather frame with the stitch through it
  (`docs/components/cards.html`).
- `.btn.cattle-rivet`: a leather strap with two brass rivets
  (`docs/components/buttons.html`).
- `hr.cattle-rope`: two strands of hemp (`docs/components/page-break.html`).
  The contract's `hr.page-break` is the other ornament, the steer mark
  between two burnt rules.

Markup that is only flare sits inside `<div class="cattle-flare">`
wrappers. The only motion is the burn-in on the feature card, the rivet
marker on an accordion and the press of a button, all transitions the
global `prefers-reduced-motion` rule shortens to nothing.

The burn is two tokens: `--cattle-char` (the fill, charred by day and
cream by night) and `--cattle-burn`, one `text-shadow` list whose scorch
layers are transparent in the dark half and whose tooling layers are
transparent in the light half, so it needs no `data-scheme` hook and
survives the retoken paste-in. The wood grain (`--cattle-grain`) and the
leather pebbling (`--cattle-leather`) are two small `feTurbulence` SVGs
layered on `body` with a veil between them that is bg0 by day and nothing
by night. The mark is `--cattle-mark`, a mask; replace it and your own
mark appears on every page break. All of them live in `theme.css`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
Cattle to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, remove the fonts `<link>`s, remove the
`<div class="cattle-flare">` wrappers, and drop the `cattle-*` classes
(the elements that carried them stay valid without them).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="cattle">`. Colours carry
over; the fonts, the burn, the grain and the leather are this template's
own tokens and stay here. The light accent is saddle brown `#7a3b17`,
which passes on maple but not on dark leather, so the dark accent is
brass. Neither half is black or white.

```css
:root[data-theme='cattle'],
[data-theme='cattle'] {
  --pal-bg0: light-dark(#e8d9bf, #2a1a12);
  --pal-bg0-soft: light-dark(#f0e4cd, #33221a);
  --pal-bg1: light-dark(#dcc9a6, #3d2a20);
  --pal-bg2: light-dark(#c4ad83, #553b2d);
  --pal-bg3: light-dark(#9e8660, #74533f);

  --pal-fg: light-dark(#2a1a12, #efe2c8);
  --pal-fg-muted: light-dark(#6b5340, #c9b08e);
  --pal-gray: light-dark(#8c7a62, #9a8368);

  --pal-red: light-dark(#9c2a1e, #e08a72);
  --pal-green: light-dark(#4e6b2f, #a3bf7a);
  --pal-yellow: light-dark(#8a5a12, #e0b866);
  --pal-blue: light-dark(#3f5c7a, #93aecb);
  --pal-purple: light-dark(#6d4a6a, #bb9cc0);
  --pal-aqua: light-dark(#2f6b62, #8ec2b4);

  --pal-accent: light-dark(#7a3b17, #d9a65a);
  --pal-accent-strong: light-dark(#5a2a0e, #e8bd78);
  --pal-on-accent: light-dark(#f3e7cf, #2a1a12);

  --pal-shadow-1: light-dark(rgb(42 26 18 / 0.16), rgb(0 0 0 / 0.45));
  --pal-shadow-2: light-dark(rgb(42 26 18 / 0.28), rgb(0 0 0 / 0.65));
}
```

## Licence

MIT, like the rest of retemplate. The burnt boards, the leather and the
other art in `assets/` are original and free to reuse or replace. Alfa
Slab One and Bitter are licensed under the SIL Open Font License by their
authors.
