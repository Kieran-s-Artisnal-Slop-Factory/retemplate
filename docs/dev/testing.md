# Testing

There is no test suite in the JavaScript sense: the templates contain
almost no JavaScript, and what a template *is* — a design — is judged by
eye. What can be checked by a script is checked by one script, and what
cannot is a short visual pass at every checkpoint.

## `tools/check.py`

Python 3.10+, standard library only. No install step.

```bash
python tools/check.py                    # every template + landing + fixtures + bookkeeping
python tools/check.py --template neon    # one template
python tools/check.py --list             # the contract file list
```

Output is `path:line: error|warning: message`, sorted by file, then a count.
Exit status is 1 when any error was reported; warnings never fail the run.

| Check | What it asserts | Scope |
| --- | --- | --- |
| structure | every contract file exists; `example/` is `index.html` + exactly two pages; `css/` and `js/` hold only their contract files; `assets/` holds images and the three fixture images; no stray files or folders at the template root | template |
| head | doctype; `html[lang=en][data-theme=<name>]`; charset, viewport and color-scheme metas; a title; the favicon link; `theme.js` as a plain synchronous script before the stylesheets; `theme.css` then `global.css`; no external `<link>` except Google Fonts | every page |
| overview | `index.html` uses every component (the list in the contract §4) | `index.html` |
| links | every `href`, `src`, `srcset`, `poster`, `data` and CSS `url()` is relative, resolves to a file, is not a directory, stays inside the folder (except `.site-link`), loads nothing external except the fonts link; install-set files reference only `css/`, `assets/`, `fonts/` | every page + both stylesheets |
| js | only `js/theme.js` and `js/copy.js`; no inline script content; the only handler attribute is `onclick="…showModal()"` | every page |
| tokens | `theme.css`: the `:root, .themed` block with every mapping name, every shared token and the four retemplate tokens; the palette block in the named form with exactly the 19 slots as `light-dark()` pairs; no `--pal-*` anywhere else; no bare `:root` palette; no colour literal outside the palette and `--<name>-*` tokens; contrast of the three gating pairs in both halves (others reported). `global.css`: no colour literal, no `--pal-*` reference; `light-dark()` reported; `prefers-reduced-motion` present | both stylesheets |
| fixtures | the `[data-fixture]` subtree in `blogpost.html` and `forms.html` equals the fixture's, normalised | two pages |
| snippets | every `data-snippet` example/code pair on a docs page matches (same-page, or by `data-source` + `data-select`); the `palette` snippet and the README's ```css fence equal the palette block | docs pages, README |
| nav | every sidebar page carries the same link set, covering every contract page, with `aria-current` on its own link and the `site-link`; the three navbar pages share a link set and carry the scheme toggle and the `site-link`; example pages link back to the overview | sidebar + navbar pages |
| component pages | each component page shows its component (or an iframe for page-level ones) and has a snippet | docs/components |
| contract | every instance of a contract component (navbar, sidebar, footer, card, fifty-fifty, gallery, lightbox, accordion, switch, dialog, author card, field, banner, table-wrap) has a skeleton — tags, non-flare classes, `name`/`role`/`popover`/`popovertarget`/`type`/`data-*` — that `plain` also has; `.<name>-flare` subtrees and `.<name>-*` classes are ignored, and content slots (card bodies, accordion bodies, banners, fields, footer columns, inline `<svg>` drawings such as `.card-icon`) are compared by their root element only | every template except plain |
| landing | a card per template folder; tags from the vocabulary with one per group; both previews present; a row per template in `templates/README.md`; the landing's own head, links and scripts | unfiltered runs |
| fixtures pages | the two fixture pages parse, link cleanly and carry a `[data-fixture]` element | unfiltered runs |
| bookkeeping | `CHANGELOG.md`'s first heading names the `VERSION` | unfiltered runs, warning |

What the checker cannot see: whether it looks right. That is the visual
pass.

## The visual pass

Done at every checkpoint (and, for a single template, when it is declared
done). Serve the repo — `python -m http.server 8080` from the repo root, or
open the files directly — and look at, for each template:

`index.html`, `blogpost.html`, `forms.html`, `sidebar.html`,
`docs/index.html`, `docs/components/cards.html`, `docs/theme.html`,
`example/index.html`

…each in **both schemes** (use the toggle; the third click returns to
auto) at a **desktop width** and a **phone width** (about 375px). Check:

- Nothing overflows horizontally; text is readable in both halves.
- The scheme toggle flips everything, including native controls and the
  scrollbar, and the choice survives a reload.
- Accordion opens; exclusive groups close their siblings.
- Lightbox opens from a thumbnail, prev/next move, ESC and the close
  button close it.
- Dialog opens and closes; the mobile nav and the sidebar drawer open,
  close on ESC, and close when clicking outside.
- The docs copy button copies.
- The fonts load (if the template links any) and the fallback stack is
  acceptable with the network blocked.

Anything that needs a human judgement (taste, a contrast warning the
checker reported, an animation) goes in the TODO's **For human** list.

## Checkpoints

A checkpoint is: the unfiltered checker green, the visual pass done for
everything new since the last checkpoint, the Progress table in
`docs/dev/plans/version-0.1.0-phased.md` updated, and any accepted contract
gaps applied to `plain` and to every built template before the next batch
starts.

## Deploying

`.github/workflows/pages.yml` runs the checker and, if it passes, publishes
the repository root to GitHub Pages. There is nothing to build.
