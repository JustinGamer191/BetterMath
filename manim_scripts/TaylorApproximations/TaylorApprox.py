from manim import *
class Intro(Scene):
    def construct(self):
        title = Text("Taylor Series Approximations")
        title.scale(0.5)
        title.color = BLUE

        text = MathTex(
            r"\text{A Taylor series of a function}",
            r"\text{can be used to approximate its value}",
            r"\text{near a given point.}"
        )
        text.scale(0.5)
        text.arrange(DOWN)
        text.color = RED
        
        pendulum_formula = MathTex(
            r"T = 2\pi \sqrt{\frac{L}{g}}"
        )
        pendulum_formula.scale(0.5)
        pendulum_formula.color = GREEN
        pendulum_formula.move_to([0,0,0])

        textp = MathTex(
            r"\text{A Taylor series approximation was used}",
            r"\text{to derive the formula for the period of a simple pendulum}",
            r"\text{for small angles } \theta \text{ (in radians)}"
        )
        textp.scale(0.5)
        textp.arrange(DOWN)
        textp.color = ORANGE
        textp.move_to([0, -1.5, 0])

        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.play(Write(text))
        self.play(text.animate.move_to([0, 1.5, 0]))
        self.wait(2)
        self.play(Write(pendulum_formula))
        self.wait(2)
        self.play(Write(textp))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(pendulum_formula), FadeOut(textp))
        self.wait(2)
        
class TaylorApprox(Scene):
    def construct(self):
        origin = [0, 1.5, 0]
        length = 3
        max_angle = PI / 6 

        pivot = Dot(origin, radius=0.09, color=GRAY)

        support = Line([origin[0] - 0.5, origin[1], 0], [origin[0] + 0.5, origin[1], 0], color=GRAY, stroke_width=4)
        equilibrium_point = [
            origin[0],
            origin[1] - length,
            0
        ]
        dotted_line = DashedLine(
            start=[equilibrium_point[0], equilibrium_point[1], 0],
            end=[equilibrium_point[0], equilibrium_point[1]+3, 0],
            color=GRAY,
            dash_length=0.15,
            stroke_width=2
        )
        arc = Arc(
            start_angle=-PI/2, 
            angle=max_angle, 
            radius=0.7, 
            arc_center=origin, 
            color=YELLOW
        )
        theta_label = MathTex(r"\theta", color=YELLOW).scale(0.7)
        theta_label.move_to([
            0.7 * np.cos(-PI/2 + max_angle/2),
            origin[1] + 0.7 * np.sin(-PI/2 + max_angle/2),
            0
        ])
        def get_bob_and_string(angle):
            bob_pos = [
                origin[0] + length * np.sin(angle),
                origin[1] - length * np.cos(angle),
                0
            ]
            string = Line(origin, bob_pos, color=WHITE, stroke_width=3)
            bob = Circle(radius=0.22, color=BLUE, fill_opacity=1).move_to(bob_pos)
            return VGroup(string, bob)

        pendulum = get_bob_and_string(max_angle)
        length_label = MathTex(r"L", color=WHITE).scale(0.7)
        string_midpoint = [
            (origin[0] + pendulum[0].get_end()[0]) / 2,
            (origin[1] + pendulum[0].get_end()[1]) / 2,
            0
        ]
        length_label.move_to(string_midpoint + np.array([0.3, 0, 0]))
        
        arc_s = Arc(
            start_angle=-PI/2,
            angle=max_angle,
            radius=length,
            arc_center=origin,
            color=GREEN,
            stroke_width=4
        )
        s_label = MathTex(r"s", color=GREEN).scale(0.7)
        s_label.move_to(arc_s.get_center() + DOWN * 0.3)
        all_elements = VGroup(pendulum, length_label, theta_label, support, pivot, arc, dotted_line, arc_s, s_label)
        all_elements.shift(2 * UP)
        theta_label.shift(DOWN*0.25)
        
        
        self.play(Create(support), Create(pivot), Create(dotted_line))
        self.play(Create(arc_s), Write(s_label))
        self.play(Create(pendulum), Write(length_label))
        self.play(Create(arc), Write(theta_label))
        self.wait(1)

        text3 = MathTex(r"F = mg\sin(\theta)", color=RED).scale(0.7)
        text4 = MathTex(r"\text{Small angle approximation using Taylor Series:}", color=RED).scale(0.7)
        text5 = MathTex(r"\sin(\theta) \approx \theta", color=RED).scale(0.7)
        text6 = MathTex(r"\Rightarrow F \approx mg\theta", color=RED).scale(0.7)
        text7 = MathTex(r"\theta = \frac{s}{L}", color=RED).scale(0.7)
        text8 = MathTex(r"\Rightarrow F \approx mg \frac{s}{L}", color=RED).scale(0.7)
        text9 = MathTex(r"\text{Force is proportional to displacement } s", color=RED).scale(0.7)
        text10 = MathTex(r"\Rightarrow \text{Simple Harmonic Motion}", color=RED).scale(0.7)
        text4.next_to(text3, DOWN, buff=0.1)
        text5.next_to(text4, DOWN, buff=0.1)
        text6.next_to(text5, DOWN, buff=0.1)
        text7.next_to(text3, DOWN, buff=0.1)
        text8.next_to(text7, DOWN, buff=0.1)
        text9.next_to(text8, DOWN, buff=0.1)
        text10.next_to(text9, DOWN, buff=0.1)
        text9.next_to(text8, DOWN, buff=0.1)

        self.play(Write(text3))
        self.wait(1)
        self.play(Write(text4))
        self.wait(1)
        self.play(Write(text5))
        self.wait(1)
        self.play(Write(text6))
        self.wait(1)
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(text5))
        self.play(text6.animate.move_to(text3))
        self.play(Write(text7))
        self.wait(1)
        self.play(Write(text8))
        self.wait(1)
        self.play(Write(text9))
        self.wait(1)
        self.play(Write(text10))
        self.wait(1)
        self.play(FadeOut(text6), FadeOut(text7), FadeOut(text9), FadeOut(all_elements))
        self.play(text8.animate.move_to([0,2,0]), text10.animate.move_to([0,2,0]).shift(DOWN))

        text11 = MathTex(r"F = kx", color=RED).scale(0.7)
        text11.move_to([0,2,0]).shift(1.5*DOWN)
        text12 = MathTex(r"\Rightarrow \text{SHM with } k = \frac{mg}{L}", color=RED).scale(0.7)
        text12.next_to(text11, DOWN, buff=0.1)
        text13 = MathTex(r"T = 2\pi \sqrt{\frac{m}{k}}", color=RED).scale(0.7)
        text13.next_to(text12, DOWN, buff=0.1)
        text14 = MathTex(r"\Rightarrow T = 2\pi \sqrt{\frac{L}{g}}", color=RED).scale(0.7)
        text14.next_to(text13, DOWN, buff=0.1)
        self.play(Write(text11))
        self.wait(1)
        self.play(Write(text12))
        self.wait(1)
        self.play(Write(text13))
        self.wait(1)
        self.play(Write(text14))
        self.wait(2)