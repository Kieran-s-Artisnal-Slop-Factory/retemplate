# 0.1.0 Unreleased

## Features

* **The `plain` template.** The reference implementation of the template contract: an overview, a blog post built from the shared markdown fixture, a forms page built from the shared form fixture, a sidebar-layout variant, a 22-page docs tree (get started, tokens, defaults, blog anatomy, and one page per component with a live preview, copyable markup, variants, classes and notes), and a three-page example site. Two stylesheets, one 45-line script for the tri-state light/dark toggle, and a one-line `onclick` on dialog openers; everything else is HTML and CSS. Its palette block is a retoken theme.

* **The landing page.** `index.html` lists every template with a hand-drawn preview per scheme, a title search and tag filters (scheme, type, motion, fonts, feel) that combine, and links to each template's overview, docs and example site.

## Bug Fixes


## Other

* **Structural checker and fixtures.** `tools/check.py` (Python, standard library only) enforces the template contract: required files, the head block, relative links, the retoken token rules with contrast maths, fixture and snippet parity, navigation consistency and the JavaScript allow-list. `fixtures/` holds the canonical markdown test article and form that every template embeds verbatim.
