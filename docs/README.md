# Retemplate documentation

Re-usable HTML + CSS templates and themes: take a folder, use it. No build
step, no framework. Every template is also a retoken theme.

## For users

- [Using a template](user/using-a-template.md): copy the folder, keep the
  install set, paste the head block, write HTML.
- [Using a template's theme in retoken](user/retoken.md): the palette block
  and where it goes.
- Each template's own docs: `templates/<name>/docs/index.html` (get started,
  theme, defaults, blog anatomy, one page per component).

## For developers

- [The template contract](dev/template-contract.md): what every template
  must contain and how it is checked.
- [Testing](dev/testing.md): `tools/check.py` and the visual pass.
- [Adding a template](dev/adding-a-template.md): copy plain, re-skin, make
  it distinct, check.
- Plans: [TODO](dev/plans/TODO), [version 0.1.0 phased plan](dev/plans/version-0.1.0-phased.md).
