# Gothic

Pale stone and iron ink with a crimson accent by day; near-black stone with
candle-gold accents by night. One pointed arch, cut with `clip-path`, on
the hero picture, the gallery, the avatar and an arched card; every other
corner square. UnifrakturMaguntia for `h1`, `h2` and the masthead only,
Crimson Pro for everything that has to be read, with small caps for labels,
navigation and buttons. Tracery rules drawn as masks, an illuminated
initial, and a feature card that fills with stained glass when you hover.
Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page cathedral archive,
and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="gothic">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=UnifrakturMaguntia&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `clip-path`, `mask-image`. No polyfills.
- **Fonts:** UnifrakturMaguntia (display) and Crimson Pro (body), both
  OFL, loaded from Google Fonts by the three `<link>`s above. Without them
  the fallback stacks in `theme.css` give Old English Text MT or another
  system blackletter where one exists, and Palatino or Georgia for the
  body. To self-host, download the two families, put the files in
  `fonts/`, add `@font-face` rules at the top of `css/global.css` (not
  `theme.css`, whose palette block is pasted elsewhere) and drop the three
  `<link>`s. Blackletter has one weight and no italic; the stylesheet never
  asks it for either.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those
  calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.gothic-initial` on a paragraph: an illuminated first letter.
- `.gothic-manuscript` with a `.gothic-marginalia` aside: a two-column
  page with notes in the margin.
- `.gothic-rose`: sizes an inline rose-window SVG.
- `hr.gothic-tracery`: an arcade rule, one small arch repeated
  (`docs/components/page-break.html`). The contract's `hr.page-break` is
  the other ornament, a quatrefoil.
- `.card.gothic-arch`: the card's picture becomes a lancet
  (`docs/components/cards.html`).

Markup that is only flare sits inside `<div class="gothic-flare">`
wrappers. Nothing animates continuously; the only motion is the
stained-glass wash on the feature card and the arch marker on an
accordion, both transitions the global `prefers-reduced-motion` rule
shortens to nothing.

The arch is one token, `--gothic-arch`, a polygon in percentages. The
tracery is two SVG masks, `--gothic-tracery` and `--gothic-rule`, filled
with `--gothic-ornament`, which is crimson in the light half and candle
gold in the dark one. All of them live in `theme.css`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
Gothic to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, remove the fonts `<link>`s, remove the
`<div class="gothic-flare">` wrappers, and drop the `gothic-*` classes
(the elements that carried them stay valid without them).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="gothic">`. Colours carry
over; the fonts, the arch, the tracery and the glass are this template's
own tokens and stay here. The light accent is the crimson `#7a1f2b`, which
passes on pale stone but not on near-black, so the dark accent is the gold.

```css
:root[data-theme='gothic'],
[data-theme='gothic'] {
  --pal-bg0: light-dark(#e9e5dc, #111014);
  --pal-bg0-soft: light-dark(#f2efe7, #1a181e);
  --pal-bg1: light-dark(#dcd7cb, #242128);
  --pal-bg2: light-dark(#bcb5a6, #3b363f);
  --pal-bg3: light-dark(#948c7c, #57515e);

  --pal-fg: light-dark(#23222a, #e6e1d6);
  --pal-fg-muted: light-dark(#5c5866, #aaa39b);
  --pal-gray: light-dark(#7d7885, #7b7580);

  --pal-red: light-dark(#8e2230, #d46a72);
  --pal-green: light-dark(#35603f, #8fb894);
  --pal-yellow: light-dark(#6a500d, #d9b866);
  --pal-blue: light-dark(#3f5a82, #8fa6c9);
  --pal-purple: light-dark(#5b4a7c, #b09ad0);
  --pal-aqua: light-dark(#2f6a72, #86bcc0);

  --pal-accent: light-dark(#7a1f2b, #c9a24c);
  --pal-accent-strong: light-dark(#5e1520, #e0bf6b);
  --pal-on-accent: light-dark(#f2efe7, #111014);

  --pal-shadow-1: light-dark(rgb(35 34 42 / 0.14), rgb(0 0 0 / 0.5));
  --pal-shadow-2: light-dark(rgb(35 34 42 / 0.26), rgb(0 0 0 / 0.7));
}
```

## Licence

MIT, like the rest of retemplate. The window drawings and other art in
`assets/` are original and free to reuse or replace. UnifrakturMaguntia
and Crimson Pro are licensed under the SIL Open Font License by their
authors.
