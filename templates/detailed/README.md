# Detailed

Art deco. Cream and black ink with a bronze accent by day; deep navy with
gold by night. The navbar, the top bar, the footer and the lightbox are black
bands in both halves, because brass belongs on black. Rays fan down from the
top of every page; corners are cut in steps with one `clip-path`; the page
break is a pair of gold chevrons; the feature card wears a stepped gold
frame and a sheen of gold leaf sweeps across it once when you rest on it.
Limelight over the door, Josefin Sans capitals for kickers and navigation,
Jost for the body. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set** (`css/`, `js/theme.js`,
`assets/`, this file) and delete the **showcase** (`index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`). Or keep `example/`, a complete three-page hotel site called
The Marlowe, and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="detailed">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Limelight&family=Josefin+Sans:wght@400;600;700&family=Jost:ital,wght@0,300;0,400;0,500;1,400&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `clip-path`, `mask-image`. No polyfills.
- **Fonts:** Limelight (the h1 and the masthead), Josefin Sans (kickers,
  navigation, small capitals) and Jost (body), all OFL, loaded from Google
  Fonts by the three `<link>`s above. Without them the fallback stacks in
  `theme.css` are Copperplate or Futura and Century Gothic. To self-host,
  download the three families, put the files in `fonts/`, add `@font-face`
  rules at the top of `css/global.css` (not `theme.css`, whose palette block
  is pasted elsewhere) and drop the three `<link>`s.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog and lightbox openers. Under a strict CSP, move
  those calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html` and on the pages of the
components they dress. Everything is prefixed `detailed-` so it is easy to
find and easy to strip.

- `.hero.detailed-marquee`: the hero as a name over a door. One centred
  column, Limelight at its largest, a single call, and a `.detailed-sunburst`
  child (an inline SVG) rising behind the heading.
- `.card.detailed-stepped`: top corners cut in two steps with a gold
  hairline following the cut; the title in Limelight.
- `.btn.detailed-outline`: a double gold outline that fills gold on hover.
- `.table-wrap.detailed-menu`: a data table set like a bill of fare, with
  `tr.detailed-course` for course headings.
- `.detailed-frame` with `.detailed-frame-title`: a stepped panel with a
  double gold rule and a bronze title plate.
- `.detailed-chevron`: the page-break ornament as a free-standing block.

Markup for flare sits inside `<div class="detailed-flare">` wrappers. Nothing
animates continuously; the only motion is the sheen on the feature card,
which runs once per hover and is removed under `prefers-reduced-motion`.
The rays behind every page are `--detailed-rays` and `--detailed-rays-fade`,
layered on `body`; remove the `background-image` line in `global.css` to
lose them.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Detailed
to another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>`s, remove the `<div class="detailed-flare">`
wrappers, and drop any `detailed-*` class. The base classes underneath them
(`.card`, `.btn`, `.table-wrap`, `.hero`) keep working.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="detailed">`. Colours carry over; the
fonts, the gold, the rays, the steps and the sheen are this template's own
tokens and stay here.

```css
:root[data-theme='detailed'],
[data-theme='detailed'] {
  --pal-bg0: light-dark(#f3ead8, #0d1220);
  --pal-bg0-soft: light-dark(#faf5e8, #131a2c);
  --pal-bg1: light-dark(#eadfc6, #1a2238);
  --pal-bg2: light-dark(#d3c39c, #34405c);
  --pal-bg3: light-dark(#b8a374, #4d5878);

  --pal-fg: light-dark(#14121a, #efe6d2);
  --pal-fg-muted: light-dark(#5c5142, #b9ae94);
  --pal-gray: light-dark(#8a7d66, #7f8699);

  --pal-red: light-dark(#a3342a, #e08a7a);
  --pal-green: light-dark(#3f6b3a, #9cc98a);
  --pal-yellow: light-dark(#8a6414, #e2c46b);
  --pal-blue: light-dark(#2f5375, #8fb0dc);
  --pal-purple: light-dark(#5f4270, #b79ad0);
  --pal-aqua: light-dark(#2b6a66, #8dc7c0);

  --pal-accent: light-dark(#7a5a12, #d4af37);
  --pal-accent-strong: light-dark(#5c4309, #e8c65a);
  --pal-on-accent: light-dark(#f3ead8, #0d1220);

  --pal-shadow-1: light-dark(rgb(20 18 26 / 0.12), rgb(0 0 0 / 0.5));
  --pal-shadow-2: light-dark(rgb(20 18 26 / 0.22), rgb(0 0 0 / 0.65));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace. Limelight, Josefin Sans and Jost are
licensed under the SIL Open Font License by their authors.
