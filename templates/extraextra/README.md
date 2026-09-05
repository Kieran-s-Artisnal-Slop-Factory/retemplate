# ExtraExtra

A poster wall. Warm paper and near-black type by day, near-black and paper
by night, and one bright orange that never changes and only ever carries
black type. No maximum page width: sections are ruled off edge to edge with
2px lines in the type colour, and full-bleed bands in orange or ink cut
across the page. Anton in capitals for every heading, brand, button and
badge; Barlow for the body; IBM Plex Mono for kickers, labels and data.
No corners, no shadows. The signature is a ticker, an ink strip of mono
facts moving under the hero. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page site for a music
venue (home, line-up, tickets), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="extraextra">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:ital,wght@0,400;0,500;0,700;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `mix-blend-mode`. No polyfills.
- **Fonts:** Anton (display), Barlow (body) and IBM Plex Mono (data), all
  OFL, loaded from Google Fonts by the three `<link>`s above. Without them
  the fallback stacks in `theme.css` give Impact or Arial Narrow Bold for
  the display, Helvetica or Arial for the body and the system mono for the
  rest; the bands and rules carry the look on their own. To self-host,
  download the three families, put the files in `fonts/`, add
  `@font-face` rules at the top of `css/global.css` (not `theme.css`,
  whose palette block is pasted elsewhere) and drop the three `<link>`s.
  Anton has one weight and no italic; the stylesheet never asks it for
  either.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog and lightbox openers. Under a strict CSP,
  move those calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.extraextra-band` on a section: a full-bleed orange band with black
  type. A `.fifty-fifty` inside it drops its own box
  (`docs/components/fifty-fifty.html`).
- `.extraextra-band-ink` on a section: the page in reverse, ink ground and
  paper type; in the dark scheme, the one pale band on a black page.
- `.extraextra-ticker`: the moving strip of mono facts, two copies of one
  `<p>` so the loop has no gap. It pauses on hover and focus and stops
  under `prefers-reduced-motion`.
- `.card.extraextra-poster`: a card with no box, a ten-pixel ink bar on
  top and the title a size up (`docs/components/cards.html`).
- `.btn.extraextra-shout`: a button in display capitals at heading size,
  for the one call on a page (`docs/components/buttons.html`).
- `.table-wrap.extraextra-times`: the set-times board, mono figures with
  the first column in capitals (`docs/components/table.html`).
- `.banner.extraextra-strip`: a full-bleed ink notice with an orange
  label (`docs/components/banner.html`).

Markup that is only flare sits inside `<div class="extraextra-flare">`
wrappers. The ticker is the only thing that moves on its own; the feature
card's two-colour print and the accordion marker are transitions the
global `prefers-reduced-motion` rule shortens to nothing.

The bands cancel the page gutter with a negative margin, so they belong
directly inside `main.page`. The orange is one token, `--extraextra-orange`,
the same in both schemes, with `--extraextra-on-orange` for the black type
on it; the rule and bar weights are `--extraextra-rule` (2px) and
`--extraextra-bar` (10px); the gutter is `--extraextra-gutter`. All of them
live in `theme.css`.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
ExtraExtra to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, remove the fonts `<link>`s, remove the
`<div class="extraextra-flare">` wrappers, and drop the `extraextra-*`
classes (the elements that carried them stay valid without them; a band
becomes an ordinary section).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="extraextra">`. Colours carry
over; the fonts, the bands, the bar weights and the ticker are this
template's own tokens and stay here. The light accent is a burnt orange,
`#a63a00`, because the bright orange fails 4.5:1 on paper as a text
colour; on black it passes, so the dark accent is the bright orange
itself. The border slot (`--pal-bg2`) is the ink, so retoken's own
components rule in the same weight.

```css
:root[data-theme='extraextra'],
[data-theme='extraextra'] {
  --pal-bg0: light-dark(#f3eee4, #0d0c0b);
  --pal-bg0-soft: light-dark(#faf7f0, #141312);
  --pal-bg1: light-dark(#e8e1d2, #1e1c19);
  --pal-bg2: light-dark(#141312, #f3eee4);
  --pal-bg3: light-dark(#8a8378, #5a554e);

  --pal-fg: light-dark(#141312, #f3eee4);
  --pal-fg-muted: light-dark(#4d4741, #b8b0a4);
  --pal-gray: light-dark(#7a736a, #857d73);

  --pal-red: light-dark(#c8102e, #ff5c5c);
  --pal-green: light-dark(#1f6f3a, #4fc26b);
  --pal-yellow: light-dark(#8a5a00, #ffc466);
  --pal-blue: light-dark(#1f4fa3, #7fa8ff);
  --pal-purple: light-dark(#6b3fa0, #b48cff);
  --pal-aqua: light-dark(#0b6e73, #4fd0d6);

  --pal-accent: light-dark(#a63a00, #ff6a00);
  --pal-accent-strong: light-dark(#7d2b00, #ff8a3d);
  --pal-on-accent: light-dark(#fff8f0, #0d0c0b);

  --pal-shadow-1: light-dark(rgb(20 19 18 / 0), rgb(0 0 0 / 0));
  --pal-shadow-2: light-dark(rgb(20 19 18 / 0), rgb(0 0 0 / 0));
}
```

## Licence

MIT, like the rest of retemplate. The poster art in `assets/` is original
and free to reuse or replace. Anton, Barlow and IBM Plex Mono are licensed
under the SIL Open Font License by their authors.
