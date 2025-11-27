from manim import *


class Intro(Scene):
    def construct(self):
        t1 = MathTex(
            r"\text{Parrondo's Paradox: Introduction}",
            r"\text{Winning from losing situations.}",
            color=BLUE,
        )
        t1.scale(0.5)
        t1.arrange(DOWN)

        t2 = MathTex(
            r"\text{Let's imagine you have a coin,}",
            r"\text{one that has a 50.5\% chance on landing on heads}",
            r"\text{and a 49.5\% chance of landing on tails.}",
            color=BLUE,
        )
        t2.scale(0.5)
        t2.arrange(DOWN)
        t2.move_to([0, 2, 0])

        rim = Circle(radius=1, color=YELLOW, stroke_width=6)
        face = Circle(radius=0.9, color=YELLOW, fill_opacity=1)

        heads = Text("H").scale(2).set_color(BLACK)
        headsLabel = MathTex(r"50.5\%")
        headsLabel.scale(0.5)
        headsLabel.next_to(heads, 0.5 * DOWN)
        headsLabel.color = BLACK

        tails = Text("T").scale(2).set_color(BLACK)
        tailsLabel = MathTex(r"49.5\%")
        tailsLabel.scale(0.5)
        tailsLabel.color = BLACK
        tailsLabel.next_to(heads, 0.5 * DOWN)
        tails.rotate(angle=0.5 * PI, axis=UP)
        tailsLabel.rotate(angle=1.5 * PI, axis=UP)
        coin = VGroup(rim, face, heads, headsLabel)

        # Intro
        self.play(Write(t1))
        self.wait()

        self.play(FadeOut(t1[1]), t1[0].animate.move_to([0, 3, 0]))
        self.wait()
        self.play(Write(t2[0]))
        self.wait()

        # Coin animation
        self.play(Write(coin))
        self.play(Write(t2[1]))
        coin1 = coin.copy()
        self.add(coin1)
        self.play(coin1.animate.move_to([-1.5, -2, 0]))
        self.play(Rotate(coin, angle=0.5 * PI, axis=UP, run_time=2, rate_func=smooth))
        self.replace(heads, tails)
        self.replace(headsLabel, tailsLabel)
        self.play(Rotate(coin, angle=0.5 * PI, axis=UP, run_time=2, rate_func=smooth))
        self.play(Write(t2[2]))
        coin2 = coin.copy()
        self.add(coin2)
        self.play(coin2.animate.move_to([1.5, -2, 0]))
        self.wait()

        self.play(
            FadeOut(t1[0], t2, coin),
            coin1.animate.move_to([-1, 2.5, 0]).scale(0.75),
            coin2.animate.move_to([1, 2.5, 0]).scale(0.75),
        )
        self.wait()

        # Expected loss of coin game A
        t3 = MathTex(
            r"\text{Now imagine for every time it lands on heads, you lost \$1,}",
            r"\text{and for every time it lands on tails, you gain \$1.}",
            r"\text{Your expected gain is: } 0.505 * -1 + 0.495 * 1 = -0.01",
            r"\text{Or a loss of 1 cent per flip.}",
            color=BLUE,
        )
        t3.scale(0.5)
        t3.arrange(DOWN)

        self.play(Write(t3[0]))
        self.play(Indicate(coin1, color=RED))
        self.play(Write(t3[1]))
        self.play(Indicate(coin2, color=GREEN))
        self.wait()
        self.play(Write(t3[2:]))
        self.wait(1.5)
        self.play(FadeOut(t3[0:3], t3[3][0:3]))
        self.play(t3[3][3:].animate.move_to([0, 1.25, 0]).set_color(RED))

        tA = MathTex(
            r"\text{Let's call this game}",
            r"\mathbf{\text{Game A}}",
            r"\text{and set it aside for now.}",
            color=RED,
        )

        tA.scale(0.5)
        tA.arrange(DOWN)

        self.play(Write(tA), run_time=4)
        self.wait()

        self.play(FadeOut(tA[0], tA[2]), tA[1].animate.move_to([0, 3.5, 0]))
        self.wait()
        gameA = VGroup(coin1, coin2, t3[3][3:], tA[1])
        self.play(gameA.animate.scale(0.01))
        self.remove(gameA)
        self.wait()
        t1 = (
            MathTex(
                r"\text{Now let's imagine you have another game}",
                r"\text{where you spin a wheel.}",
            )
            .set_color(RED)
            .scale(0.5)
            .arrange(DOWN)
        )
        t2 = (
            MathTex(
                r"\text{If your amount of money is divisible by 3,}",
                r"\text{you spin a wheel that has a 9.5\% chance of winning.}",
                r"\text{Otherwise, you spin a wheel that has a 74.5\% chance of winning.}",
            )
            .set_color(RED)
            .scale(0.4)
            .arrange(DOWN)
        )
        self.play(Write(t1))
        self.wait()
        self.play(FadeOut(t1))
        self.play(Write(t2[0:2]), run_time=3)
        self.wait()
        self.play(t2[0:2].animate.move_to([0, 3, 0]))

        def animateWheel(radius=1.5, fraction=0.095):
            wheel_radius = radius

            green_angle = fraction * TAU

            green_sector = Sector(
                radius=wheel_radius,
                angle=green_angle,
                start_angle=PI / 2,
                color=GREEN,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=3,
            )

            red_sector = Sector(
                radius=wheel_radius,
                angle=TAU - green_angle,
                start_angle=PI / 2 + green_angle,
                color=RED,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=3,
            )

            wheel = VGroup(red_sector, green_sector)

            center_circle = Circle(
                radius=0.15,
                color=YELLOW,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2,
            )

            pointer = Triangle(color=YELLOW, fill_opacity=1).scale(0.3).rotate(PI)
            pointer.move_to(UP * (wheel_radius + 0.4))

            self.play(Write(wheel), FadeIn(center_circle), FadeIn(pointer))
            self.wait(1)

            spins = 1
            total_angle = spins * TAU + np.random.random() * TAU
            self.play(
                Rotate(
                    wheel,
                    angle=total_angle,
                    run_time=3,
                    rate_func=rate_functions.ease_out_cubic,
                ),
                Rotate(
                    center_circle,
                    angle=total_angle,
                    run_time=3,
                    rate_func=rate_functions.ease_out_cubic,
                ),
            )
            self.wait(0.5)
            return VGroup(wheel, pointer, center_circle)

        badWheel = animateWheel()
        self.play(FadeOut(t2[0], t2[1][0:21], t2[1][25:]))
        self.play(t2[1][21:25].animate.move_to([0, -1.75, 0]).set_color(RED))
        badLabel = MathTex(r"\text{If money is divisible by 3:}")
        badLabel.scale(0.5)
        badLabel.move_to([0, 2.5, 0]).set_color(RED)
        self.play(FadeIn(badLabel))
        badWheel.add(t2[1][21:25], badLabel)
        self.play(badWheel.animate.scale(0.5).move_to([-1, -2.5, 0]))
        self.wait()

        t2[2].move_to([0, 0, 0])
        self.play(Write(t2[2]))
        self.play(t2[2].animate.move_to([0, 2.5, 0]))

        goodWheel = animateWheel(1.5, 0.745)
        self.play(FadeOut(t2[2][0:31], t2[2][36:]))
        self.play(t2[2][31:36].animate.move_to([0, -1.75, 0]).set_color(GREEN))
        goodWheel.add(t2[2][31:36])
        goodLabel = MathTex(r"\text{If money isn't divisible by 3:}")
        goodLabel.scale(0.5)
        goodLabel.move_to([0, 2.5, 0]).set_color(GREEN)
        self.play(FadeIn(goodLabel))
        goodWheel.add(goodLabel)

        self.play(goodWheel.animate.scale(0.5).move_to([1, -2.5, 0]))
        self.play(VGroup(goodWheel, badWheel).animate.move_to([0, -1.5, 0]))

        t3 = (
            MathTex(
                r"\text{Your expected gain can be solved using}",
                r"\text{a complicated markov chain, but it's around}",
                r"\text{a loss of 0.87 cents per spin.}",
            )
            .scale(0.5)
            .set_color(RED)
            .arrange(DOWN)
            .shift(UP)
        )

        self.play(Write(t3), run_time=2)
        self.wait()
        self.play(FadeOut(t3[0:2]), t3[2].animate.move_to([0, -3, 0]))
        self.wait()
        gameBLabel = MathTex(r"\text{Game B}").scale(0.5).set_color(BLUE)
        self.play(Write(gameBLabel))
        gameB = VGroup(gameBLabel, t3[2], goodWheel, badWheel)
        self.add(gameA)
        self.play(gameA.animate.scale(100))
        self.wait()


class Second(Scene):
    def construct(self):
        t4 = (
            MathTex(
                r"\text{If you chose to play any of these games,}",
                r"\text{you would lose all your money!}",
                r"\text{However, alternating between games}",
                r"\text{yields a different result.}",
            )
            .scale(0.5)
            .arrange(DOWN)
            .set_color(GOLD)
        )

        self.play(Write(t4[0:2]), run_time=1.5)
        self.wait()
        self.play(Write(t4[2:]), run_time=1.5)
        self.wait()
        self.play(FadeOut(t4))

        t5 = (
            MathTex(
                r"\text{For example, alternating between}",
                r"\text{two rounds of game A and}",
                r"\text{two rounds of game B}",
                r"\text{results in a profit of 1.48 cents per round.}",
            )
            .scale(0.5)
            .arrange(DOWN)
            .set_color(GOLD)
        )
        self.play(Write(t5), run_time=3)
        self.wait()
        t6 = MathTex(
            r"\text{The purpose of this animation}",
            r"\text{was to motivate curiosity.}",
            r"\text{If you're curious about the math",
            r"\text{that'll be for part 2.}",
        )
        t6.scale(0.5).set_color(GOLD)
        t6.arrange(DOWN)
        self.play(FadeOut(t5))
        self.play(Write(t6), run_time=3)
        self.wait()
        self.play(FadeOut(t6))

        # AI generated outro for funsies!
        fontSize = 48
        better = Text("Better", font_size=fontSize, weight=BOLD, color=BLUE)
        math = Text("Math", font_size=fontSize, weight=BOLD, color=WHITE)
        dot = Text(".", font_size=fontSize, weight=BOLD, color=BLUE)
        tv = Text("TV", font_size=fontSize, weight=BOLD, color=WHITE)

        logo = VGroup(better, math, dot, tv).arrange(RIGHT, buff=0.1)
        logo.move_to([0, 1, 0])

        tagline = Text("MATH is ART", font_size=fontSize / 4, color=GREY, slant=ITALIC)
        tagline.next_to(logo, DOWN, buff=0.5)

        left_line = Line(LEFT * 3, LEFT * 0.5, color=BLUE, stroke_width=3)
        right_line = Line(RIGHT * 0.5, RIGHT * 3, color=BLUE, stroke_width=3)
        left_line.next_to(tagline, DOWN, buff=0.3)
        right_line.next_to(tagline, DOWN, buff=0.3)

        self.play(
            FadeIn(better, shift=DOWN * 0.5),
            FadeIn(math, shift=DOWN * 0.5),
            FadeIn(dot, shift=DOWN * 0.5),
            FadeIn(tv, shift=DOWN * 0.5),
            run_time=1,
        )

        self.play(logo.animate.scale(1.1), rate_func=there_and_back, run_time=0.5)

        self.play(Write(tagline), Create(left_line), Create(right_line), run_time=1)

        sparkles = VGroup(
            *[
                Star(color=YELLOW, fill_opacity=0.8)
                .scale(0.2)
                .move_to(
                    logo.get_center()
                    + np.array([np.random.uniform(-3, 3), np.random.uniform(-2, 2), 0])
                )
                for _ in range(12)
            ]
        )

        self.play(
            LaggedStart(*[FadeIn(star, scale=0.5) for star in sparkles], lag_ratio=0.1),
            run_time=1,
        )

        self.play(FadeOut(sparkles), run_time=0.5)

        self.play(
            *[FadeOut(mob) for mob in [logo, tagline, left_line, right_line]],
            run_time=1
        )

        self.wait(0.5)
