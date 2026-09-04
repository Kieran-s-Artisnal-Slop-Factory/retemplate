#!/usr/bin/env python3
"""retemplate structural checker.

Python 3.10+, standard library only. No third-party packages, no build step.

    python tools/check.py                # every template + the landing + fixtures
    python tools/check.py --template neon
    python tools/check.py --list         # print the contract file list and exit

Exits 1 when any error was reported. Warnings never fail the run.

What it checks is written up in docs/dev/testing.md; the rules it enforces
are the template contract in docs/dev/template-contract.md. Keep the three
in step: if a rule changes here, change the prose too.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
FIXTURES = ROOT / "fixtures"
LANDING = ROOT / "index.html"

# ---------------------------------------------------------------------------
# The contract, as data
# ---------------------------------------------------------------------------

COMPONENTS = [
    "accordion", "cards", "fifty-fifty", "gallery", "switch", "page-break",
    "buttons", "forms", "dialog", "navbar", "sidebar", "banner", "badge",
    "table", "author-card", "footer", "flare",
]

TOP_PAGES = ["index.html", "blogpost.html", "forms.html", "sidebar.html"]
DOCS_PAGES = ["docs/index.html", "docs/theme.html", "docs/defaults.html",
              "docs/blog.html", "docs/components/index.html"] + [
    f"docs/components/{c}.html" for c in COMPONENTS]
SIDEBAR_PAGES = ["sidebar.html"] + DOCS_PAGES
NAVBAR_PAGES = ["index.html", "blogpost.html", "forms.html"]

REQUIRED_FILES = TOP_PAGES + DOCS_PAGES + [
    "README.md", "css/theme.css", "css/global.css", "js/theme.js",
    "js/copy.js", "assets/favicon.svg", "example/index.html",
]

# Files a user keeps. Nothing in here may reference anything outside it.
INSTALL_SET_DIRS = ("css", "js/theme.js", "fonts", "assets")

# Everything index.html must use at least once ("ties the elements together").
OVERVIEW_MUST_USE = [
    ".card", ".card-horizontal", ".card-feature", ".fifty-fifty", ".gallery",
    ".lightbox", ".accordion", ".switch", "hr.page-break", "dialog.modal",
    ".banner", ".badge", ".data-table", ".btn", ".footer", ".navbar",
]

# What each component docs page must contain at least once.
COMPONENT_PAGE_MUST_CONTAIN = {
    "accordion": ".accordion", "cards": ".card", "fifty-fifty": ".fifty-fifty",
    "gallery": ".gallery", "switch": ".switch", "page-break": "hr.page-break",
    "buttons": ".btn", "forms": ".field", "dialog": "dialog.modal",
    "navbar": "iframe", "sidebar": "iframe", "banner": ".banner",
    "badge": ".badge", "table": ".data-table", "author-card": ".author-card",
    "footer": "iframe", "flare": None,
}

# Component selectors whose instances must match a shape plain defines.
CONTRACT_COMPONENTS = [
    "header.navbar", "aside.sidebar", "footer.footer", ".card", ".fifty-fifty",
    ".gallery", "dialog.lightbox", ".accordion-group", ".accordion", ".switch",
    "dialog.modal", ".author-card", ".field", ".banner", ".table-wrap",
]

# retoken's colour mapping (theme.css, `:root, .themed`), copied verbatim.
COLOR_MAPPING = [
    "--color-primary", "--color-primary-strong", "--color-primary-soft",
    "--color-on-primary", "--bg-color", "--surface-color",
    "--surface-raised-color", "--border-color", "--text-color",
    "--text-muted-color", "--color-success", "--color-success-soft",
    "--color-danger", "--color-danger-soft", "--color-warning",
    "--color-warning-soft", "--color-info", "--color-info-soft",
    "--editor-bg", "--editor-gutter-bg", "--editor-gutter-fg",
    "--editor-active-line", "--editor-selection", "--editor-cursor",
    "--editor-chrome-color", "--syntax-keyword", "--syntax-string",
    "--syntax-number", "--syntax-comment", "--syntax-type",
    "--syntax-operator", "--syntax-name", "--syntax-punctuation",
    "--editor-tooltip-bg", "--editor-tooltip-fg", "--editor-tooltip-border",
    "--editor-tooltip-selected-bg", "--editor-tooltip-selected-fg",
    "--editor-match-fg", "--shadow-1", "--shadow-2",
]

# retoken's SHARED_VARS (theme.ts) — names required, values per template.
SHARED_VARS = [
    "--font-body", "--font-mono", "--font-size-sm", "--font-size-base",
    "--font-size-lg", "--font-size-xl", "--font-size-2xl", "--line-height",
    "--space-1", "--space-2", "--space-3", "--space-4", "--space-5",
    "--space-6", "--radius-sm", "--radius-md", "--radius-lg", "--radius-full",
    "--page-max-width", "--sidebar-width", "--panel-width", "--toc-width",
    "--navbar-height",
]

# retemplate's own shared tokens (retoken's editor ignores them).
EXTRA_SHARED = ["--font-display", "--font-weight-display", "--font-size-3xl",
                "--font-size-hero"]

PALETTE_SLOTS = [
    "--pal-bg0", "--pal-bg0-soft", "--pal-bg1", "--pal-bg2", "--pal-bg3",
    "--pal-fg", "--pal-fg-muted", "--pal-gray", "--pal-red", "--pal-green",
    "--pal-yellow", "--pal-blue", "--pal-purple", "--pal-aqua",
    "--pal-accent", "--pal-accent-strong", "--pal-on-accent",
    "--pal-shadow-1", "--pal-shadow-2",
]

# Contrast rules (decision 19). Errors gate; warnings report.
CONTRAST_ERRORS = [("--pal-fg", "--pal-bg0", 4.5),
                   ("--pal-accent", "--pal-bg0", 4.5),
                   ("--pal-on-accent", "--pal-accent", 4.5)]
CONTRAST_WARNINGS = [("--pal-fg-muted", "--pal-bg0", 4.5),
                     ("--pal-accent-strong", "--pal-bg0", 4.5),
                     ("--pal-fg", "--pal-bg0-soft", 4.5),
                     ("--pal-fg", "--pal-bg1", 4.5),
                     ("--pal-red", "--pal-bg0", 3.0),
                     ("--pal-green", "--pal-bg0", 3.0),
                     ("--pal-yellow", "--pal-bg0", 3.0),
                     ("--pal-blue", "--pal-bg0", 3.0)]

TAG_GROUPS = {
    "scheme": {"light-first", "dark-first", "balanced"},
    "type": {"serif", "sans", "display", "mono"},
    "motion": {"animated", "still"},
    "fonts": {"google-fonts", "system-fonts"},
    "feel": {"minimal", "ornate", "playful", "editorial"},
}
TAG_VOCABULARY = set().union(*TAG_GROUPS.values())

ALLOWED_EXTERNAL_HOSTS = ("https://fonts.googleapis.com", "https://fonts.gstatic.com")

ONCLICK_RE = re.compile(
    r"^\s*(?:document\.getElementById\(['\"][\w-]+['\"]\)|[A-Za-z_][\w-]*)"
    r"\.showModal\(\)\s*;?\s*$")

NAMED_COLORS = set("""
aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond
blue blueviolet brown burlywood cadetblue chartreuse chocolate coral
cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray
darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid
darkred darksalmon darkseagreen darkslateblue darkslategray darkslategrey
darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue
firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod
gray green greenyellow grey honeydew hotpink indianred indigo ivory khaki
lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan
lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon
lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue
lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue
mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen
mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin
navajowhite navy oldlace olive olivedrab orange orangered orchid
palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff
peru pink plum powderblue purple rebeccapurple red rosybrown royalblue
saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue
slateblue slategray slategrey snow springgreen steelblue tan teal thistle
tomato turquoise violet wheat white whitesmoke yellow yellowgreen
""".split())

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, int, str]] = []
        self.warnings: list[tuple[str, int, str]] = []

    def error(self, path: Path | str, line: int, msg: str) -> None:
        self.errors.append((rel(path), line, msg))

    def warn(self, path: Path | str, line: int, msg: str) -> None:
        self.warnings.append((rel(path), line, msg))

    def dump(self) -> None:
        for kind, items in (("error", self.errors), ("warning", self.warnings)):
            for path, line, msg in sorted(items):
                where = f"{path}:{line}" if line else path
                print(f"{where}: {kind}: {msg}")


def rel(path: Path | str) -> str:
    p = Path(path)
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


# ---------------------------------------------------------------------------
# A small HTML tree
# ---------------------------------------------------------------------------


class Node:
    __slots__ = ("tag", "attrs", "children", "parent", "line")

    def __init__(self, tag: str, attrs: dict[str, str], line: int, parent=None):
        self.tag = tag
        self.attrs = attrs
        self.children: list = []   # Node or str
        self.parent = parent
        self.line = line

    # -- queries ------------------------------------------------------------
    @property
    def classes(self) -> set[str]:
        return set(self.attrs.get("class", "").split())

    def elements(self):
        return [c for c in self.children if isinstance(c, Node)]

    def walk(self):
        yield self
        for c in self.children:
            if isinstance(c, Node):
                yield from c.walk()

    def text(self) -> str:
        out = []
        for c in self.children:
            out.append(c if isinstance(c, str) else c.text())
        return "".join(out)

    def matches(self, selector: str) -> bool:
        """tag, .class, #id, tag.class, tag#id — nothing else."""
        m = re.fullmatch(r"([a-z0-9-]*)((?:[.#][\w-]+)*)", selector)
        if not m:
            raise ValueError(f"unsupported selector {selector!r}")
        tag, rest = m.group(1), m.group(2)
        if tag and self.tag != tag:
            return False
        for part in re.findall(r"[.#][\w-]+", rest):
            if part[0] == "." and part[1:] not in self.classes:
                return False
            if part[0] == "#" and self.attrs.get("id") != part[1:]:
                return False
        return True

    def select(self, selector: str) -> list["Node"]:
        return [n for n in self.walk() if n.matches(selector)]

    def first(self, selector: str):
        for n in self.walk():
            if n.matches(selector):
                return n
        return None

    def ancestors(self):
        n = self.parent
        while n is not None:
            yield n
            n = n.parent


class Tree(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Node("#document", {}, 0)
        self.cur = self.root
        self.doctype = ""
        self.inline_scripts: list[int] = []

    def handle_decl(self, decl: str) -> None:
        self.doctype = decl.strip()

    def handle_starttag(self, tag, attrs) -> None:
        node = Node(tag, {k: (v if v is not None else "") for k, v in attrs},
                    self.getpos()[0], self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag) -> None:
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is None or n.parent is None:
            return
        self.cur = n.parent

    def handle_data(self, data: str) -> None:
        if self.cur.tag == "script" and data.strip():
            self.inline_scripts.append(self.cur.line)
        self.cur.children.append(data)


def parse_html(text: str) -> Tree:
    t = Tree()
    t.feed(text)
    t.close()
    return t


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalise_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def serialise(node: Node, *, keep_text=True, strip_classes=(), skip_class=None,
              attr_filter=None, collapse=False) -> str:
    """A canonical string for structural comparison.

    With collapse=True, consecutive identical child skeletons are folded into
    one, so a list with three items has the same shape as one with eight."""
    if skip_class and skip_class in node.classes:
        return ""
    attrs = dict(node.attrs)
    if strip_classes:
        cls = [c for c in attrs.get("class", "").split()
               if not any(c.startswith(p) for p in strip_classes)]
        if cls:
            attrs["class"] = " ".join(sorted(cls))
        else:
            attrs.pop("class", None)
    elif "class" in attrs:
        attrs["class"] = " ".join(sorted(attrs["class"].split()))
    if attr_filter:
        attrs = {k: v for k, v in attrs.items() if attr_filter(k)}
    a = "".join(f' {k}="{v}"' for k, v in sorted(attrs.items()))
    inner = []
    for c in node.children:
        if isinstance(c, str):
            if keep_text:
                t = normalise_ws(c)
                if t:
                    inner.append(t)
        else:
            child = serialise(c, keep_text=keep_text, strip_classes=strip_classes,
                              skip_class=skip_class, attr_filter=attr_filter, collapse=collapse)
            if collapse and inner and inner[-1] == child:
                continue
            inner.append(child)
    return f"<{node.tag}{a}>{''.join(inner)}</{node.tag}>"


def first_difference(a: Node, b: Node, **kw) -> tuple[Node, Node] | None:
    """Descend both trees and return the first pair of nodes that differ."""
    if serialise(a, **kw) == serialise(b, **kw):
        return None
    ea, eb = a.elements(), b.elements()
    for x, y in zip(ea, eb):
        if serialise(x, **kw) != serialise(y, **kw):
            return first_difference(x, y, **kw)
    return (a, b)


# ---------------------------------------------------------------------------
# CSS helpers
# ---------------------------------------------------------------------------


def strip_css_comments(css: str) -> str:
    return re.sub(r"/\*.*?\*/", lambda m: " " * len(m.group(0)), css, flags=re.S)


def css_blocks(css: str):
    """Yield (selector, body, line) for every innermost `{}` block."""
    css = strip_css_comments(css)
    i = 0
    stack: list[tuple[str, int, int]] = []   # (selector, body_start, line)
    n = len(css)
    while i < n:
        ch = css[i]
        if ch == "{":
            j = i - 1
            while j >= 0 and css[j] not in "{};":
                j -= 1
            selector = normalise_ws(css[j + 1:i])
            stack.append((selector, i + 1, css.count("\n", 0, i) + 1))
        elif ch == "}":
            if stack:
                selector, start, line = stack.pop()
                body = css[start:i]
                # drop nested blocks from the body so declarations are ours only
                body = re.sub(r"[^{};]*\{[^{}]*\}", "", body)
                yield selector, body, line
        i += 1


def declarations(body: str):
    for m in re.finditer(r"(?:^|;)\s*(--[\w-]+|[a-zA-Z-]+)\s*:\s*([^;]+)", body):
        yield m.group(1).strip(), m.group(2).strip()


def css_urls(css: str):
    for m in re.finditer(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", strip_css_comments(css)):
        yield m.group(2).strip(), css.count("\n", 0, m.start()) + 1


COLOR_FUNCTION_RE = re.compile(r"\b(rgba?|hsla?|hwb|lab|lch|oklab|oklch|color)\s*\(")
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")


def colour_literals(value: str, prop: str) -> list[str]:
    """Colour literals in a declaration value, ignoring url() and var()."""
    v = re.sub(r"url\([^)]*\)", " ", value)
    v = re.sub(r"var\([^)]*\)", " ", v)
    hits = HEX_RE.findall(v) + [m.group(0) for m in COLOR_FUNCTION_RE.finditer(v)]
    if not prop.startswith("font"):
        for word in re.findall(r"[A-Za-z]+", v):
            if word.lower() in NAMED_COLORS:
                hits.append(word)
    return hits


# -- colour parsing for contrast --------------------------------------------

def _srgb_to_linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c: float) -> float:
    c = min(max(c, 0.0), 1.0)
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def _oklch_to_rgb(L: float, C: float, H: float):
    a = C * math.cos(math.radians(H))
    b = C * math.sin(math.radians(H))
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    if C > 0.0005 and any(x < -0.0005 or x > 1.0005 for x in (r, g, bb)):
        return _oklch_to_rgb(L, C - 0.002, H)      # CSS-style gamut mapping: reduce chroma
    return tuple(_linear_to_srgb(x) for x in (r, g, bb))


def parse_colour(value: str):
    """-> (r, g, b) in 0..1, or None when the value is not a plain colour."""
    v = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        elif len(h) == 8:
            h = h[:6]
        if len(h) != 6:
            return None
        return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(([^)]*)\)", v)
    if m:
        parts = re.split(r"[\s,/]+", m.group(1).strip())[:3]
        try:
            return tuple(float(p.rstrip("%")) / (100 if p.endswith("%") else 255) for p in parts)
        except ValueError:
            return None
    m = re.fullmatch(r"hsla?\(([^)]*)\)", v)
    if m:
        parts = re.split(r"[\s,/]+", m.group(1).strip())[:3]
        try:
            h = float(re.sub(r"deg$", "", parts[0])) / 360
            s = float(parts[1].rstrip("%")) / 100
            l = float(parts[2].rstrip("%")) / 100
        except (ValueError, IndexError):
            return None
        import colorsys
        return colorsys.hls_to_rgb(h, l, s)
    m = re.fullmatch(r"oklch\(([^)]*)\)", v)
    if m:
        parts = re.split(r"[\s,/]+", m.group(1).strip())[:3]
        try:
            L = float(parts[0].rstrip("%")) / (100 if parts[0].endswith("%") else 1)
            C = float(parts[1])
            H = float(re.sub(r"deg$", "", parts[2]))
        except (ValueError, IndexError):
            return None
        return _oklch_to_rgb(L, C, H)
    if v == "white":
        return (1.0, 1.0, 1.0)
    if v == "black":
        return (0.0, 0.0, 0.0)
    return None


def luminance(rgb) -> float:
    r, g, b = (_srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def split_light_dark(value: str):
    m = re.fullmatch(r"light-dark\((.*)\)", value.strip(), flags=re.S)
    if not m:
        return None
    depth, start, parts = 0, 0, []
    s = m.group(1)
    for i, ch in enumerate(s):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(s[start:i].strip())
            start = i + 1
    parts.append(s[start:].strip())
    return parts if len(parts) == 2 else None


# ---------------------------------------------------------------------------
# Link resolution
# ---------------------------------------------------------------------------


def is_external(url: str) -> bool:
    return url.startswith(("http://", "https://", "//"))


def resolve(page: Path, url: str) -> Path:
    target = url.split("#", 1)[0].split("?", 1)[0]
    return (page.parent / target).resolve()


def inside(path: Path, folder: Path) -> bool:
    try:
        path.relative_to(folder)
        return True
    except ValueError:
        return False


# ---------------------------------------------------------------------------
# Per-template checks
# ---------------------------------------------------------------------------


class TemplateCheck:
    def __init__(self, folder: Path, report: Report, plain_shapes=None):
        self.folder = folder
        self.name = folder.name
        self.r = report
        self.plain_shapes = plain_shapes
        self.pages: dict[str, Tree] = {}
        self.page_paths: list[Path] = sorted(folder.rglob("*.html"))

    # -- helpers ---------------------------------------------------------------
    def relpath(self, page: Path) -> str:
        return page.relative_to(self.folder).as_posix()

    def tree(self, page: Path) -> Tree:
        key = self.relpath(page)
        if key not in self.pages:
            self.pages[key] = parse_html(read(page))
        return self.pages[key]

    def run(self) -> None:
        self.check_structure()
        for page in self.page_paths:
            self.check_head(page)
            self.check_links_html(page)
            self.check_js(page)
        for css in ("css/theme.css", "css/global.css"):
            p = self.folder / css
            if p.exists():
                self.check_links_css(p)
        self.check_tokens()
        self.check_fixtures()
        self.check_snippets()
        self.check_nav()
        self.check_component_pages()
        self.check_contract()

    # -- structure ---------------------------------------------------------------
    def check_structure(self) -> None:
        for f in REQUIRED_FILES:
            if not (self.folder / f).exists():
                self.r.error(self.folder / f, 0, "required file missing")
        example = self.folder / "example"
        if example.is_dir():
            pages = sorted(p.name for p in example.glob("*.html"))
            if len(pages) != 3 or "index.html" not in pages:
                self.r.error(example, 0,
                             f"example/ must hold index.html + exactly two more pages, found {pages}")
        css_dir = self.folder / "css"
        if css_dir.is_dir():
            for p in css_dir.iterdir():
                if p.name not in ("theme.css", "global.css"):
                    self.r.error(p, 0, "css/ may only contain theme.css and global.css")
        js_dir = self.folder / "js"
        if js_dir.is_dir():
            for p in js_dir.iterdir():
                if p.name not in ("theme.js", "copy.js"):
                    self.r.error(p, 0, "js/ may only contain theme.js and copy.js")
        assets = self.folder / "assets"
        if assets.is_dir():
            for p in assets.rglob("*"):
                if p.is_file() and p.suffix.lower() not in (".svg", ".png", ".jpg", ".jpeg", ".webp", ".ico"):
                    self.r.error(p, 0, "assets/ holds images only")
            for f in ("fixture-photo-1.svg", "fixture-photo-2.svg", "avatar.svg"):
                if not (assets / f).exists():
                    self.r.error(assets / f, 0, "fixture image every template must ship")
        fonts = self.folder / "fonts"
        if fonts.is_dir():
            for p in fonts.rglob("*"):
                if p.is_file() and p.suffix.lower() not in (".woff2", ".txt", ".md", ".json"):
                    self.r.error(p, 0, "fonts/ holds woff2 files and their licences only")
        for top in self.folder.iterdir():
            if top.is_file() and top.name not in TOP_PAGES + ["README.md"]:
                self.r.error(top, 0, "unexpected file at the template root")
            if top.is_dir() and top.name not in ("css", "js", "fonts", "assets", "docs", "example"):
                self.r.error(top, 0, "unexpected folder at the template root")

    # -- head ---------------------------------------------------------------------
    def check_head(self, page: Path) -> None:
        t = self.tree(page)
        depth = len(page.relative_to(self.folder).parts) - 1
        prefix = "../" * depth
        if not t.doctype.lower().startswith("doctype html"):
            self.r.error(page, 1, "missing <!doctype html>")
        html = t.root.first("html")
        if html is None:
            self.r.error(page, 1, "no <html> element")
            return
        if html.attrs.get("lang") != "en":
            self.r.error(page, html.line, 'html must carry lang="en"')
        if html.attrs.get("data-theme") != self.name:
            self.r.error(page, html.line, f'html must carry data-theme="{self.name}"')
        head = html.first("head")
        if head is None:
            self.r.error(page, html.line, "no <head>")
            return
        metas = head.select("meta")
        if not any(m.attrs.get("charset", "").lower() == "utf-8" for m in metas):
            self.r.error(page, head.line, '<meta charset="utf-8"> missing')
        if not any(m.attrs.get("name") == "viewport" for m in metas):
            self.r.error(page, head.line, "viewport meta missing")
        if not any(m.attrs.get("name") == "color-scheme" and
                   normalise_ws(m.attrs.get("content", "")) == "light dark" for m in metas):
            self.r.error(page, head.line, '<meta name="color-scheme" content="light dark"> missing')
        title = head.first("title")
        if title is None or not title.text().strip():
            self.r.error(page, head.line, "<title> missing or empty")
        icon = [l for l in head.select("link") if l.attrs.get("rel") == "icon"]
        if not icon or not icon[0].attrs.get("href", "").endswith("assets/favicon.svg"):
            self.r.error(page, head.line, f'<link rel="icon" href="{prefix}assets/favicon.svg"> missing')
        # theme.js: synchronous, in head, before the stylesheets
        order = [n for n in head.elements() if n.tag in ("script", "link")]
        scripts = [n for n in order if n.tag == "script"]
        sheets = [n for n in order if n.tag == "link" and n.attrs.get("rel") == "stylesheet"]
        boot = [s for s in scripts if s.attrs.get("src", "").endswith("js/theme.js")]
        if not boot:
            self.r.error(page, head.line, f'<script src="{prefix}js/theme.js"></script> missing from <head>')
        else:
            b = boot[0]
            if "defer" in b.attrs or "async" in b.attrs or b.attrs.get("type") == "module":
                self.r.error(page, b.line, "theme.js must be a plain synchronous script (no defer/async/module)")
            if sheets and order.index(b) > order.index(sheets[0]):
                self.r.error(page, b.line, "theme.js must come before the stylesheets")
        hrefs = [s.attrs.get("href", "") for s in sheets]
        local = [h for h in hrefs if not is_external(h)]
        expected = [f"{prefix}css/theme.css", f"{prefix}css/global.css"]
        if local != expected:
            self.r.error(page, head.line, f"stylesheets must be exactly {expected} in that order, found {local}")
        for l in head.select("link"):
            href = l.attrs.get("href", "")
            if is_external(href) and not href.startswith(ALLOWED_EXTERNAL_HOSTS):
                self.r.error(page, l.line, f"external <link> not allowed: {href}")
        if depth == 0 and page.name == "index.html":
            self.check_overview(page)

    def check_overview(self, page: Path) -> None:
        t = self.tree(page)
        for sel in OVERVIEW_MUST_USE:
            if not t.root.first(sel):
                self.r.error(page, 0, f"index.html must use {sel} at least once")

    # -- links ------------------------------------------------------------------------
    def check_links_html(self, page: Path) -> None:
        t = self.tree(page)
        for n in t.root.walk():
            for attr in ("href", "src", "poster", "data"):
                url = n.attrs.get(attr)
                if url is None or n.tag == "#document":
                    continue
                if n.tag == "use" and attr == "href" and url.startswith("#"):
                    continue
                self.check_url(page, n, attr, url)
            if "srcset" in n.attrs:
                for cand in n.attrs["srcset"].split(","):
                    self.check_url(page, n, "srcset", cand.strip().split()[0])

    def check_url(self, page: Path, n: Node, attr: str, url: str) -> None:
        url = url.strip()
        if not url or url.startswith(("#", "mailto:", "tel:", "data:")):
            return
        if url.startswith("javascript:"):
            self.r.error(page, n.line, "javascript: URLs are not allowed")
            return
        if is_external(url):
            if n.tag == "a":
                return                                   # hyperlinks may leave the site
            if n.tag == "link" and url.startswith(ALLOWED_EXTERNAL_HOSTS):
                return
            self.r.error(page, n.line, f"external resource not allowed: {url}")
            return
        if url.startswith("/"):
            self.r.error(page, n.line, f"root-absolute path: {url}")
            return
        target = resolve(page, url)
        if target.is_dir():
            self.r.error(page, n.line, f"directory link ({url}); point at a file such as index.html")
            return
        if not inside(target, self.folder):
            if n.tag == "a" and "site-link" in n.classes and target == LANDING.resolve():
                if not target.exists():
                    self.r.warn(page, n.line, "site-link points at the landing page, which is not built yet")
                return
            self.r.error(page, n.line, f"link leaves the template folder: {url}")
            return
        if not target.exists():
            self.r.error(page, n.line, f"broken link: {url}")

    def check_links_css(self, css: Path) -> None:
        for url, line in css_urls(read(css)):
            if url.startswith("data:"):
                continue
            if is_external(url):
                self.r.error(css, line, f"external url() not allowed: {url}")
                continue
            if url.startswith("/"):
                self.r.error(css, line, f"root-absolute url(): {url}")
                continue
            target = resolve(css, url)
            if not target.exists():
                self.r.error(css, line, f"broken url(): {url}")
                continue
            ok = any(inside(target, self.folder / d) for d in ("css", "assets", "fonts"))
            if not ok:
                self.r.error(css, line, f"install-set file references outside the install set: {url}")

    # -- javascript -------------------------------------------------------------------
    def check_js(self, page: Path) -> None:
        t = self.tree(page)
        for line in t.inline_scripts:
            self.r.error(page, line, "inline <script> content is not allowed")
        for s in t.root.select("script"):
            src = s.attrs.get("src", "")
            if not src:
                continue
            target = resolve(page, src)
            if target not in (self.folder / "js/theme.js", self.folder / "js/copy.js"):
                self.r.error(page, s.line, f"script not on the allow-list: {src}")
        for n in t.root.walk():
            for k, v in n.attrs.items():
                if k.startswith("on"):
                    if k != "onclick" or not ONCLICK_RE.match(v):
                        self.r.error(page, n.line,
                                     f'inline handler not allowed: {k}="{v}" (only onclick="…showModal()")')

    # -- tokens ---------------------------------------------------------------------------
    def check_tokens(self) -> None:
        theme = self.folder / "css/theme.css"
        glob = self.folder / "css/global.css"
        if theme.exists():
            self.check_theme_css(theme)
        if glob.exists():
            self.check_global_css(glob)

    def check_theme_css(self, theme: Path) -> None:
        css = read(theme)
        blocks = list(css_blocks(css))
        palette_sel = {f":root[data-theme='{self.name}'], [data-theme='{self.name}']",
                       f':root[data-theme="{self.name}"], [data-theme="{self.name}"]'}
        semantic = [b for b in blocks if b[0] == ":root, .themed"]
        palette = [b for b in blocks if b[0] in palette_sel]
        if not semantic:
            self.r.error(theme, 0, "missing the `:root, .themed` block")
        else:
            decl = dict(declarations(semantic[0][1]))
            line = semantic[0][2]
            if normalise_ws(decl.get("color-scheme", "")) != "light dark":
                self.r.error(theme, line, "`:root, .themed` must declare `color-scheme: light dark`")
            for name in COLOR_MAPPING + SHARED_VARS + EXTRA_SHARED:
                if name not in decl:
                    self.r.error(theme, line, f"`:root, .themed` must declare {name}")
            for name, value in decl.items():
                if name.startswith("--pal-"):
                    self.r.error(theme, line, f"{name} belongs in the palette block, not `:root, .themed`")
                if name in COLOR_MAPPING or name in SHARED_VARS or name in EXTRA_SHARED:
                    lits = colour_literals(value, name)
                    if lits and name in COLOR_MAPPING:
                        self.r.error(theme, line, f"{name} must map to tokens, not literals ({lits[0]})")
        if not palette:
            self.r.error(theme, 0, f"missing the palette block `:root[data-theme='{self.name}'], [data-theme='{self.name}']`")
        else:
            decl = dict(declarations(palette[0][1]))
            line = palette[0][2]
            slots = [k for k in decl if k.startswith("--pal-")]
            missing = [s for s in PALETTE_SLOTS if s not in decl]
            extra = [s for s in slots if s not in PALETTE_SLOTS]
            if missing:
                self.r.error(theme, line, f"palette block missing {missing}")
            if extra:
                self.r.error(theme, line, f"palette block has unknown slots {extra}")
            for k in slots:
                if not decl[k].startswith("light-dark("):
                    self.r.error(theme, line, f"{k} must be a light-dark() pair")
            self.check_contrast(theme, line, decl)
        # every --pal-* declaration lives in the palette block; no bare :root palette
        for sel, body, line in blocks:
            if sel in palette_sel:
                continue
            for name, value in declarations(body):
                if name.startswith("--pal-"):
                    self.r.error(theme, line, f"{name} declared under `{sel}`; the palette may only be declared in the named palette block")
                if name.startswith("--") and not name.startswith(f"--{self.name}-") and sel != ":root, .themed":
                    self.r.error(theme, line, f"{name} declared under `{sel}`: only `--{self.name}-*` tokens may live outside the two contract blocks")
                if name.startswith("--") and sel not in (":root, .themed") and not name.startswith(f"--{self.name}-"):
                    pass
            if sel.startswith(":root") and "data-theme" not in sel and sel != ":root, .themed" and any(
                    n.startswith("--pal-") for n, _ in declarations(body)):
                self.r.error(theme, line, "a bare :root palette would hijack a retoken site; use the named form")
        # template tokens may hold literals; anything else in theme.css may not
        for sel, body, line in blocks:
            for name, value in declarations(body):
                if name.startswith("--pal-") or name.startswith(f"--{self.name}-"):
                    continue
                if name.startswith("--") and (name in COLOR_MAPPING):
                    continue
                if name in ("scrollbar-color",):
                    continue
                if not name.startswith("--") and colour_literals(value, name):
                    self.r.error(theme, line, f"colour literal in `{sel} {{ {name} }}`; use a token")

    def check_contrast(self, theme: Path, line: int, decl: dict[str, str]) -> None:
        halves: dict[str, tuple] = {}
        for slot in PALETTE_SLOTS:
            v = decl.get(slot)
            if not v:
                continue
            pair = split_light_dark(v)
            if not pair:
                continue
            cols = tuple(parse_colour(p) for p in pair)
            if any(c is None for c in cols):
                if slot not in ("--pal-shadow-1", "--pal-shadow-2"):
                    self.r.warn(theme, line, f"{slot}: could not parse a colour for contrast ({v})")
                continue
            halves[slot] = cols
        for fg, bg, minimum in CONTRAST_ERRORS:
            self._contrast_rule(theme, line, halves, fg, bg, minimum, error=True)
        for fg, bg, minimum in CONTRAST_WARNINGS:
            self._contrast_rule(theme, line, halves, fg, bg, minimum, error=False)

    def _contrast_rule(self, theme, line, halves, fg, bg, minimum, error) -> None:
        if fg not in halves or bg not in halves:
            return
        for i, half in enumerate(("light", "dark")):
            ratio = contrast(halves[fg][i], halves[bg][i])
            if ratio < minimum:
                msg = f"{fg} on {bg} in {half} is {ratio:.2f}:1 (needs {minimum}:1)"
                (self.r.error if error else self.r.warn)(theme, line, msg)

    def check_global_css(self, glob: Path) -> None:
        css = read(glob)
        for sel, body, line in css_blocks(css):
            for name, value in declarations(body):
                if "var(--pal-" in value:
                    self.r.error(glob, line, f"global.css references a palette slot in `{sel} {{ {name} }}`; use a semantic token")
                lits = colour_literals(value, name)
                if lits:
                    self.r.error(glob, line, f"colour literal {lits[0]} in `{sel} {{ {name} }}`; global.css uses tokens only")
                if "light-dark(" in value:
                    self.r.warn(glob, line, f"light-dark() in global.css (`{sel} {{ {name} }}`); scheme pairs belong in theme.css")
        if "prefers-reduced-motion" not in css:
            self.r.warn(glob, 0, "global.css does not mention prefers-reduced-motion")

    # -- fixtures ------------------------------------------------------------------------
    def check_fixtures(self) -> None:
        for fixture, page_name in (("markdown-test", "blogpost.html"), ("forms", "forms.html")):
            fpath = FIXTURES / f"{fixture}.html"
            page = self.folder / page_name
            if not fpath.exists() or not page.exists():
                continue
            canon = self._fixture_node(parse_html(read(fpath)).root, fixture)
            mine = self._fixture_node(self.tree(page).root, fixture)
            if canon is None:
                self.r.error(fpath, 0, f'no element with data-fixture="{fixture}"')
                continue
            if mine is None:
                self.r.error(page, 0, f'{page_name} must embed the fixture: an element with data-fixture="{fixture}"')
                continue
            diff = first_difference(canon, mine)
            if diff:
                a, b = diff
                self.r.error(page, b.line,
                             f"fixture drift: <{b.tag}> differs from fixtures/{fixture}.html:{a.line} <{a.tag}>")

    @staticmethod
    def _fixture_node(root: Node, name: str):
        for n in root.walk():
            if n.attrs.get("data-fixture") == name:
                return n
        return None

    # -- snippets ----------------------------------------------------------------------------
    def check_snippets(self) -> None:
        for page in self.page_paths:
            if "docs" not in page.relative_to(self.folder).parts:
                continue
            t = self.tree(page)
            examples = {n.attrs["data-snippet"]: n for n in t.root.select("figure")
                        if "data-snippet" in n.attrs}
            codes = [n for n in t.root.select("code") if "data-snippet" in n.attrs]
            seen = set()
            for code in codes:
                key = code.attrs["data-snippet"]
                seen.add(key)
                if key == "palette":
                    self.check_palette_snippet(page, code)
                    continue
                snippet_tree = parse_html(code.text())
                snippet_nodes = snippet_tree.root.elements()
                if "data-source" in code.attrs:
                    src = resolve(page, code.attrs["data-source"])
                    sel = code.attrs.get("data-select", "")
                    if not src.exists() or not sel:
                        self.r.error(page, code.line, "data-source snippet needs an existing data-source and a data-select")
                        continue
                    live = parse_html(read(src)).root.first(sel)
                    if live is None:
                        self.r.error(page, code.line, f"data-select {sel!r} matches nothing in {rel(src)}")
                        continue
                    live_nodes = [live]
                else:
                    fig = examples.get(key)
                    if fig is None:
                        self.r.error(page, code.line, f'snippet "{key}" has no <figure class="example" data-snippet="{key}">')
                        continue
                    live_nodes = fig.elements()
                self._compare_nodes(page, code, live_nodes, snippet_nodes, key)
            for key, fig in examples.items():
                if key not in seen:
                    self.r.error(page, fig.line, f'example "{key}" has no <code data-snippet="{key}">')

    def _compare_nodes(self, page, code, live_nodes, snippet_nodes, key) -> None:
        kw = dict(keep_text=True)
        live_s = [serialise(n, **kw) for n in live_nodes]
        snip_s = [serialise(n, **kw) for n in snippet_nodes]
        if live_s == snip_s:
            return
        if len(live_s) != len(snip_s):
            self.r.error(page, code.line,
                         f'snippet "{key}": {len(snip_s)} top-level element(s) in the snippet, {len(live_s)} in the example')
            return
        for a, b in zip(live_nodes, snippet_nodes):
            d = first_difference(a, b, **kw)
            if d:
                self.r.error(page, code.line,
                             f'snippet "{key}" differs from the live example at <{d[0].tag}> (example line {d[0].line})')
                return

    def palette_block_text(self) -> str | None:
        theme = self.folder / "css/theme.css"
        if not theme.exists():
            return None
        css = strip_css_comments(read(theme))
        m = re.search(rf":root\[data-theme=['\"]{self.name}['\"]\],\s*\[data-theme=['\"]{self.name}['\"]\]\s*\{{[^}}]*\}}", css)
        return normalise_ws(m.group(0)) if m else None

    def check_palette_snippet(self, page: Path, code: Node) -> None:
        block = self.palette_block_text()
        if block is None:
            return
        if normalise_ws(code.text()) != block:
            self.r.error(page, code.line, "the palette snippet does not match the palette block in css/theme.css")

    def check_readme_palette(self) -> None:
        readme = self.folder / "README.md"
        block = self.palette_block_text()
        if not readme.exists() or block is None:
            return
        text = read(readme)
        fences = re.findall(r"```css\n(.*?)```", text, flags=re.S)
        if not any(normalise_ws(f) == block for f in fences):
            self.r.error(readme, 0, "README.md must print the palette block (```css fence) exactly as in css/theme.css")

    # -- navigation --------------------------------------------------------------------------
    def check_nav(self) -> None:
        self.check_readme_palette()
        sidebar_sets: dict[str, set[str]] = {}
        for rp in SIDEBAR_PAGES:
            page = self.folder / rp
            if not page.exists():
                continue
            t = self.tree(page)
            aside = t.root.first("aside.sidebar")
            if aside is None:
                self.r.error(page, 0, "sidebar page without <aside class=\"sidebar\">")
                continue
            links = set()
            current_ok = False
            for a in aside.select("a"):
                href = a.attrs.get("href", "")
                if not href or is_external(href) or href.startswith("#"):
                    continue
                target = resolve(page, href)
                if "site-link" in a.classes:
                    continue
                if inside(target, self.folder):
                    key = target.relative_to(self.folder).as_posix()
                    links.add(key)
                    if key == rp and a.attrs.get("aria-current") == "page":
                        current_ok = True
            if not current_ok:
                self.r.error(page, aside.line, 'the sidebar link to this page must carry aria-current="page"')
            if not aside.select("a.site-link"):
                self.r.error(page, aside.line, 'the sidebar must carry the one <a class="site-link"> back to the landing')
            sidebar_sets[rp] = links
        if sidebar_sets:
            required = set(TOP_PAGES + DOCS_PAGES + ["example/index.html"])
            first_key = next(iter(sidebar_sets))
            canonical = sidebar_sets[first_key]
            for rp, links in sidebar_sets.items():
                if links != canonical:
                    self.r.error(self.folder / rp, 0,
                                 f"sidebar links differ from {first_key}: {sorted(links ^ canonical)}")
            missing = required - canonical
            if missing:
                self.r.error(self.folder / first_key, 0, f"sidebar nav is missing links to {sorted(missing)}")
        navbar_sets: dict[str, set[str]] = {}
        for rp in NAVBAR_PAGES:
            page = self.folder / rp
            if not page.exists():
                continue
            header = self.tree(page).root.first("header.navbar")
            if header is None:
                self.r.error(page, 0, "navbar page without <header class=\"navbar\">")
                continue
            if not header.select("a.site-link"):
                self.r.error(page, header.line, 'the navbar must carry the one <a class="site-link"> back to the landing')
            if not header.select("button.scheme-toggle"):
                self.r.error(page, header.line, "the navbar must carry <button class=\"scheme-toggle\">")
            links = set()
            for a in header.select("a"):
                href = a.attrs.get("href", "")
                if href and not is_external(href) and "site-link" not in a.classes:
                    target = resolve(page, href)
                    if inside(target, self.folder):
                        links.add(target.relative_to(self.folder).as_posix())
            navbar_sets[rp] = links
        if navbar_sets:
            first_key = next(iter(navbar_sets))
            for rp, links in navbar_sets.items():
                if links != navbar_sets[first_key]:
                    self.r.error(self.folder / rp, 0, f"navbar links differ from {first_key}")
        for page in sorted((self.folder / "example").glob("*.html")) if (self.folder / "example").is_dir() else []:
            t = self.tree(page)
            back = any(resolve(page, a.attrs.get("href", "")) == self.folder / "index.html"
                       for a in t.root.select("a") if a.attrs.get("href") and not is_external(a.attrs["href"]))
            if not back:
                self.r.error(page, 0, "example pages must link back to ../index.html (the template overview)")

    # -- component pages ----------------------------------------------------------------------
    def check_component_pages(self) -> None:
        for comp, sel in COMPONENT_PAGE_MUST_CONTAIN.items():
            page = self.folder / f"docs/components/{comp}.html"
            if not page.exists() or sel is None:
                continue
            if not self.tree(page).root.first(sel):
                self.r.error(page, 0, f"component page must show {sel}")
        for comp in COMPONENTS:
            page = self.folder / f"docs/components/{comp}.html"
            if page.exists() and not self.tree(page).root.select("code"):
                self.r.error(page, 0, "component page has no <code> snippet")

    # -- contract shapes ------------------------------------------------------------------------
    def shapes(self) -> dict[str, set[str]]:
        """For each contract component selector, the set of skeletons found."""
        out: dict[str, set[str]] = {s: set() for s in CONTRACT_COMPONENTS}
        for page in self.page_paths:
            t = self.tree(page)
            for sel in CONTRACT_COMPONENTS:
                for n in t.root.select(sel):
                    out[sel].add(self.skeleton(n))
        return out

    def skeleton(self, n: Node) -> str:
        keep = lambda k: k in ("name", "role", "popover", "popovertarget", "type", "open") or k.startswith("data-")
        return serialise(n, keep_text=False, strip_classes=(f"{self.name}-",),
                         skip_class=f"{self.name}-flare", attr_filter=keep, collapse=True)

    def check_contract(self) -> None:
        if self.plain_shapes is None or self.name == "plain":
            return
        for page in self.page_paths:
            t = self.tree(page)
            for sel in CONTRACT_COMPONENTS:
                for n in t.root.select(sel):
                    if self.skeleton(n) not in self.plain_shapes[sel]:
                        self.r.error(page, n.line,
                                     f"{sel} instance does not match any shape in templates/plain (contract drift; add flare inside .{self.name}-flare or report a contract gap)")


# ---------------------------------------------------------------------------
# Root-level checks: landing, fixtures, bookkeeping
# ---------------------------------------------------------------------------


def check_root_page(page: Path, report: Report, allowed_scripts: set[Path]) -> None:
    t = parse_html(read(page))
    if not t.doctype.lower().startswith("doctype html"):
        report.error(page, 1, "missing <!doctype html>")
    head = t.root.first("head")
    if head is None:
        report.error(page, 1, "no <head>")
        return
    metas = head.select("meta")
    for what, ok in (("charset", any(m.attrs.get("charset", "").lower() == "utf-8" for m in metas)),
                     ("viewport", any(m.attrs.get("name") == "viewport" for m in metas)),
                     ("color-scheme", any(m.attrs.get("name") == "color-scheme" for m in metas))):
        if not ok:
            report.error(page, head.line, f"{what} meta missing")
    for line in t.inline_scripts:
        report.error(page, line, "inline <script> content is not allowed")
    for s in t.root.select("script"):
        src = s.attrs.get("src", "")
        if src and resolve(page, src) not in allowed_scripts:
            report.error(page, s.line, f"script not on the allow-list: {src}")
    for n in t.root.walk():
        for attr in ("href", "src"):
            url = n.attrs.get(attr)
            if not url or url.startswith(("#", "mailto:", "data:")):
                continue
            if is_external(url):
                if n.tag == "a" or (n.tag == "link" and url.startswith(ALLOWED_EXTERNAL_HOSTS)):
                    continue
                report.error(page, n.line, f"external resource not allowed: {url}")
                continue
            if url.startswith("/"):
                report.error(page, n.line, f"root-absolute path: {url}")
                continue
            target = resolve(page, url)
            if target.is_dir():
                report.error(page, n.line, f"directory link ({url})")
            elif not target.exists():
                if target == LANDING.resolve():
                    report.warn(page, n.line, "links to the landing page, which is not built yet")
                else:
                    report.error(page, n.line, f"broken link: {url}")
            elif not inside(target, ROOT):
                report.error(page, n.line, f"link leaves the repo: {url}")
        for k, v in n.attrs.items():
            if k.startswith("on") and (k != "onclick" or not ONCLICK_RE.match(v)):
                report.error(page, n.line, f'inline handler not allowed: {k}="{v}"')


def check_landing(report: Report, template_names: list[str]) -> None:
    if not LANDING.exists():
        report.warn(LANDING, 0, "no landing page yet (Phase 2)")
        return
    check_root_page(LANDING, report, {ROOT / "landing/theme.js", ROOT / "landing/landing.js"})
    t = parse_html(read(LANDING))
    cards = {n.attrs["data-template"]: n for n in t.root.walk() if "data-template" in n.attrs}
    for name in template_names:
        card = cards.get(name)
        if card is None:
            report.error(LANDING, 0, f"no card for templates/{name}/ (an element with data-template=\"{name}\")")
            continue
        tags = set(card.attrs.get("data-tags", "").split())
        unknown = tags - TAG_VOCABULARY
        if unknown:
            report.error(LANDING, card.line, f"card {name}: tags not in the vocabulary: {sorted(unknown)}")
        for group, allowed in TAG_GROUPS.items():
            if not tags & allowed:
                report.error(LANDING, card.line, f"card {name}: needs a {group} tag ({sorted(allowed)})")
        for scheme in ("light", "dark"):
            p = ROOT / "landing/previews" / f"{name}-{scheme}.svg"
            if not p.exists():
                report.error(p, 0, "preview missing")
    for name in cards:
        if name not in template_names:
            report.error(LANDING, cards[name].line, f"card for a template folder that does not exist: {name}")
    readme = TEMPLATES / "README.md"
    if readme.exists():
        text = read(readme)
        for name in template_names:
            if f"templates/{name}/" not in text and f"{name}/" not in text:
                report.error(readme, 0, f"templates/README.md has no row for {name}")


def check_fixture_pages(report: Report) -> None:
    for p in sorted(FIXTURES.glob("*.html")) if FIXTURES.is_dir() else []:
        check_root_page(p, report, set())
        t = parse_html(read(p))
        if not any("data-fixture" in n.attrs for n in t.root.walk()):
            report.error(p, 0, "fixture page has no [data-fixture] element")


def check_bookkeeping(report: Report) -> None:
    version = (ROOT / "VERSION")
    changelog = ROOT / "CHANGELOG.md"
    if version.exists() and changelog.exists():
        v = read(version).strip()
        first = next((l for l in read(changelog).splitlines() if l.startswith("# ")), "")
        if v not in first:
            report.warn(changelog, 1, f"first heading does not mention VERSION {v}: {first!r}")


# ---------------------------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--template", help="check only templates/<name>")
    ap.add_argument("--list", action="store_true", help="print the contract file list and exit")
    args = ap.parse_args(argv)

    if args.list:
        print("\n".join(REQUIRED_FILES))
        return 0

    report = Report()
    names = sorted(p.name for p in TEMPLATES.iterdir() if p.is_dir()) if TEMPLATES.is_dir() else []
    if args.template:
        if args.template not in names:
            print(f"templates/{args.template}/ does not exist", file=sys.stderr)
            return 1
        selected = [args.template]
    else:
        selected = names

    plain_shapes = None
    if "plain" in names and (args.template or "plain") != "plain" or (not args.template and "plain" in names):
        plain_shapes = TemplateCheck(TEMPLATES / "plain", Report()).shapes()

    for name in selected:
        TemplateCheck(TEMPLATES / name, report, plain_shapes).run()

    if not args.template:
        check_landing(report, names)
        check_fixture_pages(report)
        check_bookkeeping(report)
        if not names:
            print("no templates yet; root checks only")

    report.dump()
    scope = f"templates/{args.template}" if args.template else "everything"
    print(f"checked {scope}: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
