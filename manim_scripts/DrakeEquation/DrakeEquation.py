from manim import *
import random


# --- SCENE 1: INTRODUCTION TO THE DRAKE EQUATION ---
# The Drake Equation estimates the number of active, communicative extraterrestrial civilizations in our galaxy
class Intro(Scene):
    def construct(self):
        # --- TITLE AND INTRODUCTION ---
        t1 = MathTex(
            r"\text{Fermi Estimations}",
            r"\text{Part 1: The Drake Equation}",
            r"\text{An estimation for the number of}",
            r"\text{advanced civilizations in our galaxy.}",
        )
        t1.arrange(DOWN)
        t1[0].color = BLUE
        t1[1:].color = GOLD
        t1.scale(0.5)

        # Display title sequence
        self.play(Write(t1[0]))
        self.play(Write(t1[1]))
        self.play(Write(t1[2]), Write(t1[3]))
        self.wait(1)

        # Keep only the main title visible
        self.play(FadeOut(t1[0], t1[2:]), t1[1].animate.move_to([0, 3, 0]))
        self.wait(1)

        # --- TERM 1: STAR FORMATION RATE ---
        # First component of Drake Equation: R* = rate of star formation
        t2 = MathTex(
            r"\text{First, let's count the number of stars in the Milky Way galaxy.}",
            r"\text{That's a lot! Over 100 billion to be exact!}",
            r"\text{Stars in our galaxy form at a rate of } \frac{10 \text{stars}}{\text{year}}",
        )
        t2.scale(0.5)
        t2.arrange(DOWN)
        t2.next_to(t1[1], DOWN)
        t2.color = GOLD

        self.play(Write(t2[0]))

        # --- VISUAL: STARFIELD ANIMATION ---
        # Create 2000 random stars to visualize the vastness of our galaxy
        def add_stars():
            stars = VGroup()
            for _ in range(2000):
                star = Dot(
                    point=[random.uniform(-2, 2), random.uniform(-2, 0), 0],
                    radius=random.uniform(0.02, 0.06),  # Vary star sizes
                    color=interpolate_color(
                        BLUE_A, WHITE, random.uniform(0.8, 1.0)
                    ),  # Create color variation
                )
                stars.add(star)
            self.play(Write(stars))

            # Animate stars twinkling with different colors (white, blue, yellow like real stars)
            self.play(
                *[
                    star.animate.set_opacity(random.uniform(0.4, 1)).set_color(
                        random.choice([WHITE, BLUE_B, YELLOW_E])
                    )
                    for star in stars
                ],
                run_time=2
            )
            return stars

        stars = add_stars()

        # Display remaining text about star formation
        self.play(Write(t2[1]))
        self.play(Write(t2[2]))
        self.wait(1)

        # --- EXTRACT FIRST DRAKE EQUATION TERM ---
        t3 = MathTex(
            r"\text{That's the first part of our Drake Equation:}",
            r"10 \frac{\text{stars}}{year}",
        )
        t3.scale(0.5)
        t3.arrange(DOWN)
        t3.next_to(t2[-1], DOWN)
        t3.color = BLUE

        # Clear stars and isolate the first term
        self.play(FadeOut(stars))
        self.play(Write(t3))
        self.wait(2)

        # Move term to equation building area (left side of screen)
        self.play(
            FadeOut(t2, t3[0]), t3[1].animate.next_to(t1[1], DOWN).shift(2.5 * LEFT)
        )
        self.wait()

        # --- TERM 2: PLANETS PER STAR ---
        # Second component: fp = fraction of stars with planetary systems
        t4 = MathTex(
            r"\text{Next, how many planets are there per star?}",
            r"\text{Current estimations say on average there is }",
            r"1 \frac{\text{planet}}{\text{star}}",
            r"\text{ in the milky way.}",
        )
        t4.scale(0.5)
        t4[0].next_to(t1[1], 4 * DOWN)
        t4[1:].next_to(t4[0], DOWN)
        t4.color = GOLD

        self.play(Write(t4[0]))
        self.play(Write(t4[1:]))
        self.wait()

        # --- VISUAL: PLANET ORBITING STAR ---
        def rotate_planet_star():
            # Create a simple star-planet system
            star = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
            star.set_fill(YELLOW, 1)
            star.move_to([0, -1, 0])

            planet = Circle(radius=0.15, color=BLUE, fill_opacity=1)
            planet.set_fill(BLUE, 1)
            planet.move_to(star.get_center() + RIGHT * 1.5)

            # Orbital path (light gray circle)
            orbit = Circle(radius=1.5, color=WHITE, stroke_opacity=0.3)
            orbit.move_to(star.get_center())

            self.play(Write(star))
            self.play(Write(planet), Write(orbit))

            # Animate one complete orbit
            self.play(
                Rotating(
                    planet,
                    about_point=star.get_center(),
                    angle=2 * PI,  # Full 360-degree rotation
                    run_time=2,
                    rate_func=linear,
                ),
            )
            return VGroup(star, orbit, planet)

        system = rotate_planet_star()
        self.play(FadeOut(system))
        self.wait(1)

        # --- ADD MULTIPLICATION SYMBOL ---
        mult = MathTex(r"\times")
        mult.scale(0.5)
        mult.next_to(t3[1], RIGHT)

        # Add second term to equation: 10 × 1
        self.play(
            FadeOut(t4[0], t4[1], t4[3]),
            t4[2].animate.next_to(mult, RIGHT),
            FadeIn(mult),
        )
        self.wait()

        # --- TERM 3: HABITABLE ZONE FRACTION ---
        # Third component: ne = average number of planets in habitable zone per star with planets
        t5 = MathTex(
            r"\text{But are all these planets habitable?",
            r"Let's explore the percentage of planets that are habitable!}",
            r"\text{Estimates say 1 in 10 planets around a star are habitable:}",
            r"\frac{1}{10} \frac{\text{habitable}}{\text{planets}}",
        )
        t5.scale(0.5)
        t5[0].move_to(t4[0])
        t5[1].next_to(t5[0], DOWN)
        t5[2:].next_to(t5[1], DOWN)
        t5.color = BLUE

        self.play(Write(t5[0]))
        self.play(Write(t5[1]))
        self.play(Write(t5[2:]))

        # --- VISUAL: HABITABLE ZONE DEMONSTRATION ---
        # Show 10 planets, only 1 in the habitable "Goldilocks zone"
        def habitable():
            star = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
            star.set_fill(YELLOW, 1)
            star.move_to(ORIGIN + DOWN * 1.5)

            self.play(Write(star))

            planets = VGroup()
            num_planets = 10
            habitable_index = random.randint(
                0, num_planets - 1
            )  # Randomly choose which planet is habitable

            # Create 10 planets at different distances from star
            for i in range(num_planets):
                x = (
                    star.get_x() + ((-1) ** i) * (i + 3) / 5
                )  # Alternate left/right positioning
                y = star.get_y()

                # Green = habitable zone, Blue = too hot or too cold
                color = GREEN if i == habitable_index else BLUE

                planet = Circle(radius=0.05, color=color, fill_opacity=1)
                planet.set_fill(color, 1)
                planet.move_to([x, y, 0])

                planets.add(planet)

            self.play(FadeIn(planets))

            # Highlight the habitable planet by rotating it
            self.play(
                Rotating(
                    planets[habitable_index],
                    about_point=star.get_center(),
                    angle=2 * PI,
                    run_time=2,
                    rate_func=linear,
                ),
            )
            return VGroup(planets, star)

        planets = habitable()
        self.wait()
        self.play(FadeOut(planets))
        self.wait()

        # --- ADD THIRD TERM TO EQUATION ---
        mult2 = mult.copy()
        mult2.next_to(t4[2], RIGHT)

        # Equation now reads: 10 × 1 × 1/10
        self.play(
            FadeOut(t5[0], t5[1], t5[2]),
            FadeIn(mult2),
            t5[3].animate.next_to(mult2, RIGHT),
        )
        self.wait()
        self.wait(2)

        # --- COMMENTED OUT SECTION ---
        # This section was planned to introduce the concept of "advanced civilizations"
        # capable of radio communication, but was moved to Scene 2 instead
        """
        t2 = MathTex(r"\text{First, let's define an advanced civilization as one}",
                     r"\text{that can and will transmit and recieve radio waves.}")
        t2.color = GOLD
        t2.arrange(DOWN).scale(0.5)
        t2.next_to(t1[1], DOWN)
        
        self.play(Write(t2))
        
        def radioAnimation():
            # Radio dish (parabolic antenna)
            dish = Arc(
                radius=3,
                start_angle=-PI/4,
                angle=PI/2,
                color=WHITE,
                stroke_width=8
            )
            
            dish.shift(2*LEFT, 1*DOWN)
            
            self.play(Create(dish), run_time=1.5)
            
            # Radio wave propagation parameters
            incident_angle = 10 * DEGREES
            wave_length = 4
            
            start_pos = LEFT * 5 + DOWN * 2
            
            # Calculate wave direction vector
            incident_direction = np.array(
                [np.cos(incident_angle),
                np.sin(incident_angle),
                0
                ]
                )
            
            # Create sinusoidal wave pattern
            def create_wave(position, direction, color=PURPLE):
                wave_group = VGroup()
                num_waves = 1
                for i in range(num_waves):
                    offset = i * 0.3
                    wave_points = []
                    for t in np.linspace(0, wave_length, 100):
                        x = t * direction[0]
                        y = t * direction[1] + 0.3 * np.sin(4 * PI * t - offset * 2 * PI)
                        wave_points.append(position + np.array([x, y, 0]))
                    
                    wave_curve = VMobject()
                    wave_curve.set_points_smoothly(wave_points)
                    wave_curve.set_color(color)
                    wave_curve.set_stroke(width=3)
                    wave_group.add(wave_curve)
                return wave_group
            
            # Incoming radio wave
            incident_wave = create_wave(start_pos, incident_direction, PURPLE)
            self.play(Create(incident_wave))
            
            # Calculate where wave hits the dish
            collision_point = [1,-1,0]
            travel_distance = np.linalg.norm(collision_point - start_pos)
            
            # Animate wave traveling to dish
            self.play(
                incident_wave.animate.shift(incident_direction * (travel_distance - wave_length * 0.7)),
                run_time=1.5,
                rate_func=linear
            )
            
            # Flash effect when wave hits dish
            self.play(
                Flash(collision_point, color=YELLOW, flash_radius=0.8),
                run_time=0.3
            )
            
            # Calculate reflection angle (angle of incidence = angle of reflection)
            reflected_direction = np.array([np.cos(PI - incident_angle),
                                            np.sin(PI - incident_angle),
                                            0])
            
            # Create reflected wave
            reflected_wave = create_wave(collision_point + DOWN + RIGHT,
                                         reflected_direction,
                                         PURPLE)
            
            # Swap incident wave for reflected wave
            self.play(
                FadeOut(incident_wave),
                FadeIn(reflected_wave),
                run_time=0.5
            )
            
            # Animate reflected wave traveling away
            self.play(
                reflected_wave.animate.shift(reflected_direction * 6),
                run_time=1.5,
                rate_func=linear
            )
            self.play(FadeOut(reflected_wave, dish))
        radioAnimation()
        self.wait()
        
        t3 = MathTex(r"\text{Let's assume the fraction of civilizations}",
                     r"\text{classified as \"advanced\" is equal to}", r"\frac{}")
        
        
        
        self.wait(2)
        """


# --- SCENE 2: COMPLETING THE DRAKE EQUATION ---
# Adds remaining terms: civilization development probability and temporal overlap
class Second(Scene):
    def construct(self):
        # --- RESTORE PREVIOUS EQUATION ---
        # Recreate the equation built in Scene 1: R* × fp × ne
        def previous_frame():
            lastFrame = MathTex(
                r"\text{Part 1: The Drake Equation}",
                r"10 \frac{\text{stars}}{year}",
                r"\times",
                r"1 \frac{\text{planet}}{\text{star}}",
                r"\times",
                r"\frac{1}{10} \frac{\text{habitable}}{\text{planets}}",
            )
            lastFrame.scale(0.5)
            lastFrame[0].color = GOLD
            lastFrame[1].color = BLUE
            lastFrame[3].color = GOLD
            lastFrame[5].color = BLUE
            lastFrame[0].move_to([0, 3, 0])
            lastFrame[1].next_to(lastFrame[0], DOWN).shift(2.5 * LEFT)
            lastFrame[2].next_to(lastFrame[1], RIGHT)
            lastFrame[3].next_to(lastFrame[2], RIGHT)
            lastFrame[4].next_to(lastFrame[3], RIGHT)
            lastFrame[5].next_to(lastFrame[4], RIGHT)

            self.add(lastFrame)
            return lastFrame

        lastFrame = previous_frame()

        # --- TERM 4: FRACTION WITH INTELLIGENT LIFE ---
        # fl = fraction of habitable planets that develop intelligent life
        t1 = MathTex(
            r"\text{But how many of these habitable planets have advanced civilizations?}",
            r"\text{First, let's classify an advanced civilization as one that}",
            r"\text{can and will transmit and recieve radio waves.}",  # Note: typo in original "recieve" -> "receive"
            color=GOLD,
        )
        t1.scale(0.5).arrange(DOWN).move_to([0, 1.25, 0])
        self.play(Write(t1[0]))
        self.wait()
        self.play(Write(t1[1:]))
        self.wait()

        # --- VISUAL: RADIO COMMUNICATION ---
        # Simplified radio dish and wave animation
        def radio_animation():
            # Parabolic dish antenna
            dish = Arc(
                radius=2, start_angle=-PI / 4, angle=PI / 2, color=WHITE, stroke_width=8
            )
            dish.move_to([2, -2, 0])
            self.play(Create(dish))

            # Create sinusoidal radio wave
            wave = VMobject(color=PURPLE)
            points = [np.array([x, np.sin(x), 0]) for x in np.linspace(0, 10, 200)]
            wave.set_points_smoothly(points)
            wave.scale(0.25).move_to([0, -2.5, 0]).rotate(15 * DEGREES)

            # Animate wave transmission
            self.play(Write(wave))
            self.play(wave.animate.move_to([1.25, -2, 0]))  # Wave approaches dish

            # Flash when signal is received
            collision_point = [2, -2, 0]
            self.play(
                Flash(collision_point, color=YELLOW, flash_radius=0.5, line_length=0.5)
            )

            # Reflect wave
            self.play(wave.animate.rotate(-30 * DEGREES))
            self.play(wave.animate.move_to([0, -1.5, 0]))
            self.wait()
            self.play(FadeOut(dish, wave))

        radio_animation()
        self.play(FadeOut(t1[1:]))

        # --- PESSIMISTIC ESTIMATE ---
        # Conservative Drake Equation: very few civilizations develop technology
        t2 = MathTex(
            r"\text{We could be strict and say that a mere fraction, around }",
            r"\frac{1 \text{ advanced}}{1000 \text{ habitable}}",
            r"\text{go on to develop advanced civilizations.}",
        )
        t2.color = GOLD
        t2.scale(0.5).arrange(DOWN).next_to(t1[0], DOWN)
        self.play(Write(t2), run_time=3)
        self.wait()

        # --- OPTIMISTIC ESTIMATE ---
        # Optimistic Drake Equation: all habitable planets eventually develop life
        self.play(FadeOut(t2))
        t3 = MathTex(
            r"\text{Or we could be optimistic and say that}",
            r"\frac{1 \text{ advanced}}{1 \text{ habitable}}",
            r"\text{of the habitable planets go on to develop life.}",
        )
        t3.color = GOLD
        t3.scale(0.5).arrange(DOWN).next_to(t1[0], DOWN)
        self.play(Write(t3), run_time=3)
        self.wait()

        # For this video, we'll use the optimistic estimate
        t4 = MathTex(r"\text{For our purposes, let's assume the best odds!}")
        t4.scale(0.5).next_to(t3[2], DOWN)
        t4.color = GOLD
        self.play(Write(t4))
        self.wait()

        # --- ADD FOURTH TERM TO EQUATION ---
        times3 = MathTex(r"\times")
        times3.scale(0.5).next_to(lastFrame[5], RIGHT)

        # Equation now: 10 × 1 × 1/10 × 1
        self.play(
            FadeOut(t1[0], t3[0], t3[2], t4),
            FadeIn(times3),
            t3[1].animate.next_to(times3, RIGHT),
        )
        self.wait()
        self.wait(2)

        # --- TERM 5: TEMPORAL OVERLAP ---
        # L = length of time civilizations are detectable
        # This is crucial: civilizations must exist at the SAME TIME to communicate
        t5 = MathTex(
            r"\text{Finally, for the last term in our equation, we'll have to}",
            r"\text{consider the chance two civilizations coexist at the same time.}",
            r"\text{Let's imagine the Milky Way as a long glowing bar,}",
            r"\text{and tiny, bright flashes to symbolize the appearance of life.}",
            color=BLUE,
        )
        t5.scale(0.5).arrange(DOWN).next_to(t1[0], DOWN)
        t5.shift(0.5 * UP)
        self.play(Write(t5[0:2]), run_time=4)
        self.wait()
        self.play(Write(t5[2:]), run_time=4)
        self.wait()

        # --- VISUAL: GALACTIC TIMELINE ---
        # Demonstrates how rare temporal overlap is across billions of years
        def MilkWayBar():
            # Timeline bar representing 10 billion year lifespan of Milky Way
            bar = Line(
                start=[-4, -0.5, 0], end=[4, -0.5, 0], stroke_width=15, color=BLUE_E
            )
            self.play(Create(bar))

            label = Text(
                "Milky Way Lifetime (~10 billion years)", font_size=28, color=GOLD
            )
            label.scale(0.5)
            label.next_to(bar, UP)
            self.play(Write(label))
            self.wait(1)

            # Create glowing effect for civilization appearances
            def make_glow(center, color=YELLOW, radius=0.3, glow_factor=3):
                layers = VGroup()
                for i in range(glow_factor):
                    circle = Circle(
                        radius=radius * (1 + i * 0.5),
                        color=color,
                        stroke_width=0,
                        fill_opacity=max(0.4 - i * 0.1, 0),  # Fade out at edges
                    )
                    circle.move_to(center)
                    layers.add(circle)
                return layers

            # Simulate 10 civilizations appearing at random times
            num_civs = 10
            for _ in range(num_civs):
                start_x = random.uniform(-4.5, 4.5)  # Random position on timeline
                civ = Dot(point=[start_x, -0.5, 0], radius=0.12, color=YELLOW)
                glow = make_glow(civ.get_center(), color=YELLOW, radius=0.2)

                # Flash briefly (representing brief civilization lifespan)
                self.play(FadeIn(glow, civ), run_time=0.1)
                self.wait(0.3)
                self.play(FadeOut(glow, civ), run_time=0.1)

            # Explain what overlapping flashes would mean
            overlap = Text(
                "Overlapping Flashes = Communication Possible", font_size=24, color=GOLD
            )
            overlap.scale(0.5)
            overlap.next_to(bar, DOWN)
            self.play(Write(overlap))
            self.wait(2)
            self.play(FadeOut(bar, label, overlap))

        MilkWayBar()
        self.wait()
        self.play(FadeOut(t5))

        # --- CALCULATE TEMPORAL OVERLAP PROBABILITY ---
        # L/L_MW = civilization lifetime / galaxy lifetime
        # Using 400 years (since we've had radio) / 10 billion years
        t6 = MathTex(
            r"\text{The chance that two advanced civilizations coexist}",
            r"\text{is equal to the average lifetime of a civilization}",
            r"\text{divided by the lifetime of the milky way.}",
            r"\frac{L}{L_{MW}} = \frac{~400 \text{ years}}{~10^{10} \text{ years}}",
        )

        t6.color = BLUE
        t6.scale(0.5).arrange(DOWN)
        t6.shift(UP)

        self.play(Write(t6[0:3]), run_time=6)
        self.wait()
        self.play(Write(t6[3]))
        self.wait()

        # --- ADD FIFTH TERM TO EQUATION ---
        # Scale down existing equation to make room
        self.play(VGroup(lastFrame[1:], times3, t3[1]).animate.scale(0.75).shift(LEFT))
        times4 = MathTex(r"\times")
        times4.scale(0.5).scale(0.75)
        times4.next_to(t3[1], 0.75 * RIGHT)
        self.play(FadeIn(times4))

        # Add temporal overlap term
        self.play(t6[3][6:].animate.scale(0.75).next_to(times4, 0.75 * RIGHT))
        self.wait(2)
        self.play(FadeOut(t6[0:3], t6[3][0:6]))
        self.wait()

        # --- FINAL CALCULATION: THE FERMI PARADOX ---
        # Complete Drake Equation: 10 × 1 × 0.1 × 1 × (400/10^10) ≈ 1/10,000,000
        t7 = MathTex(
            r"\text{Multiplying these together yields:}",
            r"~\frac{1}{10^7}",  # 1 in 10 million
            r"\text{or a 1 in 10 million chance that two advanced}",
            r"\text{civilizations coexist at once.}",
            r"\text{We Are Alone.}",
        )
        t7.scale(0.5).arrange(DOWN)
        t7.color = GOLD
        t7[4].color = RED  # Emphasize the sobering conclusion

        self.play(Write(t7[0:4]), run_time=8)
        self.wait()
        self.play(Write(t7[4]))  # The Fermi Paradox: Where is everybody?
        self.wait(5)
