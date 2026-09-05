# Using a template's theme in retoken

Every template's palette is a [retoken](https://kieranwood.ca/retoken/theme/)
theme: a block of nineteen `--pal-*` colour slots in retoken's named-palette
form, each a `light-dark()` pair. Paste it into a retoken site and the
site takes the template's colours in both schemes.

## What to copy

The palette block, exactly as printed. It is in two places per template:

- `templates/<name>/README.md`, in the ```css fence near the end.
- `templates/<name>/docs/theme.html`, with a copy button.

Both are checked against `css/theme.css`, so they are always the current
values. It looks like this (Glassy's, abridged):

```css
:root[data-theme='glassy'],
[data-theme='glassy'] {
  --pal-bg0: light-dark(#eef1fb, #141727);
  --pal-fg: light-dark(#1f2a44, #eef0fb);
  --pal-accent: light-dark(#3556c9, #8ea6ff);
  /* … sixteen more slots … */
}
```

## Where to paste it

Into your retoken site's `src/styles/theme.css`, after the palettes that
are already there. The selector is the named form on purpose: a bare
`:root` block would tie with retoken's default palette and win by source
order, hijacking the site. The named form only applies when you select it.

## How to select it

Either set it on the document:

```html
<html data-theme="glassy">
```

or open retoken's theme editor, which discovers every named palette in the
stylesheet and lists it by name.

## What carries over, and what does not

Colours carry over. The three pairs that carry text (`--pal-fg` on
`--pal-bg0`, `--pal-accent` on `--pal-bg0`, `--pal-on-accent` on
`--pal-accent`) meet 4.5:1 in both schemes in every template; the checker
enforces it.

Fonts, radii, spacing, layout widths and the template's own `--<name>-*`
tokens (glows, textures, ornaments) stay in the template. Set fonts and
shape in retoken's editor if you want them to match; they are ordinary
shared tokens there.

## Going the other way

A retoken palette can be dropped into a template just as easily: replace
the palette block in `css/theme.css` with yours and change `data-theme` on
every page to your palette's name. Everything in `global.css` is written
against the tokens, never against literal colours, so the template restyles
itself.
