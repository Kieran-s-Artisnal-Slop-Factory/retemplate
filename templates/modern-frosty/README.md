# Modern Frosty

Near-white with a cast of ice by day, deep slate blue by night. Hairlines
instead of shadows, corners of 4px and 6px, one deep cold blue for links,
focus and the primary button. Frost (a translucent fill and an 8px blur)
appears only where something sits over the page: the sticky navbar and top
bar, dialogs, the lightbox controls, the mobile menu and the sidebar
drawer, and the note's toolbar. Geist for everything, Geist Mono for
labels. No gradients, no orbs, no motion beyond hover. Part of
[retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file. Delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, Sheaf, a complete three-page notes app
(home, features, pricing), and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="modern-frosty">
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
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `backdrop-filter`. No polyfills. Where
  `backdrop-filter` is missing the frosted surfaces keep their translucent
  fill and lose the blur.
- **Fonts:** Geist (body and headings) and Geist Mono (labels, badges,
  table heads, code), both OFL, loaded from Google Fonts by the three
  `<link>`s above. Without them the fallback stacks in `theme.css` give
  the system sans and the system mono. To self-host, download the two
  families, put the files in `fonts/`, add `@font-face` rules at the top
  of `css/global.css` (not `theme.css`, whose palette block is pasted
  elsewhere) and drop the three `<link>`s.
- **Script:** `js/theme.js` (the theme toggle, about 45 lines) and a
  one-line `onclick` on dialog and lightbox openers. Under a strict CSP,
  move those calls into a script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Documented on `docs/components/flare.html`:

- `.modern-frosty-note`: a note as the app draws it, a sticky frosted
  `.modern-frosty-toolbar` over a ruled `.modern-frosty-sheet`. Add
  `.modern-frosty-scroll` to cap it at 22rem and let it scroll, which is
  what gives the toolbar something to frost. The overview and the example
  home use one as the hero.
- `.modern-frosty-keys`: a wrapping list of keyboard shortcuts.

Variants of contract components, each additive and documented on that
component's page:

- `.grid-2.modern-frosty-ledger`, `.grid-3.modern-frosty-ledger`: cards
  that share their hairlines, one border around the set, no gaps
  (`docs/components/cards.html`).
- `.btn.modern-frosty-quiet`: text in the link colour, no border, ice on
  hover (`docs/components/buttons.html`).
- `.accordion-group.modern-frosty-lines`: the group without its box, only
  the rules between items (`docs/components/accordion.html`).
- `.field.modern-frosty-inline`: label left, control right, one ruled row
  (`docs/components/forms.html`).
- `.table-wrap.modern-frosty-plans` with `.modern-frosty-pick` on one
  column: a plans comparison with the prices in the last row
  (`docs/components/table.html`).

Markup that is only flare sits inside `<div class="modern-frosty-flare">`
wrappers. Nothing animates continuously; the only transitions are hover
colours and the feature card's frost clearing, both of which the global
`prefers-reduced-motion` rule shortens to nothing.

The frost is two tokens, `--modern-frosty-frost` (the fill) and
`--modern-frosty-blur` (8px); the hover tint is `--modern-frosty-ice` and
the note's lines are `--modern-frosty-rule`. All of them live in
`theme.css`, so lowering the blur or warming the ice is one edit.

## Swapping templates

Every retemplate template uses the same markup. To move a site from
Modern Frosty to another template, replace `css/` and `assets/`, change
`data-theme` on `<html>`, remove the fonts `<link>`s, remove the
`<div class="modern-frosty-flare">` wrappers, and drop the
`modern-frosty-*` classes (the elements that carried them stay valid
without them).

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing
palettes and select it with `<html data-theme="modern-frosty">`. Colours
carry over; the fonts, the frost and the note are this template's own
tokens and stay here. The light accent is `#1c5aa3` on `#f4f7fb`; the dark
accent turns to ice, `#8cc0f0` on `#0f1a27`, with near-black text on the
primary button. Both pairs clear 4.5:1.

```css
:root[data-theme='modern-frosty'],
[data-theme='modern-frosty'] {
  --pal-bg0: light-dark(#f4f7fb, #0f1a27);
  --pal-bg0-soft: light-dark(#ffffff, #152232);
  --pal-bg1: light-dark(#e9f0f7, #1b2b3d);
  --pal-bg2: light-dark(#d2dfeb, #2b3f55);
  --pal-bg3: light-dark(#a8bdd1, #42597a);

  --pal-fg: light-dark(#142130, #e7eef6);
  --pal-fg-muted: light-dark(#506478, #a2b4c8);
  --pal-gray: light-dark(#7f92a5, #6e829a);

  --pal-red: light-dark(#b42318, #f0857b);
  --pal-green: light-dark(#157347, #6fcf97);
  --pal-yellow: light-dark(#946200, #e4b85a);
  --pal-blue: light-dark(#2569b3, #8cc0f0);
  --pal-purple: light-dark(#5b4bc4, #b5a8f2);
  --pal-aqua: light-dark(#0f7b8a, #6ed2df);

  --pal-accent: light-dark(#1c5aa3, #8cc0f0);
  --pal-accent-strong: light-dark(#154a89, #b4d8f8);
  --pal-on-accent: light-dark(#ffffff, #0b1622);

  --pal-shadow-1: light-dark(rgb(20 33 48 / 0.06), rgb(0 0 0 / 0.45));
  --pal-shadow-2: light-dark(rgb(20 33 48 / 0.16), rgb(0 0 0 / 0.6));
}
```

## Licence

MIT, like the rest of retemplate. The drawings in `assets/` are original
and free to reuse or replace. Geist and Geist Mono are licensed under the
SIL Open Font License by Vercel.
