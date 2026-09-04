# Allegory

Two faces of one site. By day the page is ivory with an antique gold for
links and a brighter gold for the bands that carry white display type:
wings around a halo, a soft radiance from above. By night the page is
off-black with a red for links and a deeper red for the bands that carry
black display type: horns around a flame, hard offset shadows. Cormorant
Garamond for the telling, Inter for the controls. Two classes pin any
element to one face whatever the visitor chose, and the feature card turns
over to show the other. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page story site whose two
chapter pages mirror each other, and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="allegory">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `mask-image`, `color-scheme` on an
  element. No polyfills.
- **Fonts:** Cormorant Garamond (display) and Inter (body), both OFL, loaded
  from Google Fonts by the three `<link>`s above. Without them the fallback
  stacks in `theme.css` are Garamond/Times and Segoe UI/Helvetica. To
  self-host, download the two families, put the files in `fonts/`, add
  `@font-face` rules at the top of `css/global.css` (not `theme.css`, whose
  palette block is pasted elsewhere) and drop the three `<link>`s.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those calls
  into a script of your own. The script also mirrors the scheme in effect to
  `<html data-scheme>`, which is what swaps the wings for the horns.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

One idea, documented on `docs/components/flare.html`: `.allegory-halo` pins
an element to the day face and `.allegory-horn` to the night face, by
setting `color-scheme` on it and re-pointing the ornament. Put either on a
card, a page header or a section, or both on the two children of an
`.allegory-diptych`, the split section the overview opens with. Around
that: `.allegory-band` (display type on the gold or red band, the literal
white-on-gold and black-on-red of the brief, never for body text),
`.allegory-verse` (a centred quotation with the ornament above it) and
`.btn.allegory-vow` (a button in italic display type). Decoration that
needs markup sits inside `<div class="allegory-flare">`. Nothing animates
continuously; the only motion is the feature card's turn and a short fade
on scheme change, both shortened to nothing by the global
`prefers-reduced-motion` rule.

The radiance by day and the flame by night are `--allegory-*` gradient
tokens layered on `<body>`, each transparent in the other half; remove
`background-image` from `body` in `global.css` to lose both. The ornaments
are `--allegory-wings` and `--allegory-horns`, SVG data URIs used as masks
and filled with the band colour; `--allegory-ornament` chooses between them
and is re-pointed under `:root[data-scheme='dark']`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Allegory
to another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>`s, remove the `allegory-*` classes and
any `<div class="allegory-flare">` wrappers.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="allegory">`. Colours carry over, both
faces of them; the fonts, the bands, the ornaments and the pins are this
template's own tokens and stay here.

```css
:root[data-theme='allegory'],
[data-theme='allegory'] {
  --pal-bg0: light-dark(#fbf7ee, #0b0708);
  --pal-bg0-soft: light-dark(#fffdf7, #16100f);
  --pal-bg1: light-dark(#f2ead7, #20171a);
  --pal-bg2: light-dark(#dccfa8, #3d2429);
  --pal-bg3: light-dark(#bfa96e, #5e333d);
  --pal-fg: light-dark(#2a2418, #f3ebe6);
  --pal-fg-muted: light-dark(#6e6246, #b89b98);
  --pal-gray: light-dark(#8f856d, #7d6a6a);
  --pal-red: light-dark(#a8322f, #ff6b6b);
  --pal-green: light-dark(#4a7a3a, #7fbf7a);
  --pal-yellow: light-dark(#8a6d1f, #e0b45a);
  --pal-blue: light-dark(#3e5f8c, #7ea4d8);
  --pal-purple: light-dark(#6b4f8a, #b98cd8);
  --pal-aqua: light-dark(#2f7a78, #66c2b8);
  --pal-accent: light-dark(#8a6d1f, #e0334f);
  --pal-accent-strong: light-dark(#6b5314, #ff5c73);
  --pal-on-accent: light-dark(#fffdf7, #0b0708);
  --pal-shadow-1: light-dark(rgb(138 109 31 / 0.14), transparent);
  --pal-shadow-2: light-dark(rgb(138 109 31 / 0.26), transparent);
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace. Cormorant Garamond and Inter are
licensed under the SIL Open Font License by their authors.
