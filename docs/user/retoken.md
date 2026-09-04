# Using a template's theme in retoken

*(Stub — finished in Phase 11.)*

Every template's palette is a [retoken](https://kieranwood.ca/retoken/theme/)
theme. To use one in a retoken site:

1. Open `templates/<name>/README.md` (or `docs/theme.html`) and copy the
   palette block — the `:root[data-theme='<name>'], [data-theme='<name>']`
   rule with the nineteen `--pal-*` slots.
2. Paste it into your retoken `src/styles/theme.css` after the existing
   palettes.
3. Select it: `<html data-theme="<name>">`, or pick it in retoken's theme
   editor, which discovers it from the stylesheet.

What is carried: colours. What is not: fonts, radii, spacing, layout widths
and the template's `--<name>-*` tokens — set those in retoken's editor.
