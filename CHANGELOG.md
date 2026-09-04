# 0.1.0 Unreleased

## Features

* **The `plain` template.** The reference implementation of the template contract: an overview, a blog post built from the shared markdown fixture, a forms page built from the shared form fixture, a sidebar-layout variant, a 22-page docs tree (get started, tokens, defaults, blog anatomy, and one page per component with a live preview, copyable markup, variants, classes and notes), and a three-page example site. Two stylesheets, one 45-line script for the tri-state light/dark toggle, and a one-line `onclick` on dialog openers; everything else is HTML and CSS. Its palette block is a retoken theme.

* **The landing page.** `index.html` lists every template with a hand-drawn preview per scheme, a title search and tag filters (scheme, type, motion, fonts, feel) that combine, and links to each template's overview, docs and example site.

* **The `neumorphic` template.** Soft UI on a single surface: every card, button and field is pushed out of, or pressed into, the page colour by a pair of light and dark shadows, with no borders anywhere but a banner's coloured edge. Buttons and the feature card press in on click; inputs and the switch track are sunken. Cool grey with white highlights by day, charcoal by night; Nunito from Google Fonts. Example site: a smart-home dashboard.

* **The `brutal-news` template.** A brutalist newspaper: white paper and black ink, rules never thinner than three pixels, no rounded corners, hard offset shadows, and a harsh set of hues at full strength (hot red, acid yellow, cobalt, signal green). Archivo Black headlines, Inter body, JetBrains Mono kickers and data, all from Google Fonts. Flare: a masthead with dateline, ruled columns with a drop cap, tape, a ruled box and a red block. Dark mode prints the same paper in reverse. Example site: a local newspaper.

* **The `glassy` template.** Glassmorphism: a soft gradient backdrop built from three colour tokens, two blurred colour orbs drifting behind the page, and every card, bar, panel and dialog a translucent sheet with a bright edge and a backdrop blur. Pill buttons, large radii, a strip of four wave layers on a slow parallax that stops under reduced motion, system fonts. Example site: a small design studio.

## Bug Fixes


## Other

* **Structural checker and fixtures.** `tools/check.py` (Python, standard library only) enforces the template contract: required files, the head block, relative links, the retoken token rules with contrast maths, fixture and snippet parity, navigation consistency and the JavaScript allow-list. `fixtures/` holds the canonical markdown test article and form that every template embeds verbatim.
