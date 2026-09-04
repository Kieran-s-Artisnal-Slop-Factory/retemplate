# Fixtures

Canonical demo content that every template embeds **verbatim**. There is no
build step, so the copies are real copies; `python tools/check.py` compares
each template's copy to the file here and fails on any difference.

| File | Fragment | Embedded by |
| --- | --- | --- |
| `markdown-test.html` | `<article data-fixture="markdown-test">` | `templates/<name>/blogpost.html` |
| `forms.html` | `<form data-fixture="forms">` | `templates/<name>/forms.html` |
| `markdown-test.md` | — | nobody; it is the markdown source of the article, kept for humans |
| `assets/fixture-photo-1.svg`, `assets/fixture-photo-2.svg` | — | referenced by the article as `assets/…`, so every template ships the same file names in its own `assets/` |

Each `.html` here is also a complete page in the browser's default styling —
`markdown-test.html` is the "page with an example of rendered markdown text"
the TODO asks for, and the quickest way to see what a template's `.prose`
styling is up against.

## Editing a fixture

1. Edit the file here (and, for the article, keep `markdown-test.md` in step).
2. Paste the fragment into every template's page — the element carrying
   `data-fixture`, opening tag to closing tag.
3. Run `python tools/check.py`. It reports the first differing element per
   template.

What the comparison ignores: whitespace between elements and attribute order.
What it does not ignore: text, attribute values, element order.
