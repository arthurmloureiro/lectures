import marimo

__generated_with = "0.23.16"
app = marimo.App(
    width="full",
    layout_file="layouts/lecture1_marimo_demo.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
    from scipy.special import hermite
    from textwrap import dedent

    from slide_helpers import (
        bullet_slide,
        h1,
        h2,
        notes_tag,
        omega_card,
        responsive_fig,
        tex_inline,
        tex_svg,
        title_only_slide,
        venn_svg,
    )

    # matplotlib's mathtext doesn't support LaTeX's \color macro (each
    # tex_svg() call is a single flat color), so the per-term color-coding
    # from the original KaTeX version now lives only in BAYES_LABELS_MD.
    BAYES_EQUATION = tex_svg(r"P(A\,|\,B) = \dfrac{P(B\,|\,A)P(A)}{P(B)}", fontsize=34)
    BAYES_LABELS_MD = """
    <span style="color:#F5821F">Posterior Distribution</span> &nbsp;&nbsp;
    <span style="color:#39B54A">Likelihood</span> &nbsp;&nbsp;
    <span style="color:#A31E33">Prior</span> &nbsp;&nbsp;
    <span style="color:#29ABE2">Evidence</span>
    """

    AXIOM1_EQUATION = tex_svg(r"\sum_{\forall E \in \Omega} P(E) = P(\Omega) = 1", fontsize=32)
    AXIOM2_EQUATION = tex_svg(r"\forall A \subseteq \Omega,\ P(A) \geq 0", fontsize=32)
    AXIOM3_EQUATION = tex_svg(r"P(A \cup B) = P(A) + P(B)", fontsize=32)
    return (
        AXIOM1_EQUATION,
        AXIOM2_EQUATION,
        AXIOM3_EQUATION,
        BAYES_EQUATION,
        BAYES_LABELS_MD,
        bullet_slide,
        dedent,
        h1,
        h2,
        mo,
        notes_tag,
        np,
        plt,
        responsive_fig,
        stats,
        tex_inline,
        tex_svg,
    )


@app.cell
def _(h1, mo):
    # Slide 1 -- Title
    mo.vstack(
        [
            mo.hstack(
                [
                    mo.image(src="images/title_dice_sketch.png", width="clamp(90px, 9vw, 220px)"),
                    mo.image(src="images/su_logo.png", width="clamp(55px, 5.5vw, 140px)"),
                ],
                justify="space-between",
                align="start",
            ),
            mo.Html(h1("Statistical Methods in Physics")),
            mo.md(
                """
                <p style="font-size: clamp(1rem, 2vw, 1.5rem);">
                <strong>FK7061 - Fall 2026</strong><br/>
                Lecturers: Jens Jasche, Arthur Loureiro // T.A.: Antoine Gilles Lordet
                </p>
                """
            ),
        ],
        gap=1.5,
    )

    # mo.vstack(
    #     [
    #         mo.hstack(
    #             [
    #                 mo.image(src="images/title_dice_sketch.png", width="clamp(90px, 9vw, 220px)"),
    #                 mo.image(src="images/su_logo.png", width="clamp(55px, 5.5vw, 140px)"),
    #             ],
    #             justify="space-between",
    #             align="start",
    #         ),
    #         mo.md("""<h1 style="font-size: clamp(2rem, 5vw, 80px);">Statistical Methods in Physics</h1>"""),
    #         mo.md(
    #             """
    #             <p style="font-size: clamp(1rem, 2vw, 1.5rem);">
    #             <strong>FK7061 - Fall 2026</strong><br/>
    #             Lecturers: Jens Jasche, Arthur Loureiro // T.A.: Antoine Gilles Lordet
    #             </p>
    #             """
    #         ),
    #     ],
    #     gap=1.5,
    # )
    return


@app.cell
def _(h1, mo):
    # Slide 2 -- FK7061 Evaluation Quiz (text only, no image)
    mo.vstack(
        [
            mo.Html(h1("FK7061 Evaluation Quiz")),
            mo.md(
                """
                *\\*\\* This quiz will not count towards your grade. However, we ask that you
                take it seriously, as it will be used to help improve this course (and the
                pre-requisite courses) for future course offerings*

                1. What is the difference between a Poisson Distribution and a Normal
                   Distribution? Please provide an example scenario where a set of data
                   would be reasonably fit by both distributions.
                2. How is the Bayesian concept of probability different from a frequentist
                   definition?
                3. Can you state the three Kolmogorov axioms of probability, e.g., what
                   properties do probabilities possess?
                4. Can you write Bayes' law and comment on the prior probability used in
                   Bayesian statistics?

                **Survey questions:**

                - Have you taken a statistics class (at the undergraduate or graduate
                  level) before this course? If so, please specify the university and
                  level that the class was taken at?
                - What degree/specification are you pursuing at Stockholm University?
                  Are you enrolled here, or as an ERASMUS student from another university?
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 3 -- Work Plan
    bullet_slide(
        tag="",
        heading="Work Plan",
        body_md="""
        **The Frequentist Portion**

        - **Lecture 1:** Introduction
        - **Lecture 2:** Probability Distributions
        - **Lecture 3:** Propagation of Errors, Covariances
        - **Lecture 4:** The Likelihood -- Part 1
        - **Lecture 5:** The Likelihood -- Part 2
        - **Lecture 6:** Method of Least Squares
        - **Lecture 7:** Confidence Intervals -- Part 1
        - **Lecture 8:** Confidence Intervals -- Part 2
        - **Lecture 9:** Hypothesis Testing
        """,
        image_html=mo.image(src="images/workplan_bellcurve_neon.png", width="100%"),
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 4 -- Lecture 1 Outline
    bullet_slide(
        tag="Outline",
        heading="Lecture 1",
        body_md="""
        1. What is probability?
            - Popular definitions
            - Kolmogorov's Axioms
        2. Random Variables
        3. Probability Density Functions and Cumulative Distribution Functions
        4. Mean and Standard Deviations
        5. Interpretations of Probability
            - Frequentist
            - Bayesian
        """,
        image_html=mo.image(src="images/outline_bayesian_vs_frequentist.png", width="100%"),
    )
    return


@app.cell
def _(mo):
    # Slide 5 -- centered discussion question, no image/bullets
    mo.Html(
        """
        <div style="display:flex; align-items:center; justify-content:center;
                    height:60vh; text-align:center; font-family:-apple-system,
                    'Helvetica Neue', Arial, sans-serif;">
            <div style="font-weight:800; font-size:clamp(1.6rem, 3.2vw, 5rem);
                        color:#111; line-height:1.3;">
                What is your definition of<br>probability?
            </div>
        </div>
        """
    )
    return


@app.cell
def _(mo):
    # Slide 6 -- section divider: "Kolmogorov's Axioms" with a two-circle Venn motif
    mo.Html(
        """
        <div style="display:flex; flex-direction:column; align-items:center;
                    justify-content:center; font-family:-apple-system, 'Helvetica Neue',
                    Arial, sans-serif; height:60vh; text-align:center;">

            <!-- Venn diagram circles -->
            <div style="position:relative; width:320px; height:180px; margin-bottom:2rem;">
                <div style="position:absolute; left:0; top:0; width:200px; height:200px;
                            border-radius:50%; background:#E0459B; opacity:0.75;"></div>
                <div style="position:absolute; left:80px; top:0; width:200px; height:200px;
                            border-radius:50%; background:#2E9FE8; opacity:0.75;
                            mix-blend-mode:multiply;"></div>
            </div>

            <!-- Title text -->
            <div style="font-weight:800; font-size:clamp(1.6rem, 2.6vw, 5rem); color:#111;">
                Kolmogorov's Axioms
            </div>
        </div>
        """
    )
    return


@app.cell
def _(AXIOM1_EQUATION, h1, h2, mo):
    # Slide 8 -- Axiom #1, with the plain-language quote revealed
    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                r"""
                                **Axiom #1** (First axiom of probability calculus): *Given that $\Omega$
                                is the universe of all possible outcomes of an experiment or the sample
                                space. The joint probability of all true events in $\Omega$ must be
                                maximal:*
                                """
                            ),
                            mo.center(AXIOM1_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # Right: image
                    mo.center(
                        mo.image(src="images/kolmogorov_omega_space_empty.png", width=800)
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(AXIOM1_EQUATION, h1, h2, mo):
    # Slide 8 -- Axiom #1, with the plain-language quote revealed
    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                r"""
                                **Axiom #1** (First axiom of probability calculus): *Given that $\Omega$
                                is the universe of all possible outcomes of an experiment or the sample
                                space. The joint probability of all true events in $\Omega$ must be
                                maximal:*
                                """
                            ),
                            mo.center(AXIOM1_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # Right: image
                    mo.center(
                        mo.Html(
                            """
                            <div style="border: 2px solid #111; border-radius: 0.5rem;
                                        padding: 2rem 3rem; background: #111;
                                        font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
                                        font-size: 2rem; font-weight: 800; color: #fff;
                                        text-align: center; min-width: 400px;">
                                "Something has to happen"
                            </div>
                            """
                        )
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(AXIOM2_EQUATION, h1, h2, mo):
    # Slide 9 -- Axiom #2, first reveal
    # mo.vstack(
    #     [
    #         mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),
    #         mo.md("""**Axiom #2** (Second axiom of probability calculus):"""),
    #         AXIOM2_EQUATION,
    #     ],
    #     gap=0.5,
    # )

    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                r"""
                                **Axiom #2** (Second axiom of probability calculus):
                                """
                            ),
                            mo.center(AXIOM2_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # Right: image
                    mo.center(
                        mo.image(src="images/kolmogorov_omega_A.png", width=800)
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(AXIOM2_EQUATION, h1, h2, mo):
    # Slide 10 -- Axiom #2, with quote
    # Slide 9 -- Axiom #2, first reveal
    # mo.vstack(
    #     [
    #         mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),
    #         mo.md("""**Axiom #2** (Second axiom of probability calculus):"""),
    #         AXIOM2_EQUATION,
    #     ],
    #     gap=0.5,
    # )

    # Slide 8 -- Axiom #1, with the plain-language quote revealed
    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                r"""
                                **Axiom #2** (Second axiom of probability calculus):
                                """
                            ),
                            mo.center(AXIOM2_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # quote
                    mo.center(
                        mo.Html(
                            """
                            <div style="border: 2px solid #111; border-radius: 0.5rem;
                                        padding: 2rem 3rem; background: #111;
                                        font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
                                        font-size: 2rem; font-weight: 800; color: #fff;
                                        text-align: center; min-width: 400px;">
                                "The probability of an even can <i>never</i> be negative!"
                            </div>
                            """
                        )
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(AXIOM3_EQUATION, h1, h2, mo, tex_inline):
    # Slide 11 -- Axiom #3, first reveal
    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                f"""
                                 **Axiom #3** (Third axiom of probability calculus): if
                                 {tex_inline(r"A, B \subseteq \Omega")} and
                                 {tex_inline(r"A \cap B = \emptyset")}, then: 
                                 """
                            ),
                            mo.center(AXIOM3_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # Right: image
                    mo.center(
                        mo.image(src="images/kolmogorov_omega_A_B.png", width=800)
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(AXIOM3_EQUATION, h1, h2, mo, tex_inline):
    # Slide 12 -- Axiom #3, with quote
    # mo.vstack(
    #     [
    #         mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),
    #         mo.Html(omega_card()),
    #         mo.md(
    #             f"""
    #             **Axiom #3** (Third axiom of probability calculus): *if
    #             {tex_inline(r"A, B \subseteq \Omega")} and
    #             {tex_inline(r"A \cap B = \emptyset")}, then
    #             {tex_inline(r"P(A \cup B) = P(A) + P(B)")}*

    #             #### "Probabilities of different (disjoint) events add"
    #             """
    #         ),
    #     ],
    #     gap=0.5,
    # )
    mo.vstack(
        [
            mo.Html(h1("Kolmogorov's Axioms") + h2("Probability Calculus")),

            # Box on the left, image on the right
            mo.hstack(
                [
                    # Left: Axiom #1 text + centered equation inside a styled box
                    mo.vstack(
                        [
                            mo.md(
                                f"""
                                 **Axiom #3** (Third axiom of probability calculus): if
                                 {tex_inline(r"A, B \subseteq \Omega")} and
                                 {tex_inline(r"A \cap B = \emptyset")}, then: 
                                 """
                            ),
                            mo.center(AXIOM3_EQUATION),
                        ],
                        gap=0.5,
                    ).style({
                        "border": "2px solid #2E9FE8",
                        "border-radius": "0.5rem",
                        "padding": "1rem 1.5rem",
                        "background": "#f0f8ff",
                    }),

                    # Right: quote
                    mo.center(
                        mo.Html(
                            """
                            <div style="border: 2px solid #111; border-radius: 0.5rem;
                                        padding: 2rem 3rem; background: #111;
                                        font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
                                        font-size: 2rem; font-weight: 800; color: #fff;
                                        text-align: center; min-width: 400px;">
                                "The probabilities of different (disjoint) events add"
                            </div>
                            """
                        )
                    ),
                ],
                widths=[1, 1],  # equal widths; adjust e.g. [2, 1] to give more space to the box
                align="center",
                gap=1.0,
            ),

           # mo.md("""#### "Something has to happen" """),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(dedent, h1, h2, mo, notes_tag):
    # Slide 13 -- Random Variables: definition + dice photo
    # bullet_slide(
    #     tag="",
    #     heading="Random Variables",
    #     body_md="""
    #     A measurable function defined on a probability space (which obeys the
    #     Kolmogorov axioms)
    #     """,
    #     image_html=mo.vstack(
    #         [
    #             mo.image(src="images/random_variables_dice_photo.png", width="100%"),
    #             mo.Html(notes_tag("See Lecture 1 Notes, pg 1")),
    #         ]
    #     ),
    # )
    left_col = mo.vstack(
        [
            mo.Html(h2("") + h1("Random Variables")),
            mo.md(dedent("""
                A measurable function defined on a probability space (which obeys the
                Kolmogorov axioms)
            """).strip()),
            # Notes tag pinned to bottom-left, inline-block so it hugs its content
            mo.Html(
                f"""<div style="text-align:left;">
                    {notes_tag("See Lecture 1 Notes, pg 1")}
                </div>"""
            ),
        ],
        gap=0.25,
        align="stretch",
        justify="space-between",
    )

    mo.hstack(
        [
            left_col,
            mo.image(src="images/random_variables_dice_photo.png", width="100%"),
        ],
        widths=[1, 1],
        align="start",
        gap=2,
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 14 -- Random Variables: discrete example (sum of two dice)
    bullet_slide(
        tag="",
        heading="Random Variables",
        body_md="""
        Random variables can be **discrete** or continuous
        """,
        image_html=mo.image(src="images/dice_sum_histogram.png", width="100%"),
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 15 -- Random Variables: discrete + continuous side by side
    bullet_slide(
        tag="",
        heading="Random Variables",
        body_md="""
        Random variables can be discrete or **continuous**
        """,
        image_html=mo.image(src="images/maxwell_boltzmann_speed.png", width="100%"),
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 16 -- Random Variables: "in between" (global income distribution)
    bullet_slide(
        tag="",
        heading="Random Variables",
        body_md="""
        Or in between...
        """,
        image_html=mo.image(src="images/global_income_distribution.png", width="120%"),
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 17 -- Random Variables: multidimensional (Higgs event display)
    bullet_slide(
        tag="",
        heading="Random Variables",
        body_md="""
        Random variables can be multidimensional (Lecture 3)
        """,
        image_html=mo.image(src="images/higgs_event_display.png", width="100%"),
    )
    return


@app.cell
def _(h1, mo, tex_inline):
    # Slide 18 -- Some Nomenclature and Notation (text only)
    mo.vstack(
        [
            mo.Html(h1("Some Nomenclature and Notation")),
            mo.md(
                rf"""
                - {tex_inline(r"\Omega")} $\rightarrow$  {{the set of all possible events}}
                - {tex_inline(r"A \cup B")} $\rightarrow$  {{all events that are in either A **or** B}}: [*union*]
                - {tex_inline(r"A \cap B")} $\rightarrow$ {{all events that are in A **and** B}}:  [*intersection*]
                - {tex_inline(r"A \subset B")} $\rightarrow$ {{all events in A are also in B; A is a **subset of** B}}:  [*contained in*]
                - {tex_inline(r"A^C")} or {tex_inline(r"\bar{A}")} $\rightarrow$ {{all events that are **not** in A}}: [*complement*]
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(mo):
    # Slide 19 -- Probability Spaces, first fact: P(Omega) = 1
    mo.image(src="images/probability_spaces/probability_spaces.001.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 20 -- Probability Spaces, new blank diagram (about to build up A, B)
    mo.image(src="images/probability_spaces/probability_spaces.002.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 21 -- Probability Spaces: A space
    mo.image(src="images/probability_spaces/probability_spaces.003.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 22 -- Probability Spaces: B space
    mo.image(src="images/probability_spaces/probability_spaces.004.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 23 -- Probability Spaces: B space with Equation
    mo.image(src="images/probability_spaces/probability_spaces.005.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 24 -- Probability Spaces: B space with Equation - answer
    mo.image(src="images/probability_spaces/probability_spaces.006.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 25 -- + A intersect B (green)
    mo.image(src="images/probability_spaces/probability_spaces.007.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 26 -- + A intersect B (green): answer
    mo.image(src="images/probability_spaces/probability_spaces.008.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 27 -- + B intersect A-complement (tan)
    mo.image(src="images/probability_spaces/probability_spaces.009.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 28 -- + B intersect A-complement (tan) answer
    mo.image(src="images/probability_spaces/probability_spaces.010.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 27 -- + A intersect B-complement (red): question
    mo.image(src="images/probability_spaces/probability_spaces.011.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 28 -- + A intersect B-complement (red): answer
    mo.image(src="images/probability_spaces/probability_spaces.012.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 29 -- + everything outside A union B (blue) question
    mo.image(src="images/probability_spaces/probability_spaces.013.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 29 -- + everything outside A union B (blue) answer
    mo.image(src="images/probability_spaces/probability_spaces.014.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 29 -- same diagram + the closing sum-to-one equation
    mo.image(src="images/probability_spaces/probability_spaces.015.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 30 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.001.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 31 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.002.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 32 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.003.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 33 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.004.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 34 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.005.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 35 -- If A subset B, then P(A intersect B) = P(A)
    mo.image(src="images/probability_spaces_2/probability_spaces_2.009.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 36 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.001.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 37 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.003.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 38 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.004.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.005.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.006.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.007.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.008.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.009.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.010.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.011.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.012.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.013.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.014.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.015.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.016.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.017.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.018.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.019.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.020.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.021.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.022.png", width="100%")
    return


@app.cell
def _(mo):
    # Slide 39 -- Dependent and Independent Events (definition)
    mo.image(src="images/dep_indep_events/dep_indep_events.023.png", width="100%")
    return


@app.cell
def _(h1, mo, notes_tag, tex_inline):
    # Slide 34 -- Let's do some simple proofs
    mo.vstack(
        [
            mo.Html(h1("Let's do some simple proofs")),
            mo.md(
                rf"""
                - Exercise I: Prove that if {tex_inline(r"A \subset B")}, then {tex_inline(r"P(A) \leq P(B)")}
                """
            ),
            #mo.Html(notes_tag("See Lecture 1 Notes, pg 1")),
            mo.Html(
                f"""<div style="text-align:left;">
                    {notes_tag("See Lecture 1 Notes, pg 1")}
                </div>"""
            ),
            mo.md(
                rf"""
                - Exercise II: Prove that {tex_inline(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")}
                """
            ),
            mo.Html(
                f"""<div style="text-align:left;">
                    {notes_tag("See Lecture 1 Notes, pg 2")}
                </div>"""
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(mo):
    # Slide 35 -- Break Time :)
    mo.Html(
        """
        <div style="display:flex; align-items:center; height:70vh;
                    font-family:-apple-system, 'Helvetica Neue', Arial, sans-serif;">
            <div style="font-weight:800; font-size:clamp(1.6rem, 3.2vw, 5rem); color:#111;">
                Break Time :)
            </div>
        </div>
        """
    )
    return


@app.cell
def _(h1, mo, notes_tag):
    # Slide 36 -- Dropping the Bayes (section divider)
    mo.hstack(
        [
            # Left: existing content
            mo.vstack(
                [
                    mo.Html(h1("Dropping the Bayes")),
                    mo.Html(
                        f"""<div style="text-align:left;">
                            {notes_tag("See Lecture 1 Notes, pg 2")}
                        </div>"""
                    ),
                ],
                gap=0.5,
            ),

            # Right: image
            mo.center(
                mo.image(src="images/bayes_drop.png", width="50%")
            ),
        ],
        widths=[1, 1],  # adjust e.g. [2, 1] to give more space to the left
        align="center",
        gap=1.0,
    )
    return


@app.cell
def _(BAYES_EQUATION, BAYES_LABELS_MD, h1, mo):
    # Slide 37 -- Bayes' Theorem, first reveal with term explanations
    mo.vstack(
        [
            mo.Html(h1("Bayes' Theorem")),
            BAYES_EQUATION,
            mo.md(BAYES_LABELS_MD),
            mo.md(
                r"""
                - **Likelihood**: likelihood of the data (observation) given A (a
                  parameter we wish to infer). It describes a generative model by
                  which the observation is generated given A.
                - **Prior**: background information we have about A: either
                  reflecting our belief about the parameter or the known
                  prevalence (base rates).
                - **Evidence**: a normalisation factor which can be seen as "the
                  probability of the observation". This is usually ignored but
                  relevant for model comparison!
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(BAYES_EQUATION, BAYES_LABELS_MD, h1, mo):
    # Slide 38 -- Bayes' Theorem, plausibility-update explanation
    mo.vstack(
        [
            mo.Html(h1("Bayes' Theorem")),
            BAYES_EQUATION,
            mo.md(BAYES_LABELS_MD),
            mo.md(
                r"""
                Bayes' Law (or Bayes' Theorem) describes an update of the
                plausibility $P(A)$ to a new posterior degree of plausibility
                $P(A\,|\,B)$ given some new observation $B$.
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(BAYES_EQUATION, BAYES_LABELS_MD, h1, mo):
    # Slide 39 -- Bayes' Theorem, independent-of-Bayesian-statistics note
    mo.vstack(
        [
            mo.Html(h1("Bayes' Theorem")),
            BAYES_EQUATION,
            mo.md(BAYES_LABELS_MD),
            mo.md(r"""Note that Bayes' theorem is independent of Bayesian Statistics!"""),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, mo, tex_inline, tex_svg):
    # Slide 40 -- Probability Density Function
    mo.vstack(
        [
            mo.Html(h1("Probability Density Function")),
            mo.md(f"""Let's define {tex_inline("f(x) \equiv p(x)")} as the density of probabilities in some space."""),
            mo.md("""Hence:"""),
            tex_svg(r"P(a < x < b) = \int_a^b f(x)\,dx", fontsize=34),
            mo.md("""Following Kolmogorov's axioms:"""),
            tex_svg(r"P(-\infty < x < \infty) = \int_{-\infty}^{\infty} f(x)\,dx = 1", fontsize=34),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, mo, notes_tag, np, plt, responsive_fig, tex_inline):
    # Slide 41 -- Cumulative Density Function
    _x = np.linspace(0, 10, 300)
    _fig, _ax = plt.subplots(figsize=(5, 4.5))
    _ax.plot(_x, _x / 10, color="#111", lw=2)
    _ax.plot(_x, 1 - np.exp(-_x / 2), color="#888", lw=2)
    _mixed = np.clip(0.4 * (1 - np.exp(-_x)) + 0.6 * (_x / 10) ** 0.5, 0, 1)
    _ax.plot(_x, _mixed, color="#A31E33", lw=2)
    _ax.set_xlim(0, 10)
    _ax.set_ylim(0, 1.05)
    _ax.set_xticks([0, 10])
    _ax.set_xticklabels([r"$-\infty$", r"$\infty$"])
    _ax.set_yticks([0, 0.5, 1])
    _ax.set_xlabel("x")
    _ax.set_ylabel("CDF")
    _ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()

    mo.vstack(
        [
            mo.hstack(
                [mo.Html(h1("Cumulative Density Function")), 
                 mo.Html(
                        f"""<div style="text-align:left;">
                            {notes_tag("See Lecture 1 Notes, pg 3")}
                        </div>"""
                    )],
                justify="space-between",
            ),
            mo.hstack(
                [
                    mo.md(
                        f"""Let's define {tex_inline(r"F(x) = \int_{-\infty}^{x} f(x')\,dx' \equiv P(x' < x)")} as the cumulative density function"""
                    ),
                    responsive_fig(_fig),
                ],
                widths=[1, 1],
                align="center",
                gap=2,
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, mo, tex_inline):
    # Slide 42 -- Redefining Standard Statistics
    # mo.vstack(
    #     [
    #         mo.Html(h1("Redefining Standard Statistics")),
    #         mo.md("""In terms of PDFs and CDFs"""),
    #         mo.hstack(
    #             [mo.md("**Median:**"), tex_svg(r"y_{1/2} = F^{-1}(0.5)", fontsize=26)],
    #             widths=[1, 2], align="center", gap=1,
    #         ),
    #         mo.hstack(
    #             [mo.md("**Mode:**"), mo.md(r"$\text{argmax}[f(x)]$")],
    #             widths=[1, 2], align="center", gap=1,
    #         ),
    #         mo.hstack(
    #             [
    #                 mo.md("**Mean (expectation value):**"),
    #                 tex_svg(r"\langle x \rangle = \int_{-\infty}^{\infty} x f(x)\,dx", fontsize=24),
    #             ],
    #             widths=[1, 2], align="center", gap=1,
    #         ),
    #     ],
    #     gap=0.8,
    # )

    mo.vstack(
        [
            mo.Html(h1("Redefining Standard Statistics")),
            mo.md("""In terms of PDFs and CDFs"""),
            mo.md(
                rf"""
                - **Median**: {tex_inline(r"y_{1/2} = F^{-1}(0.5)")}
                """
            ),
            mo.md(
                rf"""
                - **Mode**: {tex_inline(r"\text{argmax}[f(x)]")}
                """
            ),
            mo.md(
                rf"""
                - **Mean (expectatio value)**: {tex_inline(r"\langle x \rangle = \int_{-\infty}^{\infty} x f(x)\,dx")}
                """
            ),


        ],
        gap=0.8,
    )
    return


@app.cell
def _(mo):
    mean_slider = mo.ui.slider(start=-5.0, stop=5.0, step=0.1, value=-3.0,
                               label="Expectation (μ)", show_value=True)
    var_slider  = mo.ui.slider(start=0.1, stop=5.0, step=0.1, value=1.0,
                               label="Variance (σ²)", show_value=True)
    return mean_slider, var_slider


@app.cell
def _(
    h1,
    h2,
    mean_slider,
    mo,
    np,
    plt,
    responsive_fig,
    stats,
    tex_svg,
    var_slider,
):
    # # Slide 43 -- Expectation values and Variance: definitions
    # _x = np.linspace(-6, 6, 400)
    # _y = stats.norm.pdf(_x, -3, 1)
    # _fig, _ax = plt.subplots(figsize=(5, 4.2))
    # _ax.plot(_x, _y, color="#1f4fd6", lw=2.5)
    # _ax.set_title("Gaussian Distribution\nMean = -3.00, Variance = 1.00")
    # _ax.set_xlabel("x")
    # _ax.set_ylabel("Probability Density")
    # _ax.spines[["top", "right"]].set_visible(False)
    # plt.tight_layout()

    # mo.vstack(
    #     [
    #         mo.Html(h1("Expectation values and Variance") + h2("Definitions")),
    #         mo.hstack(
    #             [
    #                 mo.vstack(
    #                     [
    #                         mo.md("**Expectation:**"),
    #                         tex_svg(r"E[X] = \mu = \int_{x_{min}}^{x_{max}} x f(x)\,dx", fontsize=32),
    #                         mo.md("**Variance:**"),
    #                         tex_svg(
    #                             r"V[X] = \sigma^2 = E[(X-\mu)^2] = \int_{x_{min}}^{x_{max}} (x-\mu)^2 f(x)\,dx",
    #                             fontsize=32,
    #                         ),
    #                     ],
    #                     gap=0.3,
    #                 ),
    #                 responsive_fig(_fig),
    #             ],
    #             widths=[1, 1],
    #             align="center",
    #             gap=2,
    #         ),
    #     ],
    #     gap=0.5,
    # )

    # Slide 43 -- Expectation values and Variance: definitions
    _mu  = mean_slider.value
    _var = var_slider.value
    _std = np.sqrt(_var)

    _x = np.linspace(-6, 6, 400)
    _y = stats.norm.pdf(_x, _mu, _std)
    _fig, _ax = plt.subplots(figsize=(5, 4.2))
    _ax.plot(_x, _y, color="#1f4fd6", lw=2.5)
    _ax.set_title(f"Gaussian Distribution\nMean = {_mu:.2f}, Variance = {_var:.2f}")
    _ax.set_xlabel("x")
    _ax.set_ylabel("Probability Density")
    _ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()

    mo.vstack(
        [
            mo.Html(h1("Expectation values and Variance") + h2("Definitions")),
            mo.hstack(
                [
                    mo.vstack(
                        [
                            mo.md("**Expectation:**"),
                            tex_svg(r"E[X] = \mu = \int_{x_{min}}^{x_{max}} x f(x)\,dx", fontsize=32),
                            mo.md("**Variance:**"),
                            tex_svg(
                                r"V[X] = \sigma^2 = E[(X-\mu)^2] = \int_{x_{min}}^{x_{max}} (x-\mu)^2 f(x)\,dx",
                                fontsize=32,
                            ),
                        ],
                        gap=0.3,
                    ),
                    mo.vstack(
                    [
                        responsive_fig(_fig),
                        mo.hstack([mean_slider, var_slider], gap=1),
                        ]),
                ],
                widths=[1, 1],
                align="center",
                gap=2,
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, h2, mo, tex_svg):
    # Slide 44 -- Expectation values and Variance: higher-order moments
    mo.vstack(
        [
            mo.Html(h1("Expectation values and Variance") + h2("We can also calculate higher-order moments")),
            mo.md("**Skewness:**"),
            tex_svg(r"S[X] = E[(X-\mu)^3] = \int_{x_{min}}^{x_{max}} (x-\mu)^3 f(x)\,dx", fontsize=32),
            mo.md("**Kurtosis:**"),
            tex_svg(r"K[X] = E[(X-\mu)^4] = \int_{x_{min}}^{x_{max}} (x-\mu)^4 f(x)\,dx", fontsize=32),
        ],
        gap=0.4,
    )
    return


@app.cell
def _(mo):
    # Widget cell for Slide 45 -- kept invisible (assignment only) so it
    # doesn't spawn a phantom slide.
    # skew_slider = mo.ui.slider(-1.5, 1.5, value=0, step=0.1, label="Skewness")
    # kurt_slider = mo.ui.slider(-1.5, 3.0, value=0, step=0.1, label="Excess Kurtosis")

    # Widget cell for Slide 45 -- kept invisible (assignment only) so it
    # doesn't spawn a phantom slide.
    skew_slider = mo.ui.slider(-8, 8, value=0, step=0.5, label="Skewness", show_value=False)
    kurt_slider = mo.ui.slider(0.5, 5.0, value=3.5, step=0.1, label="Excess Kurtosis", show_value=False)
    return kurt_slider, skew_slider


@app.cell
def _(h1, h2, kurt_slider, mo, np, plt, responsive_fig, skew_slider, stats):
    # Slide 45 -- Expectation values and Variance: INTERACTIVE skew/kurtosis
    # Gram-Charlier A expansion: perturb a standard normal by Hermite (He_3,
    # He_4) correction terms weighted by skewness and excess kurtosis. At
    # skew=0, kurtosis=0 this degenerates exactly back to the Gaussian.
    # _x = np.linspace(-6, 6, 400)
    # _phi = stats.norm.pdf(_x)
    # _he3 = _x**3 - 3 * _x
    # _he4 = _x**4 - 6 * _x**2 + 3
    # _skew = skew_slider.value
    # _kurt = kurt_slider.value
    # _f = _phi * (1 + (_skew / 6) * _he3 + (_kurt / 24) * _he4)

    # _fig, _ax = plt.subplots(figsize=(5, 4.2))
    # _ax.plot(_x, _phi, color="#bbb", lw=1.5, ls="--", label="Standard Normal")
    # _ax.plot(_x, _f, color="#1f4fd6", lw=2.5, label="Gram-Charlier")
    # _ax.set_xlabel("x")
    # _ax.set_ylabel("f(x)")
    # _ax.set_ylim(-0.05, 0.5)
    # _ax.legend(frameon=False, loc="upper right")
    # _ax.spines[["top", "right"]].set_visible(False)
    # plt.tight_layout()

    # _left = mo.vstack(
    #     [
    #         skew_slider,
    #         kurt_slider,
    #         mo.md(f"**Skewness = {_skew:.1f}, Excess Kurtosis = {_kurt:.1f}**"),
    #     ],
    #     gap=0.5,
    # )
    # mo.vstack(
    #     [
    #         mo.Html(h1("Expectation values and Variance") + h2("We can also calculate higher-order moments")),
    #         tex_svg(
    #             r"f(x) \approx \varphi(x)\left[1 + \dfrac{S[X]}{6}He_3(x) + \dfrac{K[X]}{24}He_4(x)\right]",
    #             fontsize=28,
    #         ),
    #         mo.hstack([_left, responsive_fig(_fig)], widths=[1, 1], align="center", gap=2),
    #     ],
    #     gap=0.5,
    # )

    # Slide 45 -- Expectation values and Variance: skewness and kurtosis, visually
    # Four sample distributions chosen purely to *look* like the textbook cases:
    # right-skew, left-skew, heavy-tailed (leptokurtic), flat-topped (platykurtic).
    # Students see shape + computed moments, not formulas or distribution names.



    _rng = np.random.default_rng(7)
    _n = 20_000
    _x = np.linspace(-6, 6, 400)

    _alpha = skew_slider.value   # skew-normal shape parameter
    _beta = 5.5 - kurt_slider.value   # inverted: slider increases -> beta decreases -> kurtosis increases  

    # --- Skewness panel: skew-normal, standardised to mean 0, var 1 ---
    _skew_data = stats.skewnorm.rvs(a=_alpha, size=_n, random_state=_rng)
    _skew_data = (_skew_data - _skew_data.mean()) / _skew_data.std()
    _skew_val = stats.skew(_skew_data)

    # --- Kurtosis panel: generalised normal, standardised to mean 0, var 1 ---
    _kurt_data = stats.gennorm.rvs(beta=_beta, size=_n, random_state=_rng)
    _kurt_data = (_kurt_data - _kurt_data.mean()) / _kurt_data.std()
    _kurt_val = stats.kurtosis(_kurt_data)  # excess kurtosis, Fisher convention

    _phi = stats.norm.pdf(_x)

    _fig, _axes = plt.subplots(1, 2, figsize=(8.5, 4.2))

    _axes[0].hist(_skew_data, bins=60, range=(-5, 5), density=True, color="#1f4fd6", alpha=0.75)
    _axes[0].plot(_x, _phi, color="#999", lw=1.5, ls="--")
    _axes[0].set_title(f"Skewness = {_skew_val:.2f}", fontsize=11)
    _axes[0].set_xlim(-5, 5)
    _axes[0].set_yticks([])
    _axes[0].spines[["top", "right", "left"]].set_visible(False)

    _axes[1].hist(_kurt_data, bins=60, range=(-5, 5), density=True, color="#1f4fd6", alpha=0.75)
    _axes[1].plot(_x, _phi, color="#999", lw=1.5, ls="--")
    _axes[1].set_title(f"Excess Kurtosis = {_kurt_val:.2f}", fontsize=11)
    _axes[1].set_xlim(-5, 5)
    _axes[1].set_yticks([])
    _axes[1].spines[["top", "right", "left"]].set_visible(False)

    plt.tight_layout()

    _left = mo.vstack(
        [
            skew_slider,
            kurt_slider,
            mo.md(f"**Skewness = {_skew_val:.2f}, Excess Kurtosis = {_kurt_val:.2f}**"),
        ],
        gap=0.5,
    )
    mo.vstack(
        [
            mo.Html(h1("Expectation values and Variance") + h2("We can also calculate higher-order moments")),
            mo.md("Grey dashed curve is the Normal, for reference. Both samples are standardised to mean 0, variance 1."),
            mo.hstack([_left, responsive_fig(_fig)], widths=[1, 1], align="center", gap=2),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, mo, tex_svg):
    # Slide 46 -- Characteristic Functions
    mo.vstack(
        [
            mo.Html(h1("Characteristic Functions")),
            mo.md("""- Essentially the Fourier transform of the probability distribution function:"""),
            mo.center(tex_svg(r"\phi_X(t) = \int_{-\infty}^{\infty} e^{itx} f(x)\,dx", fontsize=36)),
            mo.md(
                """
                - This can be used to describe and differentiate between different classes of
                  probability density functions.
                """
            ),
        ],
        gap=1.5,
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 47 -- Expectation Values on Probability Space (intro)
    bullet_slide(
        tag="",
        heading="Expectation Values",
        body_md="""
        **on Probability Space**

        - Earlier on, we showed that you can calculate different moments and
          characteristic functions on a probability space.
        - Even more generically - You can calculate the expectation value of
          any function on a probability space
        """,
        image_html=mo.image(src="images/workplan_bellcurve_neon.png", width="100%"),
    )
    return


@app.cell
def _(bullet_slide, mo, notes_tag, tex_inline):
    # Slide 48 -- Expectation Values on Probability Space (worked example)
    bullet_slide(
        tag="",
        heading="Expectation Values",
        body_md=f"""
        **on Probability Space**

        **Example:** Let's assume that cars are speeding on a street, and the
        velocity that they are moving (over the speed limit) is given by:

        {tex_inline(r"f(x) = \dfrac{c}{x}, \quad 1 \leq x \leq 10")}

        There are police officers that might pull these cars over, maybe
        multiple times! How likely this is depends on the cars speed,
        following a function:

        {tex_inline(r"g(x) = \dfrac{1}{200}x^2")}

        How many times does the average car get pulled over?
        """,
        image_html=mo.vstack(
            [
                mo.image(src="images/police_speeding_neon.png", width="100%"),
                mo.Html(
                f"""<div style="text-align:right;">
                    {notes_tag("See Lecture 1 Notes, pg 3")}
                </div>"""
            ),
            ]
        ),
    )
    return


@app.cell
def _(h1, mo, notes_tag, tex_svg):
    # Slide 49 -- Expectation Values on Probability Space (the integral)
    mo.vstack(
        [
            mo.hstack(
                [mo.Html(h1("Expectation Values") ), 
                 mo.Html(
                f"""<div style="text-align:left;">
                    {notes_tag("See Lecture 1 Notes, pg 3")}
                </div>"""
            )],
                justify="space-between",
            ),
            mo.md(r"""**on Probability Space**"""),
            tex_svg(r"E[g(x)] = \int_{-\infty}^{\infty} g(x) f(x)\,dx", fontsize=38),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 50 -- Popular Probability
    bullet_slide(
        tag="",
        heading="Popular Probability",
        body_md="""
        **How would you describe these probabilities to a friend?**

        - **Frequentist:** Our Model, repeated many times, will include the
          real value most* of the time.
        - 
        """,
        image_html=mo.image(src="images/weather_forecast_screenshot.png", width="70%"),
    )
    return


@app.cell
def _(bullet_slide, mo):
    # Slide 50 -- Popular Probability
    bullet_slide(
        tag="",
        heading="Popular Probability",
        body_md="""
        **How would you describe these probabilities to a friend?**

        - **Frequentist:** Our Model, repeated many times, will include the
          real value most* of the time.
        - **Bayesian:** Expression of our ignorance, given our current Model
          and our prior knowledge.
        """,
        image_html=mo.image(src="images/weather_forecast_screenshot.png", width="70%"),
    )
    return


@app.cell
def _(h1, mo, tex_inline):
    # Slide 51 -- Interpretations of Statistics: the fundamental problem
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics")),
            mo.md(
                rf"""
                **The Fundamental Problem:**

                We can measure {tex_inline(r"P(\text{Data}\,|\,\text{Model 1})")} and
                {tex_inline(r"P(\text{Data}\,|\,\text{Model 2})")} – but what we really want to know is
                {tex_inline(r"P(\text{Model 1}\,|\,\text{Data})")} and  {tex_inline(r"P(\text{Model 2}\,|\,\text{Data})")}

                **General Problem in Physics:**

                It is often straightforward to predict a measurement from
                physical theory -- but we usually want to use data to determine if our
                theory is right.
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, h2, mo):
    # Slide 52 -- Popular Understanding (Wrong!)
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics") + h2("Popular Understanding (Wrong!)")),
            mo.md("""> "P(A) is the probability that A is true." """),
            mo.hstack(
                [
                    mo.image(src="images/weather_widget_screenshot.png", width="70%"),
                    mo.image(src="images/atlas_higgs_mass_plot.png", width="100%"),
                ],
                widths=[1, 1],
                gap=1,
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, h2, mo, tex_svg):
    # Slide 53 -- Frequentist Statistics
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics") + h2("Frequentist Statistics")),
            mo.md(
                """
                - P(A) is the fraction of experiments that reach an outcome A -- if the
                  experiment is repeated an infinite number of times:
                """
            ),
            tex_svg(r"P(A) = \lim_{n \to \infty} \dfrac{\text{Number of Results } A}{n}", fontsize=26),
            mo.md(
                """
                - <span style="color:#39B54A">**Benefits:**</span>
                    - <span style="color:#39B54A">"Objective" (not really... more on Lecture 8)</span>
                    - <span style="color:#39B54A">Experimentally Verifiable</span>
                - <span style="color:#A31E33">**Problems:**</span>
                    - <span style="color:#A31E33">Not all experiments are repeatable</span>
                    - <span style="color:#A31E33">The question we want is "The Probability that A is true"</span>
                """
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, h2, mo):
    # Slide 54 -- Frequentist Statistics are sometimes counterintuitive
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics") + h2("Frequentist Statistics are sometimes counterintuitive")),
            mo.image(src="images/katrin_histogram_fig.png", width="65%"),
            mo.md(
                """*Figure: KATRIN Collaboration, "Analysis methods for the first KATRIN neutrino-mass measurement" (2021)*"""
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, h2, mo):
    # Slide 55 -- Bayesian Statistics
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.Html(h1("Interpretations of Statistics") + h2("Bayesian Statistics")),
                    mo.md(
                        r"""
                        - The degree of belief in the hypothesis that A is true.
                        - <span style="color:#39B54A">**Benefits:**</span>
                            - <span style="color:#39B54A">It is the questions that we really want to answer</span>
                        - <span style="color:#A31E33">**Problems:**</span>
                            - <span style="color:#A31E33">The apparent subjectivity of the prior makes some scientists reluctant to adopt it.</span>
                        """
                    ),
                ]
            ),
            mo.image(src="images/bayes_handdrawn_diagram.png", width="100%"),
        ],
        widths=[1, 1],
        align="center",
        gap=2,
    )
    return


@app.cell
def _(h1, h2, mo):
    # Slide 56 -- Bayesian Statistics is easier to interpret
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics") + h2("Bayesian Statistics is easier to interpret")),
            mo.image(src="images/desi_neutrino_mass_fig.png", width="65%"),
            mo.md(
                """*Figure: DESI Collaboration, "Constraints on Neutrino Physics from DESI DR2 BAO and DR1 Full Shape" (2025)*"""
            ),
        ],
        gap=0.5,
    )
    return


@app.cell
def _(h1, mo):
    # Slide 57 -- closing: Interpretations of Statistics (video reference)
    mo.vstack(
        [
            mo.Html(h1("Interpretations of Statistics")),
            mo.image(src="images/youtube_frequentism_bayesianism.png", width="70%"),
            mo.md(
                """[https://youtu.be/KhAUfqhLakw](https://youtu.be/KhAUfqhLakw)"""
            ),
        ],
        gap=0.5,
    )
    return


if __name__ == "__main__":
    app.run()
