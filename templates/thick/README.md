# Thick

Warm paper, black ink, one bright yellow and two pastels by day; a warm
near-black with off-white ink, the same yellow and dusky pastels by night.
Every box has a 3px outline and sits on a solid offset shadow with no blur,
4px for small things and 8px for large ones; press a button, a text field, a
thumbnail or the feature card and it drops into the page by the same
distance. Rubik at 900 for headings and the brand, Rubik at 400 to 700 for
everything else, so the page has one voice. Stickers, a tilt, a yellow band
and the pile, a stack of outlined sheets under a picture, are the flare.
Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page zine shop, and
start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="thick">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700;900&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`. No polyfills.
- **Fonts:** Rubik, one family in four weights (400, 500, 700, 900), OFL,
  loaded from Google Fonts by the three `<link>`s above. Without it the
  fallback stack in `theme.css` gives Arial Black for the headings and
  Segoe UI, Roboto or Arial for the text: heavier and plainer, same
  layout. To self-host, download Rubik, put the files in `fonts/`, add
  `@font-face` rules at the top of `css/global.css` (not `theme.css`,
  whose palette block is pasted elsewhere) and drop the three `<link>`s.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those
  calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.thick-pile` on a `<figure>` around an image: the picture sits on a
  stack of outlined pink and blue sheets. The signature; the overview's
  hero uses it.
- `.thick-band`: a yellow block across the page for the one thing you
  want the reader to do. One per page.
- `.thick-yellow`, `.thick-pink`, `.thick-blue`: tinted surfaces for any
  block, and variants of `.card` (`docs/components/cards.html`) and
  `.fifty-fifty` (`docs/components/fifty-fifty.html`).
- `.thick-sticker`: pink, tilted five degrees, on a 3px shadow, on its own
  or on a `.badge` (`docs/components/badge.html`). A direct child of
  `.hero` pins itself to the hero's top edge.
- `.thick-tilt`: three degrees and nothing else.
- `.btn.thick-flat`: a button with no shadow, for rows of small actions
  (`docs/components/buttons.html`).

Markup that is only flare sits inside `<div class="thick-flare">`
wrappers. Nothing moves on its own. The only motion is the press: a 120ms
transition on `transform` and `box-shadow` when you hover or hold a
button, a text field, a thumbnail or the feature card. The global
`prefers-reduced-motion` rule shortens it to nothing, so the element still
moves, but jumps rather than slides.

The outline weight, the two offsets, the ink, the yellow, the two pastels,
the scrim, the footer colours, the pile and the page break's stripes are
`--thick-*` tokens in `theme.css`. Outlines are drawn in `--border-color`,
which is the `--pal-bg2` slot; that slot is the ink, so the whole template
turns to off-white outlines after dark from one pair.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Thick
to another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>`s, remove the `<div class="thick-flare">`
wrappers, and drop the `thick-*` classes (the elements that carried them
stay valid without them).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="thick">`. Colours carry
over; the font, the outlines, the offsets and the yellow fill are this
template's own tokens and stay here. Yellow on white cannot carry a link,
so the light accent is the ink, `#111111`, and the yellow is a fill token;
after dark the accent is the yellow itself, `#ffd400`, with near-black
text on it.

```css
:root[data-theme='thick'],
[data-theme='thick'] {
  --pal-bg0: light-dark(#fffdf5, #141412);
  --pal-bg0-soft: light-dark(#ffffff, #1c1c19);
  --pal-bg1: light-dark(#f3efe3, #262620);
  --pal-bg2: light-dark(#111111, #f5f1e6);
  --pal-bg3: light-dark(#3d3a35, #c9c4b4);

  --pal-fg: light-dark(#111111, #f5f1e6);
  --pal-fg-muted: light-dark(#4d4842, #bdb7a6);
  --pal-gray: light-dark(#7a746a, #8b8577);

  --pal-red: light-dark(#c8264a, #ff7a95);
  --pal-green: light-dark(#1d7d45, #62d68c);
  --pal-yellow: light-dark(#8a5a00, #ffd400);
  --pal-blue: light-dark(#1d55c4, #86adff);
  --pal-purple: light-dark(#7238c4, #c7a3ff);
  --pal-aqua: light-dark(#0b6f80, #5cd0e0);

  --pal-accent: light-dark(#111111, #ffd400);
  --pal-accent-strong: light-dark(#000000, #ffe25c);
  --pal-on-accent: light-dark(#ffd400, #141412);

  --pal-shadow-1: light-dark(rgb(17 17 17 / 0.16), rgb(0 0 0 / 0.5));
  --pal-shadow-2: light-dark(rgb(17 17 17 / 0.28), rgb(0 0 0 / 0.7));
}
```

## Licence

MIT, like the rest of retemplate. The stickers, the stapler, the floppy
disk and the other art in `assets/` are original and free to reuse or
replace. Rubik is licensed under the SIL Open Font License by its authors.
