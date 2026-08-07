import io
import re as _re
from textwrap import dedent

import marimo as mo
import matplotlib.pyplot as plt

# Match KaTeX's serif "Computer Modern"-derived look for equations rendered
# via matplotlib's mathtext (tex_svg/tex_inline below) -- matplotlib's own
# default (DejaVu Sans) looks visibly different from the KaTeX equations
# everywhere else in the deck.
plt.rcParams["mathtext.fontset"] = "cm"

HEAD_FONT = "-apple-system, 'Helvetica Neue', Arial, sans-serif"

# Type sizes are viewport-relative (vw) so they grow in marimo's native
# fullscreen. `rem` is tied to the root font-size, which fullscreen does
# not change -- that's why the deck used to keep laptop-sized text on a
# projector. clamp() keeps it readable in a small window too.
H1_SIZE = "clamp(1.6rem, 2.6vw, 5rem)"
H2_SIZE = "clamp(0.95rem, 1.4vw, 2.6rem)"


def h1(text: str) -> str:
    return f'<div style="font-family:{HEAD_FONT}; font-weight:800; font-size:{H1_SIZE}; color:#111; line-height:1.15; margin-bottom:0.6rem;">{text}</div>'


def h2(text: str) -> str:
    return f'<div style="font-family:{HEAD_FONT}; font-weight:700; font-size:{H2_SIZE}; color:#111; margin-top:-0.3rem;">{text}</div>'


def bullet_slide(tag: str, heading: str, body_md: str, image_html=None) -> None:
    """Two-column: tag + heading + bullet/markdown body on the left,
    an optional image or figure on the right. Notes tag pinned to bottom-left."""
    left = mo.vstack(
        [
            mo.Html(h2(tag) + h1(heading)),
            mo.md(dedent(body_md).strip()),
        ],
        gap=0.25,
        align="stretch",
        justify="space-between",
    )
    if image_html is not None:
        return mo.hstack([left, image_html], widths=[1, 1], align="start", gap=2)
    return left


def title_only_slide(tag: str, heading: str) -> None:
    return mo.Html(h2(tag) + h1(heading))


def omega_card(inner_html: str = "") -> str:
    """Empty white card with a drop shadow and an 'Omega' label bottom-left,
    matching the deck's blank sample-space placeholder panel."""
    return f"""
    <div style="position:relative; background:#fff; border-radius:4px;
                box-shadow:0 6px 18px rgba(0,0,0,0.15); min-height:280px;
                padding:1rem; margin:1rem 0;">
        {inner_html}
        <div style="position:absolute; left:1rem; bottom:0.75rem;
                    font-family:{HEAD_FONT}; font-style:italic;
                    font-size:clamp(1rem, 1.8vw, 2.2rem);">&Omega;</div>
    </div>
    """


def notes_tag(text: str) -> str:
    """Small dark pill badge mimicking the deck's 'See Lecture Notes' tag."""
    return f"""
    <div style="display:inline-block; background:#111; color:#fff;
                border-radius:999px; padding:0.2rem 0.6rem; margin-top:0.5rem;
                font-family:{HEAD_FONT}; font-size:clamp(0.8rem, 1.1vw, 1.4rem);">
        📄 {text}
    </div>
    """


def venn_svg(a_fill="none", b_fill="none", ab_fill="none", neither_fill="none") -> str:
    """Circle A overlapping rectangle B inside the Omega card, with each
    of the four regions (A-only, B-only, A intersect B, neither)
    independently colorable to build up the Probability Spaces diagrams."""
    return f"""
    <svg viewBox="0 0 800 460" style="width:100%; height:auto; display:block;">
        <rect x="0" y="0" width="800" height="460" fill="{neither_fill}"/>
        <rect x="300" y="60" width="380" height="340" fill="{b_fill}" stroke="#111" stroke-width="2"/>
        <circle cx="300" cy="230" r="170" fill="{a_fill}" stroke="#111" stroke-width="2"/>
        <clipPath id="vennClip"><rect x="300" y="60" width="380" height="340"/></clipPath>
        <circle cx="300" cy="230" r="170" fill="{ab_fill}" clip-path="url(#vennClip)"
                stroke="{'#111' if ab_fill != 'none' else 'none'}" stroke-width="2"/>
    </svg>
    """


def tex_svg(latex: str, fontsize: float = 30, color: str = "#1a1a1a"):
    """Render a LaTeX expression as an SVG via matplotlib's mathtext,
    instead of marimo's built-in KaTeX. KaTeX renders every equation
    inside a `<marimo-tex>` shadow root, and its subscript/superscript
    sizing classes are hardcoded in `rem` (a deliberate KaTeX choice,
    to stop nested \\small/\\tiny from compounding) -- `rem` always
    resolves against the page's real <html> root, across any shadow
    boundary, so no CSS in this notebook can ever resize them without
    also resizing every other rem-based thing in marimo's own UI
    (tried it -- the whole app looked zoomed in and needed scrolling).
    SVG scales with viewport just like the matplotlib plots elsewhere
    in this deck -- but unlike a plot, an equation must NOT stretch to
    `width:100%` of whatever column it happens to sit in: a short
    equation ("y_1/2 = F^-1(0.5)") in a generously-wide column would
    blow up comically large just to fill space it was never sized
    for. Instead the SVG's *height* is set to a viewport-relative
    clamp() (same scaling idea as the surrounding text) and width is
    `auto`, so the browser derives width from the SVG's own aspect
    ratio -- sized like inline text, not stretched like a figure."""
    _fig = plt.figure(figsize=(0.1, 0.1))
    _fig.text(0.5, 0.5, f"${latex}$", fontsize=fontsize, color=color, ha="center", va="center")
    _buf = io.StringIO()
    _fig.savefig(_buf, format="svg", bbox_inches="tight", pad_inches=0.08, transparent=True)
    plt.close(_fig)
    _svg = _buf.getvalue()
    _height = f"clamp({fontsize * 0.08:.2f}rem, {fontsize * 0.16:.2f}vw, {fontsize * 0.22:.2f}rem)"
    _svg = _svg.replace(
        "<svg ",
        f'<svg style="height:{_height}; width:auto; max-width:100%; display:block;" ',
        1,
    )
    return mo.Html(f'<div style="width:fit-content; max-width:100%;">{_svg}</div>')


def tex_inline(latex: str, color: str = "#1a1a1a") -> str:
    """Like tex_svg, but for math that sits *inside* a sentence
    (e.g. "if $A \\subset B$ then ..."), not on its own line. Returns
    a raw HTML string -- splice it into an f-string passed to mo.md()
    -- rather than a mo.Html object, since it has to flow inline with
    surrounding markdown text rather than stand alone.

    Sized in `em` so it inherits whatever font-size context it's
    dropped into (matching --slide-body's own vw-based scaling
    automatically). Fractions render with a much taller natural
    bounding box than flat expressions at the *same* fontsize (the
    numerator/bar/denominator stack vertically) -- an earlier version
    of this function set a single fixed `height:Nem`, which forced
    fractions and flat expressions to the same overall box height and
    therefore squashed fraction *glyphs* noticeably smaller than
    everything else on the line. Sizing by `width` instead, scaled
    against the font's own content-independent nominal em-box (not
    against this particular expression's bounding box), keeps
    glyph size consistent across expressions while still letting
    fractions render taller than flat text -- exactly like inline
    math looks in print."""
    _dpi = 100
    _fontsize = 30
    _fig = plt.figure(figsize=(0.1, 0.1), dpi=_dpi)
    # va='baseline' anchors (0.5, 0.5) to the expression's own
    # typographic baseline (of its base symbol, e.g. the integral
    # sign itself, ignoring how far sub/superscripts extend below
    # it) -- needed below to work out how far to shift the box so
    # that baseline, not the box's bounding edge, lines up with the
    # surrounding text's baseline.
    _text = _fig.text(0.5, 0.5, f"${latex}$", fontsize=_fontsize, color=color, ha="center", va="baseline")
    _fig.canvas.draw()
    _bbox = _text.get_window_extent(renderer=_fig.canvas.get_renderer())
    _buf = io.StringIO()
    _fig.savefig(_buf, format="svg", bbox_inches="tight", pad_inches=0.02, transparent=True)
    plt.close(_fig)
    _svg = _buf.getvalue()
    _svg = _re.sub(r"<\?xml.*?\?>\s*", "", _svg)
    _svg = _re.sub(r"<!DOCTYPE.*?>\s*", "", _svg, flags=_re.DOTALL)
    # marimo's markdown renderer sanitizes inline HTML and strips
    # <style> tags -- but leaves their *text content* behind as
    # visible plain text rather than removing it too. matplotlib's
    # SVG output always includes a boilerplate <defs><style>...
    # stroke-linecap/linejoin block; drop it before embedding inline
    # (mathtext glyphs are filled paths, not stroked, so it's purely
    # cosmetic boilerplate to begin with).
    _svg = _re.sub(r"<style[^>]*>.*?</style>", "", _svg, flags=_re.DOTALL)
    _ref_h = _fontsize * _dpi / 72  # content-independent nominal em-box, in px
    _target_em = 1.2  # calibrated against surrounding body text by eye
    _width_em = (_bbox.width / _ref_h) * _target_em
    # Browsers default an inline-block's *bottom edge* to the parent
    # baseline. Our expression's actual baseline usually sits above
    # that bottom edge (by however far descenders/subscripts extend
    # below it, e.g. the "min" in an integral's lower bound) -- shift
    # the whole box down by exactly that distance, converted to the
    # same em unit as the width above, so the baselines coincide
    # instead of the box's arbitrary bottom edge.
    _anchor_px = 0.5 * (0.1 * _dpi)
    _descent_px = _anchor_px - _bbox.y0
    _descent_em = _descent_px * _width_em / _bbox.width
    _svg = _svg.replace(
        "<svg ",
        f'<svg style="width:{_width_em:.3f}em; height:auto; vertical-align:{-_descent_em:.3f}em; display:inline-block;" ',
        1,
    )
    # Collapse to a single line: if the (multi-line, pretty-printed)
    # SVG's opening tag lands at the start of a markdown source line
    # -- likely once spliced into a wrapped f-string -- CommonMark
    # reads that as a raw HTML *block* (verbatim, unparsed) rather
    # than inline content, printing the tag as literal text instead
    # of rendering it. A single line can never trigger that.
    _svg = _re.sub(r"\s+", " ", _svg).strip()
    return _svg


def responsive_fig(fig):
    """Export a matplotlib figure as SVG that scales with its container."""
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    svg = buf.getvalue()
    plt.close(fig)
    svg = svg.replace("<svg ", '<svg style="width:100%; height:auto; display:block;" ', 1)
    return mo.Html(f'<div style="width:100%;">{svg}</div>')
