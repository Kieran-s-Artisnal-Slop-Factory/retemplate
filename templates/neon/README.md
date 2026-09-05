# Neon

Signage at night. A flat dark field, hairline borders at 10 to 15 percent
white, and two neon tubes: rose for what matters, cyan for what is merely
true. Glow means state: a lit thing is on, an unlit one is off. Both
schemes are dark: light is zinc (`#18181b`), dark is black (`#141414`),
and the text stays off-white in each, so the tubes keep working and
nothing is ever white. Headings in Space Grotesk, body in Inter. Part of
[retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page SaaS status site
(status board, pricing, changelog), and start from it.

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

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, and `@property` for the feature card's
  turning border. No polyfills.
- **Fonts:** Inter (body) and Space Grotesk (the sign, headings, labels),
  from Google Fonts by the `<link>` above. To self-host instead, download
  the two families from [Google Fonts](https://fonts.google.com/) (both are
  OFL), put the `woff2` files in a `fonts/` folder beside `css/`, add
  `@font-face` rules at the top of `css/global.css` pointing at
  `../fonts/…`, and drop the three lines above. `theme.css` already names
  the families with a system fallback, so the page reads while they load or
  if they never do.
- **Script:** `js/theme.js` (the scheme toggle, about 45 lines) and a
  one-line `onclick` on dialog openers. Under a strict CSP, move those calls
  into a script of your own.
- **Native controls:** both halves are dark, so `global.css` pins `select`,
  `input`, `textarea`, `dialog` and open popovers to `color-scheme: dark`
  and sets `scrollbar-color` on `:root`. The browser never paints a white
  dropdown, date picker or scrollbar; inside those elements the palette
  resolves to its black half in either scheme, so a form field is always a
  black well, one step deeper than the zinc page around it in light.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

The signature is the sign: `.neon-text` turns a headline into tube
lettering, `.neon-strike` makes it strike once on load, and `.neon-stage`
on a `.hero` sets it very large with no picture. Around it, under the same
rule (glow is state):

- `.neon-marquee`: a lit heading strip of short caps items.
- `.neon-rail` / `.neon-rail-current`: a dated list on a tube; the current
  entry's lamp is lit.
- `.neon-sign` / `.neon-sign-cyan`: a lit pill label.
- `.neon-glow` / `.neon-glow-cyan`: the glow shadow on any block.
- `.card.neon-panel`, `.neon-panel-lit`, `.neon-panel-cyan`: the card as
  a switched sign; light one in a row.
- `.badge.neon-light` with `.badge-done`, `.badge-active`,
  `.neon-light-warn`, `.neon-light-cyan`: a state light; bare, it is off.
- `.data-table.neon-status`: the table as a status board.
- `.btn.neon-outline` / `.neon-outline-cyan`: an unfilled tube.

See `docs/components/flare.html` and the cards, badge, table and buttons
pages. Two things move, the strike once and the feature card's sweep on
hover, and both stop under `prefers-reduced-motion`. There is no ambient
animation.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Neon to
another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, remove the fonts `<link>` lines, and remove any `.neon-*` classes.
A rail or a marquee then reads as an ordinary list; a stage as an ordinary
hero.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="neon">`. Colours carry over, including
the zinc light half and the black dark half; the glows and the hairlines
are this template's own tokens and stay here.

```css
:root[data-theme='neon'],
[data-theme='neon'] {
  --pal-bg0: light-dark(#18181b, #141414);
  --pal-bg0-soft: light-dark(#1f1f23, #1a1a1a);
  --pal-bg1: light-dark(#26262b, #202020);
  --pal-bg2: light-dark(#343436, #2c2c2c);
  --pal-bg3: light-dark(#4b4b4d, #3d3d3d);
  --pal-fg: light-dark(#f4f4f5, #f2f2f2);
  --pal-fg-muted: light-dark(#a1a1aa, #a3a3a3);
  --pal-gray: light-dark(#71717a, #737373);
  --pal-red: light-dark(#f87171, #f87171);
  --pal-green: light-dark(#34d399, #34d399);
  --pal-yellow: light-dark(#fbbf24, #fbbf24);
  --pal-blue: light-dark(#22d3ee, #22d3ee);
  --pal-purple: light-dark(#a78bfa, #a78bfa);
  --pal-aqua: light-dark(#67e8f9, #67e8f9);
  --pal-accent: light-dark(#f43f5e, #f43f5e);
  --pal-accent-strong: light-dark(#fb7185, #fb7185);
  --pal-on-accent: light-dark(#18181b, #141414);
  --pal-shadow-1: light-dark(rgb(0 0 0 / 0.5), rgb(0 0 0 / 0.6));
  --pal-shadow-2: light-dark(rgb(0 0 0 / 0.7), rgb(0 0 0 / 0.8));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace. The fonts are Google's under the SIL
Open Font License.
