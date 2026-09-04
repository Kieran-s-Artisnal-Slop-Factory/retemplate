# Markdown test document

This document exercises every construct a blog post is likely to use. It is
the source of `markdown-test.html`, which is the same content hand-rendered
to HTML; every template's `blogpost.html` embeds that rendered fragment
verbatim, so if you change one you change all three. It borrows the shape
of [mxstbr's markdown-test-file](https://github.com/mxstbr/markdown-test-file)
and adds the things that file leaves out (tables, images, task lists,
footnotes, definition lists).

## Headings

The line above is a level-two heading. Below are the remaining levels.

### A third-level heading

#### A fourth-level heading

##### A fifth-level heading

###### A sixth-level heading, which is as deep as it goes

## Paragraphs and inline text

Paragraphs are separated by a blank line. A single newline inside a paragraph
does nothing; two trailing spaces  
force a hard line break like the one before this clause.

Text can be *emphasised* or **strong** or ***both***; it can be
~~struck through~~, and it can hold `inline code` such as `printf()` or
`<br>`. Abbreviations get an <abbr title="HyperText Markup Language">HTML</abbr>
tag, keyboard input a <kbd>Ctrl</kbd> + <kbd>K</kbd> pair, a highlight uses
<mark>mark</mark>, and chemistry needs H<sub>2</sub>O while footnotes need a
superscript.[^1]

Links come in three kinds: an [inline link](https://example.com "with a title"),
a [reference-style link][ref], and a bare URL such as <https://example.org>.

[ref]: https://example.com/reference

## Lists

An unordered list:

- Apples
- Pears
  - A nested item
  - Another nested item, with *emphasis*
- Plums

An ordered list, whose numbers do not have to be in order in the source:

1. First
1. Second
1. Third, with a paragraph of its own.

   This paragraph belongs to the third item.

   ```python
   print("and so does this code block")
   ```

A task list:

- [x] Write the fixture
- [ ] Embed it in every template
- [ ] Never edit the copies by hand

## Blockquotes

> A blockquote can hold several paragraphs.
>
> It can also hold a list:
>
> - one
> - two
>
> > And it can nest another quote, with a heading inside:
> >
> > ### Quoted heading
> >
> > Which is unusual but legal.

## Code

Fenced code with a language:

```js
export function greet(name = "world") {
  return `Hello, ${name}!`;
}
```

Fenced code in a second language, with a long line to test overflow:

```css
.card { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: var(--space-3); padding: var(--space-4); border: 1px solid var(--border-color); }
```

Indented code, four spaces:

    $ python tools/check.py --template plain
    checked templates/plain: 0 error(s), 0 warning(s)

## Tables

| Component   | Element      | Needs JS |
| :---------- | :----------: | -------: |
| Accordion   | `<details>`  |       no |
| Dialog      | `<dialog>`   | one line |
| Lightbox    | `<dialog>`   | one line |
| Switch      | `<input>`    |       no |

The first column is left-aligned, the second centred, the third right-aligned.

## Images

![A placeholder landscape](assets/fixture-photo-1.svg "The first fixture image")

Images can also sit inline in a paragraph, like this small one:
![A second placeholder](assets/fixture-photo-2.svg "The second fixture image")
which the stylesheet should keep from breaking the line height too badly.

## Horizontal rule

The line below is a thematic break.

---

## Definition list

Markdown has no syntax for these, so they are written as HTML:

<dl>
  <dt>Token</dt>
  <dd>A named value in <code>theme.css</code> that components reference instead of a literal.</dd>
  <dt>Palette slot</dt>
  <dd>One of the nineteen <code>--pal-*</code> tokens a retoken theme fills in.</dd>
</dl>

## Details

<details>
  <summary>A collapsed section</summary>
  <p>This paragraph is hidden until the summary is clicked. It uses the browser's native disclosure, so it needs no script.</p>
</details>

## Footnotes

The footnote referenced near the top of the page is rendered at the end.[^2]

[^1]: This is the first footnote. It can be a full sentence.
[^2]: The second footnote has two paragraphs.

    This is the second paragraph of the second footnote.
