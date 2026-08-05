import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="full",
    layout_file="layouts/lecture2_marimo_demo.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    import io
    from textwrap import dedent

    # --- Shared styling to match the Keynote deck (Helvetica Neue, black text) ---
    HEAD_FONT = "-apple-system, 'Helvetica Neue', Arial, sans-serif"

    # Type sizes are viewport-relative (vw) so they grow in marimo's native
    # fullscreen. `rem` is tied to the root font-size, which fullscreen does
    # not change — that's why the deck used to keep laptop-sized text on a
    # projector. clamp() keeps it readable in a small window too.
    H1_SIZE = "clamp(1.6rem, 2.6vw, 5rem)"
    H2_SIZE = "clamp(0.95rem, 1.4vw, 2.6rem)"

    def slide_style(body: str) -> str:
        return f"""
        <div style="font-family:{HEAD_FONT}; padding: 2rem 3rem;">
        {body}
        </div>
        """

    def h1(text: str) -> str:
        return f'<div style="font-family:{HEAD_FONT}; font-weight:800; font-size:{H1_SIZE}; color:#111; line-height:1.15; margin-bottom:0.6rem;">{text}</div>'

    def h2(text: str) -> str:
        return f'<div style="font-family:{HEAD_FONT}; font-weight:700; font-size:{H2_SIZE}; color:#111; margin-top:-0.3rem;">{text}</div>'

    def bullet_slide(tag: str, heading: str, body_md: str, image_html=None) -> None:
        """Two-column: tag + heading + bullet/markdown body on the left,
        an optional image or figure on the right. Matches the
        'Lecture N / Heading / list' layout used throughout the deck."""
        # Headings go through mo.Html, NOT mo.md: mixing raw <div>s and an
        # indented markdown body in one mo.md() makes the dedent leave 4
        # spaces on the div lines, which markdown then renders as a code
        # block (i.e. the HTML shows up as text on the slide).
        left = mo.vstack(
            [mo.Html(h2(tag) + h1(heading)), mo.md(dedent(body_md).strip())],
            gap=0.25,
            align="stretch",
        )
        if image_html is not None:
            return mo.hstack([left, image_html], widths=[1, 1], align="start", gap=2)
        return left

    def responsive_fig(fig):
        """Export a matplotlib figure as SVG and force it to scale with its
        container (width:100%; height:auto), rather than sitting at a fixed
        pixel size that ignores fullscreen/slide dimensions."""
        buf = io.StringIO()
        fig.savefig(buf, format="svg", bbox_inches="tight")
        svg = buf.getvalue()
        plt.close(fig)
        svg = svg.replace("<svg ", '<svg style="width:100%; height:auto; display:block;" ', 1)
        return mo.Html(f'<div style="width:100%;">{svg}</div>')

    return bullet_slide, h1, mo, np, plt, responsive_fig, stats


@app.cell
def _(mo):
    # Slide 1 — title, untouched passthrough image
    mo.image(src="images/title_slide.png", width="100%")
    return


@app.cell
def _(bullet_slide, mo):
    # Extra demo slide — "Lecture 2 / Outline", ported natively (no image
    # export needed — it's pure text/bullets, editable directly, no
    # Keynote round-trip needed for small text changes).
    bullet_slide(
        tag="Lecture 2",
        heading="Outline",
        body_md="""
        1. Common Probability Distributions
            - a. Uniform
            - b. Normal
            - c. Exponential
            - d. Binomial
            - e. Poisson
        2. Central Limit Theorem
        3. Multivariate Probability Distributions
        """,
        image_html=mo.image(src="images/title_slide.png", width="100%"),
    )
    return


@app.cell
def _(mo):
    # Widget defined in its own cell (no visible output → no extra slide),
    # so only the cell below — title + slider + plot together — renders as a slide.
    lam_slider = mo.ui.slider(0.5, 15, value=4, step=0.5, label="λ")
    return (lam_slider,)


@app.cell
def _(h1, lam_slider, mo, np, plt, responsive_fig, stats):
    # Slide 2 — The Poisson Distribution, rebuilt + interactive
    k = np.arange(0, 21)
    pmf = stats.poisson.pmf(k, lam_slider.value)

    fig, ax = plt.subplots(figsize=(5, 4.2))
    ax.plot(k, pmf, color="gray", lw=1, zorder=1)
    ax.scatter(k, pmf, color="#7B3FA0", edgecolor="black", s=45, zorder=2)
    ax.set_xlabel("k")
    ax.set_ylabel("P(x = k)")
    ax.set_ylim(0, 0.42)
    ax.set_xlim(-0.5, 20.5)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()

    left = mo.md(
        f"""
        {h1("The Poisson Distribution")}

        The limit of the Binomial distribution when the number of trials is very
        large, and the success rate is very small, λ ≡ Np

        $$f(k;\\lambda) = P(X=k) = \\dfrac{{\\lambda^k e^{{-\\lambda}}}}{{k!}}$$

        $$E[x] = \\lambda \\qquad V[x] = \\lambda$$

        {lam_slider}

        **λ = {lam_slider.value}**
        """
    )

    mo.hstack([left, responsive_fig(fig)], widths=[1, 1], align="center", gap=2)
    return


@app.cell
def _(mo):
    # Widget defined in its own cell (no visible output → no extra slide)
    mu_slider = mo.ui.slider(-4, 4, value=0, step=0.5, label="μ")
    sigma_slider = mo.ui.slider(0.2, 5, value=1, step=0.1, label="σ²")
    return mu_slider, sigma_slider


@app.cell
def _(h1, mo, mu_slider, np, plt, responsive_fig, sigma_slider, stats):
    # Slide 3 — The Gaussian Distribution, rebuilt + interactive
    x = np.linspace(-8, 8, 400)
    sigma = np.sqrt(sigma_slider.value)
    y = stats.norm.pdf(x, mu_slider.value, sigma)

    fig2, ax2 = plt.subplots(figsize=(5, 4.2))
    ax2.plot(x, y, color="#1f4fd6", lw=2.5)
    ax2.set_xlabel("x")
    ax2.set_ylabel("φ(x; μ, σ²)")
    ax2.set_ylim(0, 1.05)
    ax2.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()

    left2 = mo.md(
        f"""
        {h1("The Gaussian Distribution")}

        Also known as Normal Distribution. Example: heights of people in a room.

        $$f(x) = \\dfrac{{1}}{{\\sigma\\sqrt{{2\\pi}}}} e^{{-\\frac{{1}}{{2}}\\left(\\frac{{x-\\mu}}{{\\sigma}}\\right)^2}}$$

        $$E[x] = \\mu \\qquad V[x] = \\sigma^2$$

        {mu_slider}

        {sigma_slider}
        """
    )

    mo.hstack([left2, responsive_fig(fig2)], widths=[1, 1], align="center", gap=2)
    return


if __name__ == "__main__":
    app.run()
