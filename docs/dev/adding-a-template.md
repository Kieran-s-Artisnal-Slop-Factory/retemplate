# Adding a template

The contract is in [template-contract.md](template-contract.md); `plain` is
its reference implementation. A new template is a copy of `plain` re-skinned.

1. Copy `templates/plain` to `templates/<name>` (lowercase, hyphens).
2. Replace every `data-theme="plain"` with `data-theme="<name>"` and rewrite
   the palette block's selector in `css/theme.css` to the new name.
3. Re-skin `css/theme.css` (palette, shared token values, `--<name>-*`
   tokens) and `css/global.css`. Keep every class name; add flare as
   `.<name>-*` inside `<div class="<name>-flare">` when it needs markup.
4. If the design needs fonts, add the Google Fonts `<link>` to the showcase
   pages and the family names to `theme.css` with fallbacks.
5. Replace `assets/` art. Keep `favicon.svg`, `avatar.svg`,
   `fixture-photo-1.svg`, `fixture-photo-2.svg` by name.
6. Rewrite the copy of `index.html`, `sidebar.html`, `docs/index.html`,
   `docs/components/flare.html` and the three `example/` pages. Leave the
   fixture fragments in `blogpost.html` and `forms.html` untouched. The
   navbar and footer snippets on `docs/components/navbar.html` and
   `footer.html` are escaped copies of `index.html`'s markup (brand name,
   footer heading), so re-copy them after rewriting the overview or the
   snippet check fails.
7. Write `README.md` (install set, browsers, fonts, the palette block in a
   ```css fence).
8. `python tools/check.py --template <name>` until green.
9. Draw `landing/previews/<name>-light.svg` and `-dark.svg`; add the card to
   `index.html` and the row to `templates/README.md`.
10. CHANGELOG entry; TODO box; the visual pass in `testing.md`.

If `plain`'s markup cannot express something the design needs, do not work
around it in the copy: change `plain` and the contract, then propagate to
every template (`check.py`'s contract check will list the instances).
