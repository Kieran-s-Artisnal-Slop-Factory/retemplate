# Glassy

Frosted glass over a soft gradient, composed by depth. Two blurred colour
orbs drift behind the page; every card, bar, panel and dialog is a
translucent sheet with a bright edge, at one of three depths; the hero is a
single deep sheet standing over a strip of four slow wave layers, and the
cards under it hang off its lower edge. Pill buttons, system fonts set light.
Airy blues by day, deep navy by night. Part of [retemplate](../../README.md).

## Take and use

Copy this folder. Keep the **install set**: `css/`, `js/theme.js`,
`assets/`, this file, and delete the **showcase**: `index.html`,
`blogpost.html`, `forms.html`, `sidebar.html`, `docs/`, `example/`,
`js/copy.js`. Or keep `example/`, a complete three-page site for a small design
studio, and start from it.

Put this at the top of every page (adjust the paths for sub-folders):

```html
<!doctype html>
<html lang="en" data-theme="glassy">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>My page</title>
  <link rel="icon" href="assets/favicon.svg">
  <script src="js/theme.js"></script>
  <link rel="stylesheet" href="css/theme.css">
  <link rel="stylesheet" href="css/global.css">
</head>
```

Then write HTML with the classes in `docs/components/` (open
`docs/index.html` in a browser for the guided version).

- **Browsers:** Baseline 2024: `light-dark()`, `:has()`, popovers,
  `<details name>`, `color-mix()`, `backdrop-filter`. No polyfills.
- **Fonts:** none. Glassy uses the system font stacks, set light at the two
  large sizes.
- **Script:** `js/theme.js` (the theme toggle, ~45 lines) and a one-line
  `onclick` on dialog openers. Under a strict CSP, move those calls into a
  script of your own.
- **Delete these:** each showcase page has an
  `<a class="site-link" href="../../index.html">` back to the retemplate
  landing; nothing else points outside the folder.

## Flare and variants

Markup flare, inside `<div class="glassy-flare">` wrappers: `.glassy-orbs`
(put it right after `<body>`) and `.glassy-waves` (a strip; one per page,
since it defines an SVG id, and meant to follow a sheet hero). Both
animations stop under `prefers-reduced-motion`.

Composition classes, no wrapper needed (another template ignores them):
`.hero.glassy-sheet` (the hero as one deep sheet over the waves),
`.glassy-shallow` / `.glassy-deep` (depth tiers on any glass component),
`.glassy-float` (pull a block up over the one before it), `.glassy-pane`
(a section-sized sheet), `.glassy-stack` (panels laid over one another in
order). Component variants: `.btn.glassy-ghost`, `.banner.glassy-frost`,
`.table-wrap.glassy-price` with `tr.glassy-total`,
`.fifty-fifty.glassy-overlap`, `.navbar.glassy-floating`. All documented on
`docs/components/flare.html` and the component pages it points to.

## Swapping templates

Every retemplate template uses the same markup. To move a site from Glassy
to another template, replace `css/` and `assets/`, change `data-theme` on
`<html>`, and remove the `<div class="glassy-flare">` wrappers.

## Using the theme in retoken

The palette block below is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. Paste it into a retoken site's `theme.css` after the existing palettes
and select it with `<html data-theme="glassy">`. Colours carry over; the
gradient, the glass and the waves are this template's own tokens and stay
here.

```css
:root[data-theme='glassy'],
[data-theme='glassy'] {
  --pal-bg0: light-dark(#eef1fb, #141727);
  --pal-bg0-soft: light-dark(#ffffff, #1c2036);
  --pal-bg1: light-dark(#f5f7fd, #232845);
  --pal-bg2: light-dark(#d9deef, #313866);
  --pal-bg3: light-dark(#b9c2df, #46508a);
  --pal-fg: light-dark(#1f2a44, #eef0fb);
  --pal-fg-muted: light-dark(#526285, #aab3d6);
  --pal-gray: light-dark(#8a97b3, #7d86ab);
  --pal-red: light-dark(#d64545, #ff7b7b);
  --pal-green: light-dark(#2e9e5b, #5fd38d);
  --pal-yellow: light-dark(#b8801a, #f0c05a);
  --pal-blue: light-dark(#2f6fdb, #7ea2ff);
  --pal-purple: light-dark(#7a5af5, #b39cff);
  --pal-aqua: light-dark(#1f9fb3, #5fd4e8);
  --pal-accent: light-dark(#3556c9, #8ea6ff);
  --pal-accent-strong: light-dark(#2a44a3, #a9bbff);
  --pal-on-accent: light-dark(#ffffff, #0f1330);
  --pal-shadow-1: light-dark(rgb(31 42 68 / 0.12), rgb(0 0 0 / 0.45));
  --pal-shadow-2: light-dark(rgb(31 42 68 / 0.22), rgb(0 0 0 / 0.6));
}
```

## Licence

MIT, like the rest of retemplate. The placeholder art in `assets/` is
original and free to reuse or replace.
