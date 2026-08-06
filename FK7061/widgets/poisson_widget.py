import marimo

__generated_with = "0.23.16"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    import io

    HEAD_FONT = "-apple-system, 'Helvetica Neue', Arial, sans-serif"

    def h1(text: str) -> str:
        return f'<div style="font-family:{HEAD_FONT}; font-weight:800; font-size:2rem; color:#111; margin-bottom:0.4rem;">{text}</div>'

    def responsive_fig(fig):
        buf = io.StringIO()
        fig.savefig(buf, format="svg", bbox_inches="tight")
        svg = buf.getvalue()
        plt.close(fig)
        svg = svg.replace("<svg ", '<svg style="width:100%; height:auto; display:block;" ', 1)
        return mo.Html(f'<div style="width:100%;">{svg}</div>')

    return HEAD_FONT, h1, mo, np, plt, responsive_fig, stats


@app.cell
def _(mo):
    # Widget in its own cell, no bare display — keeps it out of the visible output
    lam_slider = mo.ui.slider(0.5, 15, value=4, step=0.5, label="λ")
    return (lam_slider,)


@app.cell
def _(h1, lam_slider, mo, np, plt, responsive_fig, stats):
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


if __name__ == "__main__":
    app.run()
