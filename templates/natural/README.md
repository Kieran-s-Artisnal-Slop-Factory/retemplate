# Natural

Cream paper, ink, rust and moss. Fraunces for the headings, Source Sans 3
for everything else, hairline rules, uppercase tracked kickers, and a faint
green tint in the corner of the page. The page opens on a herbarium plate:
a mounted specimen with its label glued over one corner. At night the paper gives way to soil:
a tiled SVG noise texture under everything, with cream and light-green text
on top. The feature card is a pressed-flower specimen whose paper tag lifts
when you hover. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** (`css/`, `js/theme.js`,
`assets/`, this file) and delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page plant-nursery site,
and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="natural">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `mask-image`. No polyfills.
- **Fonts:** Fraunces (display) and Source Sans 3 (body), both OFL, loaded
  from Google Fonts by the three `<link>`s above. Without them the fallback
  stacks in `theme.css` are Palatino/Georgia and Segoe UI/Helvetica. To
  self-host, download the two families, put the files in `fonts/`, add
  `@font-face` rules at the top of `css/global.css` (not `theme.css`, whose
  palette block is pasted elsewhere) and drop the three `<link>`s.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Everything Natural adds beyond the shared contract comes out of a herbarium
cupboard, and all of it is documented on `docs/components/flare.html`:

- `.natural-plate`, the signature: a mounted sheet held down by two strips
  of tape, with a `.natural-label` glued over its corner carrying a
  `.natural-binomial` (Latin name, authority in `.natural-auth`) and a
  `.natural-data` list. It is the hero of the overview and of both example
  entries.
- `.natural-tag` (a paper tag with a punched hole), `.natural-note` (a page
  from the collecting book, ruled with a rust margin), `.natural-stamp` (a
  round nursery seal) and `.natural-sprig` (the page-break ornament as a
  block). Markup for these sits inside `<div class="natural-flare">`
  wrappers so a template swap can strip it.
- Five variants of contract components, each one extra class on the
  ordinary markup and documented on that component's page:
  `.card.natural-specimen` (a mounted specimen with a label for a body),
  `.accordion-group.natural-key` (a dichotomous key with numbered
  couplets), `.table-wrap.natural-calendar` (a planting calendar, a dot per
  month, with `.natural-legend`), `.fifty-fifty.natural-spread` (a plate
  beside its notes) and `.btn.natural-stamp` (a rubber-stamp button).

Nothing animates continuously; the only motion is the tag on the feature
card, which the global `prefers-reduced-motion` rule shortens to nothing.

The soil texture and the corner tint are `--natural-*` tokens layered on
`<body>`. The texture is a fine, faint grain; it is covered by a
`light-dark(var(--pal-bg0), transparent)` gradient, so it shows only in the
dark half. Remove `background-image` from `body` in `global.css` to lose
both.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Natural
to another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>`s, and remove the
`<div class="natural-flare">` wrappers.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="natural">`. Colours carry over; the
fonts, the soil texture, the sprig and the specimen tag are this template's
own tokens and stay here.

```css
:root[data-theme='natural'],
[data-theme='natural'] {
  --pal-bg0: light-dark(#ece7d6, #1c150f);
  --pal-bg0-soft: light-dark(#f5f1e4, #261e16);
  --pal-bg1: light-dark(#e3ddc9, #2f261c);
  --pal-bg2: light-dark(#c6c0a8, #47392a);
  --pal-bg3: light-dark(#a89f84, #5f4e3a);
  --pal-fg: light-dark(#2e2519, #ece7d6);
  --pal-fg-muted: light-dark(#6b6450, #b9c9a0);
  --pal-gray: light-dark(#8c8470, #8a7f6b);
  --pal-red: light-dark(#9c2f2f, #d98a74);
  --pal-green: light-dark(#4d6b38, #9fbf7a);
  --pal-yellow: light-dark(#8a6414, #d9b866);
  --pal-blue: light-dark(#3f5f7a, #8fa9bf);
  --pal-purple: light-dark(#6e4f7a, #b39ab8);
  --pal-aqua: light-dark(#2f6f68, #8fbcb2);
  --pal-accent: light-dark(#a33b2a, #e2cf9c);
  --pal-accent-strong: light-dark(#7f2c1f, #f0e2b8);
  --pal-on-accent: light-dark(#f5f1e4, #1c150f);
  --pal-shadow-1: light-dark(rgb(46 37 25 / 0.10), rgb(0 0 0 / 0.45));
  --pal-shadow-2: light-dark(rgb(46 37 25 / 0.18), rgb(0 0 0 / 0.6));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace. Fraunces and Source Sans 3 are
licensed under the SIL Open Font License by their authors.
