from manim import *


# --- SCENE 1: SOLVING A DIFFERENTIAL EQUATION (WITH CORRECTION) ---
# This animation demonstrates solving dy/dx = (4+9y²)/(e^(2x+1)) step-by-step
# Notably includes a correction from a previous video where the integration constant was forgotten
class Intro(Scene):
    def construct(self):
        # --- TITLE AND ADMISSION OF ERROR ---
        m1 = MathTex(
            r"\text{Solving First-Order Differential Equations}",
            r"\text{(and correcting my mistakes from the first video)}",
        )
        m1[0].color, m1[1].color = (
            GOLD,
            RED,
        )  # Gold for main title, red for correction note
        m1.scale(0.5).arrange(DOWN)

        # --- PROBLEM SETUP AND INITIAL STEPS ---
        # Shows the differential equation and the first two steps of the solution process
        m2 = MathTex(
            r"\frac{dy}{dx} = \frac{4+9y^2}{e^{2x+1}}",  # Original differential equation
            r"\text{First Step: Separation of Variables}",
            r"\frac{1}{4+9y^2}dy = \frac{1}{e^{2x+1}}dx",  # Separated form: move all y terms to left, x terms to right
            r"\text{Second Step: Integrate Both Sides}",
            r"\int \frac{1}{4+9y^2}dy = \int \frac{1}{e^{2x+1}}dx",  # Set up integrals
        )
        m2.scale(0.5).arrange(DOWN)
        m2[0].color, m2[1].color, m2[2].color, m2[3].color, m2[4].color = (
            RED,
            GOLD,
            RED,
            GOLD,
            RED,
        )

        # --- SOLVING THE LEFT INTEGRAL: U-SUBSTITUTION ---
        # The integral ∫1/(4+9y²)dy requires u-substitution to transform into arctan form
        m3 = MathTex(
            r"\text{To solve left side, we use u-substitution.}",
            r"\text{Let } u = \frac{3}{2}y, du = \frac{3}{2}dy",  # Substitution chosen to match arctan derivative form
            r"\text{We hope to place the expression in the form}",
            r"\frac{u'}{1+u^2} \text{ to match the integral form of arctan(u).}",  # Key: d/du[arctan(u)] = 1/(1+u²)
        )
        m3.scale(0.5).arrange(DOWN).move_to([0, 1, 0])
        m3[0].color, m3[1].color, m3[2].color, m3[3].color = GOLD, RED, GOLD, GOLD

        # --- COMPLETING THE LEFT SIDE INTEGRATION ---
        # Step-by-step transformation from original integral to arctan result
        m4 = MathTex(
            r"\frac{2}{3} \int \frac{1}{4+4u^2} = \frac{1}{6} \int \frac{1}{1+u^2}",  # Factor out constants to get 1/(1+u²)
            r"\frac{d}{du} arctan(u) = \frac{1}{1+u^2}",  # Reminder: derivative of arctan
            r"\frac{1}{6} \int \frac{1}{1+u^2} = \frac{arctan(u)}{6}",  # Apply arctan integral
            r"= \frac{arctan(\frac{3}{2}y)}{6}",  # Substitute back u = (3/2)y
        )
        m4.color = GOLD
        m4.scale(0.5).arrange(DOWN)

        # --- ANIMATION SEQUENCE ---
        self.play(Write(m1), run_time=2)
        self.wait(2)
        self.play(FadeOut(m1))

        # Show problem and initial steps
        self.play(Write(m2), run_time=5)
        self.wait(5)

        # Keep only the integral equation visible
        self.play(FadeOut(m2[0:4]), m2[4].animate.move_to([0, 2.5, 0]))
        self.wait(2)

        # Explain u-substitution strategy
        self.play(Write(m3), run_time=4)
        self.wait(4)

        # Keep only the substitution u = (3/2)y
        self.play(FadeOut(m3[0], m3[2], m3[3]), m3[1].animate.move_to([0, 2, 0]))

        # Work through the integral calculation
        self.play(Write(m4), run_time=4)
        self.wait(4)

        # Clean up to show final result of left side
        self.play(
            FadeOut(m4[0:3], m3[1]),
            m4[3].animate.move_to([0, -0.5, 0]),  # Left side result
            m2[4].animate.move_to([0, 0.5, 0]),  # Original equation
        )
        self.wait(2)


# --- SCENE 2: COMPLETING THE SOLUTION AND ADDING THE CONSTANT ---
# Solves the right side integral, combines both sides, and importantly adds +C
class Second(Scene):
    def construct(self):
        # --- RESTORE STATE FROM PREVIOUS SCENE ---
        # Left side is solved: ∫1/(4+9y²)dy = arctan((3/2)y)/6
        # Right side needs solving: ∫1/e^(2x+1)dx
        m0 = MathTex(
            r"\int \frac{1}{4+9y^2} dy = \int \frac{1}{e^{2x+1}}dx",
            r"= \frac{arctan(\frac{3}{2} y)}{6}",
        )
        m0[0].color = RED
        m0[0].scale(0.5).move_to([0, 0.5, 0])
        m0[1].color = GOLD
        m0[1].scale(0.5).move_to([0, -0.5, 0])

        # --- SOLVE RIGHT SIDE INTEGRAL ---
        # ∫1/e^(2x+1)dx = ∫e^(-2x-1)dx = -1/2 · e^(-2x-1) + C
        m1 = MathTex(
            r"\int \frac{1}{e^{2x+1}}dx = ",
            r"-\frac{1}{2} e^{-2x-1}",  # Result using chain rule: d/dx[e^(ax)] = a·e^(ax)
            color=RED,
        )
        m1.scale(0.5)

        # --- COMBINE AND SOLVE FOR Y ---
        # Algebraically isolate y by taking inverse tangent operations
        m2 = MathTex(
            r"arctan(\frac{3}{2}y) = -\frac{3}{e^{2x+1}}",  # Multiply both sides by 6 and rearrange
            r"\frac{3}{2}y = tan(-\frac{3}{e^{2x+1}})",  # Take tangent of both sides
            r"y = \frac{2}{3} tan(-\frac{3}{e^{2x+1}})",  # Multiply by 2/3 to isolate y
        )
        m2.scale(0.5).arrange(DOWN)
        m2[0].color, m2[1].color = GOLD, GOLD
        m2[2].color = PURPLE  # Final answer in purple

        # --- ANIMATION SEQUENCE ---
        self.add(m0)

        # Remove duplicate integral symbols, keep equation structure
        self.play(FadeOut(m0[0][0:10], m0[1][0]), m0[1][1:].animate.move_to(m0[0][2]))
        eq1 = VGroup(m0[1][1:], m0[0][10:])
        self.play(eq1.animate.move_to([0, 1.5, 0]))

        # Show right side integration result
        self.play(Write(m1))

        # Clean up and combine results
        self.play(
            FadeOut(m1[0], eq1[1][1:]),
            m1[1].animate.move_to(eq1[1][2]).shift(0.2 * DOWN),
        )

        # Solve for y step by step
        self.play(Write(m2))
        self.wait(4)

        # Isolate final answer
        self.play(
            FadeOut(m2[0], m2[1], eq1[0], m1[1], eq1[1][0]),
            m2[2].animate.move_to([0, 0, 0]),
        )

        # --- THE CORRECTION: ADDING THE INTEGRATION CONSTANT ---
        # This is what was missing from the original video!
        sorry = MathTex(
            r"\text{Sorry for the year-long delay!}",
            r"\text{You thought I forgot the integration constant!!!}",
        )
        sorry.scale(0.5).arrange(DOWN).move_to([0, 1, 0])

        self.play(Write(sorry[0]))
        self.play(Write(sorry[1]))

        # Add the +C that should have been there all along
        # This constant comes from the indefinite integration and represents the family of solutions
        m4 = MathTex(
            r"y = \frac{2}{3} tan(-\frac{3}{e^{2x+1}}) + C",  # General solution with arbitrary constant
            color=PURPLE,
        )
        m4.scale(0.5)

        # Transform the incomplete answer to the complete answer
        self.play(Transform(m2[2], m4))
        self.wait(2)
