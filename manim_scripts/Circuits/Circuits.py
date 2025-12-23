from manim import *


# --- SCENE 1: INTRODUCTION TO PARALLEL CIRCUITS ---
# Introduces the parallel resistance formula and demonstrates real-world applications
# Brilliant.org Partnership Video #2
class Intro(Scene):
    def construct(self):
        # --- PARALLEL RESISTANCE FORMULA ---
        # In a parallel circuit, the reciprocal of total resistance equals the sum of reciprocals
        # 1/R_T = 1/R_1 + 1/R_2 + 1/R_3 + ...
        # This means total resistance is LESS than the smallest individual resistance
        eq1 = MathTex(
            r"\frac{1}{R_T} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots"
        )
        eq1.scale(0.5)

        self.play(Write(eq1))
        self.wait()
        self.play(eq1.animate.move_to([0, 3, 0]))

        # --- REAL-WORLD APPLICATION 1: LIGHT BULB ---
        # Demonstrates how parallel circuits allow devices to operate independently
        def drawLightBulb():
            # Main glass bulb
            bulb = Circle(radius=1, color=YELLOW, fill_opacity=0.3)
            bulb.shift(UP * 0.5)

            # Filament inside bulb (tungsten wire that glows when heated)
            filament = VGroup(
                Line(ORIGIN, UP * 0.3, color=ORANGE),  # Vertical support wire
                Arc(radius=0.15, start_angle=PI, angle=PI, color=ORANGE).shift(
                    UP * 0.3
                ),  # Coiled filament
                Line(UP * 0.45, UP * 0.6, color=ORANGE),  # Top support wire
            )
            filament.shift(UP * 0.3)

            # Metal screw base components
            base_top = Rectangle(width=0.6, height=0.15, color=GRAY, fill_opacity=1)
            base_top.next_to(bulb, DOWN, buff=0)

            # Threaded metal base (contacts the socket)
            threads = VGroup()
            for i in range(4):
                thread = Rectangle(
                    width=0.5, height=0.08, color=DARK_GRAY, fill_opacity=1
                )
                thread.next_to(base_top, DOWN, buff=i * 0.1)
                threads.add(thread)

            # Bottom electrical contact
            base_bottom = Circle(radius=0.25, color=GRAY, fill_opacity=1)
            base_bottom.next_to(threads, DOWN, buff=0.05)

            lightbulb = VGroup(bulb, filament, base_top, threads, base_bottom)
            self.play(Write(lightbulb), run_time=1)

            # --- LIGHTING EFFECT ---
            # Create glowing effect when bulb turns on
            glow = Circle(radius=1.3, color=YELLOW, fill_opacity=0.2, stroke_opacity=0)
            glow.move_to(bulb.get_center())

            # Turn on the bulb
            self.play(
                bulb.animate.set_fill(YELLOW, opacity=0.8),  # Bulb lights up
                filament.animate.set_color(WHITE),  # Filament heats to white-hot
                FadeIn(glow),
                run_time=0.5,
            )

            # Pulsing glow effect
            self.play(
                glow.animate.scale(1.2).set_fill(opacity=0.1),
                rate_func=there_and_back,
                run_time=1,
            )

            self.play(FadeOut(lightbulb, glow))

        drawLightBulb()

        # --- REAL-WORLD APPLICATION 2: PHONE CHARGING ---
        # Shows how parallel circuits enable multiple devices to charge from one source
        def drawPhoneCharge():
            # --- SMARTPHONE BODY ---
            phone_body = RoundedRectangle(
                width=2,
                height=3.5,
                corner_radius=0.2,
                color=WHITE,
                fill_opacity=1,
                fill_color=BLUE_E,  # Dark blue phone body
                stroke_width=3,
            )

            # Screen (lighter blue)
            screen = RoundedRectangle(
                width=1.8,
                height=3.2,
                corner_radius=0.15,
                color=BLUE_D,
                fill_opacity=1,
                fill_color=BLUE_D,
                stroke_width=0,
            )
            screen.move_to(phone_body.get_center())

            # USB-C/Lightning charging port at bottom
            charging_port = Rectangle(
                width=0.4, height=0.1, color=DARK_GRAY, fill_opacity=1
            )
            charging_port.next_to(phone_body, DOWN, buff=-0.15)

            # Home button or sensor notch
            notch = Circle(
                radius=0.15,
                color=BLUE_E,
                fill_opacity=1,
                stroke_width=2,
                stroke_color=BLUE_D,
            )
            notch.next_to(phone_body, DOWN, buff=-0.25)

            phone = VGroup(phone_body, screen, charging_port, notch)
            phone.shift(UP * 0.5)

            # --- CHARGING CABLE ---
            # USB connector plug
            cable_plug = RoundedRectangle(
                width=0.35,
                height=0.2,
                corner_radius=0.05,
                color=WHITE,
                fill_opacity=1,
                stroke_width=2,
            )
            cable_plug.shift(DOWN * 2.5)

            # Cable wire
            cable_wire = Line(
                start=cable_plug.get_top(),
                end=cable_plug.get_top() + DOWN * 1.5,
                color=WHITE,
                stroke_width=6,
            )

            # --- BATTERY INDICATOR ---
            # Battery icon showing charge level
            battery_outline = RoundedRectangle(
                width=0.8, height=0.4, corner_radius=0.05, color=WHITE, stroke_width=3
            )
            battery_outline.move_to(screen.get_center())

            # Small battery terminal
            battery_tip = Rectangle(
                width=0.05, height=0.15, color=WHITE, fill_opacity=1
            )
            battery_tip.next_to(battery_outline, RIGHT, buff=0)

            # Battery fill level (starts low at 15%)
            battery_fill = Rectangle(width=0.7, height=0.3, color=RED, fill_opacity=1)
            battery_fill.move_to(battery_outline.get_center())
            battery_fill.stretch_to_fit_width(0.1)  # Very narrow = low battery
            battery_fill.move_to(battery_outline.get_center())
            battery_fill.shift(LEFT * 0.3)

            battery = VGroup(battery_outline, battery_tip, battery_fill)
            battery.shift(UP * 0.3)

            # Low battery percentage text
            low_battery_text = Text("15%", font_size=24, color=RED)
            low_battery_text.next_to(battery, DOWN, buff=0.3)

            # --- ANIMATION SEQUENCE: CHARGING PROCESS ---
            # Show phone with low battery
            self.play(FadeIn(phone), run_time=0.8)
            self.play(
                FadeIn(battery_outline),
                FadeIn(battery_tip),
                FadeIn(battery_fill),
                run_time=0.5,
            )
            self.play(Write(low_battery_text), run_time=0.5)
            self.wait(0.5)

            # Show charging cable
            self.play(FadeIn(cable_plug), FadeIn(cable_wire), run_time=0.5)
            self.wait(0.3)

            # Plug in the cable
            self.play(
                cable_plug.animate.move_to(charging_port.get_center() + DOWN * 0.3),
                cable_wire.animate.put_start_and_end_on(
                    charging_port.get_center() + DOWN * 0.3,
                    charging_port.get_center() + DOWN * 2,
                ),
                run_time=1.5,
                rate_func=smooth,
            )

            # Click sound effect (cable seats in port)
            self.play(cable_plug.animate.shift(UP * 0.2), run_time=0.3)

            # --- CHARGING BEGINS ---
            # Flash effect when charging starts
            flash = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5)
            flash.move_to(charging_port.get_center())
            self.play(FadeIn(flash, scale=0.5), run_time=0.2)
            self.play(FadeOut(flash, scale=1.5), run_time=0.3)

            # Battery indicator changes to green (charging)
            self.play(
                battery_fill.animate.set_color(GREEN),
                low_battery_text.animate.set_color(GREEN),
                run_time=0.3,
            )

            # Battery fills up
            new_fill = Rectangle(width=0.7, height=0.3, color=GREEN, fill_opacity=1)
            new_fill.move_to(battery_outline.get_center())

            self.play(
                Transform(battery_fill, new_fill),  # Fill expands to full width
                low_battery_text.animate.become(
                    Text("Charging", font_size=24, color=GREEN).next_to(
                        battery, DOWN, buff=0.3
                    )
                ),
                run_time=2,
            )

            # Lightning bolt icon (standard charging symbol)
            lightning = Text("⚡", font_size=30, color=YELLOW)
            lightning.move_to(battery_outline.get_center())
            self.play(FadeIn(lightning, scale=0.5), run_time=0.3)

            # Pulsing lightning effect
            self.play(
                lightning.animate.scale(1.2), rate_func=there_and_back, run_time=0.5
            )

            # Clean up
            self.play(
                FadeOut(
                    VGroup(
                        phone,
                        battery,
                        low_battery_text,
                        cable_plug,
                        cable_wire,
                        lightning,
                    )
                )
            )

        drawPhoneCharge()

        # --- SHOW PARALLEL CIRCUIT DIAGRAM ---
        # Reference image showing the electrical schematic
        parallel = ImageMobject("./images/parallelBG.png")
        parallel.scale(0.5)
        self.play(FadeIn(parallel))
        self.wait()


# --- SCENE 2: PARALLEL CIRCUIT WITH RESISTORS ---
# Demonstrates how resistors behave in parallel configuration
class ParallelCircuit(Scene):
    def construct(self):
        # --- BATTERY (VOLTAGE SOURCE) ---
        # Provides electrical potential difference (voltage V)
        battery_body = Rectangle(width=0.3, height=1.5, color=WHITE, stroke_width=3)
        battery_body.shift(LEFT * 4)

        # Positive terminal (longer line in standard battery symbol)
        positive_terminal = Line(UP * 0.25, DOWN * 0.25, color=RED, stroke_width=6)
        positive_terminal.next_to(battery_body, UP, buff=0)

        # Negative terminal (shorter line in standard battery symbol)
        negative_terminal = Line(UP * 0.15, DOWN * 0.15, color=BLUE, stroke_width=6)
        negative_terminal.next_to(battery_body, DOWN, buff=0)

        # Polarity labels
        plus_sign = Text("+", font_size=30, color=RED)
        plus_sign.next_to(positive_terminal, LEFT, buff=0.2)

        minus_sign = Text("−", font_size=30, color=BLUE)
        minus_sign.next_to(negative_terminal, LEFT, buff=0.2)

        # --- CIRCUIT WIRING ---
        # Top wire (positive rail)
        top_wire = Line(
            battery_body.get_top() + UP * 0.25,
            RIGHT * 4 + UP * 2,
            color=WHITE,
            stroke_width=3,
        )

        # Bottom wire (ground/negative rail)
        bottom_wire = Line(
            battery_body.get_bottom() + DOWN * 0.25,
            RIGHT * 4 + DOWN * 2,
            color=WHITE,
            stroke_width=3,
        )

        # Right connecting wire (completes the circuit)
        right_wire = Line(
            RIGHT * 4 + UP * 2, RIGHT * 4 + DOWN * 2, color=WHITE, stroke_width=3
        )

        # --- BRANCH 1: FIRST RESISTOR PATH ---
        branch1_left = Line(
            LEFT * 1 + UP * 2, LEFT * 1 + UP * 0.5, color=WHITE, stroke_width=3
        )
        resistor1 = self.create_resistor(LEFT * 1 + UP * 0.5, LEFT * 1 + DOWN * 0.5)
        branch1_right = Line(
            LEFT * 1 + DOWN * 0.5, LEFT * 1 + DOWN * 2, color=WHITE, stroke_width=3
        )

        # --- BRANCH 2: SECOND RESISTOR PATH ---
        branch2_left = Line(
            RIGHT * 1.5 + UP * 2, RIGHT * 1.5 + UP * 0.5, color=WHITE, stroke_width=3
        )
        resistor2 = self.create_resistor(
            RIGHT * 1.5 + UP * 0.5, RIGHT * 1.5 + DOWN * 0.5
        )
        branch2_right = Line(
            RIGHT * 1.5 + DOWN * 0.5,
            RIGHT * 1.5 + DOWN * 2,
            color=WHITE,
            stroke_width=3,
        )

        # --- COMPONENT LABELS ---
        r1_label = MathTex("R_1", font_size=32, color=YELLOW)
        r1_label.next_to(resistor1, LEFT, buff=0.4)

        r2_label = MathTex("R_2", font_size=32, color=YELLOW)
        r2_label.next_to(resistor2, RIGHT, buff=0.4)

        v_label = Text("V", font_size=32, color=WHITE)
        v_label.next_to(battery_body, LEFT, buff=0.5)

        # --- BRANCH 3: EQUIVALENT SINGLE RESISTOR ---
        # Shows how parallel resistors can be replaced by one equivalent resistor R_T
        branch3_left = Line(
            RIGHT * 1 + UP * 2, RIGHT * 1 + UP * 0.5, color=WHITE, stroke_width=3
        )
        resistor3 = self.create_resistor(RIGHT * 1 + UP * 0.5, RIGHT * 1 + DOWN * 0.5)
        branch3_right = Line(
            RIGHT * 1 + DOWN * 0.5,
            RIGHT * 1 + DOWN * 2,
            color=WHITE,
            stroke_width=3,
        )
        r3_label = MathTex("R_3", font_size=32, color=YELLOW)
        r3_label.next_to(resistor3, RIGHT, buff=0.4)

        # --- ANIMATION: SHOW PARALLEL RESISTORS ---
        self.play(
            Write(
                VGroup(
                    battery_body,
                    positive_terminal,
                    negative_terminal,
                    plus_sign,
                    minus_sign,
                    v_label,
                    top_wire,
                    bottom_wire,
                    branch1_left,
                    resistor1,
                    branch1_right,
                    branch2_left,
                    resistor2,
                    branch2_right,
                    r1_label,
                    r2_label,
                )
            )
        )
        self.wait()

        # --- TRANSITION: REPLACE WITH EQUIVALENT RESISTOR ---
        # Remove parallel resistors
        self.play(
            FadeOut(
                branch1_left,
                resistor1,
                branch1_right,
                branch2_left,
                resistor2,
                branch2_right,
                r1_label,
                r2_label,
            )
        )

        # Show single equivalent resistor R_3
        self.play(FadeIn(branch3_left, branch3_right, r3_label, resistor3))
        self.wait()

    # --- HELPER FUNCTION: CREATE RESISTOR SYMBOL ---
    # Draws the zigzag symbol used to represent resistance in circuit diagrams
    def create_resistor(self, start_point, end_point):
        points = []
        num_segments = 8  # Number of zigzag segments
        segment_length = (end_point[1] - start_point[1]) / num_segments
        width = 0.3  # Width of zigzag

        points.append(start_point)

        # Create zigzag pattern
        for i in range(1, num_segments):
            y = start_point[1] + i * segment_length
            if i % 2 == 1:  # Alternate left and right
                x = start_point[0] + width
            else:
                x = start_point[0] - width
            points.append([x, y, 0])

        points.append(end_point)

        resistor = VMobject(color=WHITE, stroke_width=3)
        resistor.set_points_as_corners(points)  # Connect points with straight lines

        return resistor


# --- SCENE 3: PARALLEL CIRCUIT WITH LIGHT BULBS ---
# Demonstrates key property: each bulb gets full voltage in parallel
class ParallelLightbulbs(Scene):
    def construct(self):
        # --- BATTERY SETUP (same as previous scene) ---
        battery_body = Rectangle(width=0.3, height=1.5, color=WHITE, stroke_width=3)
        battery_body.shift(LEFT * 4)

        positive_terminal = Line(UP * 0.25, DOWN * 0.25, color=RED, stroke_width=6)
        positive_terminal.next_to(battery_body, UP, buff=0)

        negative_terminal = Line(UP * 0.15, DOWN * 0.15, color=BLUE, stroke_width=6)
        negative_terminal.next_to(battery_body, DOWN, buff=0)

        plus_sign = Text("+", font_size=30, color=RED)
        plus_sign.next_to(positive_terminal, LEFT, buff=0.2)

        minus_sign = Text("−", font_size=30, color=BLUE)
        minus_sign.next_to(negative_terminal, LEFT, buff=0.2)

        # --- WIRING ---
        top_wire = Line(
            battery_body.get_top() + UP * 0.25,
            RIGHT * 4 + UP * 2,
            color=WHITE,
            stroke_width=3,
        )

        bottom_wire = Line(
            battery_body.get_bottom() + DOWN * 0.25,
            RIGHT * 4 + DOWN * 2,
            color=WHITE,
            stroke_width=3,
        )

        right_wire = Line(
            RIGHT * 4 + UP * 2, RIGHT * 4 + DOWN * 2, color=WHITE, stroke_width=3
        )

        # --- BRANCH 1: FIRST LIGHT BULB ---
        branch1_top = Line(
            LEFT * 1 + UP * 2, LEFT * 1 + UP * 1, color=WHITE, stroke_width=3
        )
        lightbulb1 = self.create_lightbulb(LEFT * 1)
        branch1_bottom = Line(
            LEFT * 1 + DOWN * 1, LEFT * 1 + DOWN * 2, color=WHITE, stroke_width=3
        )

        # --- BRANCH 2: SECOND LIGHT BULB ---
        branch2_top = Line(
            RIGHT * 1.5 + UP * 2, RIGHT * 1.5 + UP * 1, color=WHITE, stroke_width=3
        )
        lightbulb2 = self.create_lightbulb(RIGHT * 1.5)
        branch2_bottom = Line(
            RIGHT * 1.5 + DOWN * 1, RIGHT * 1.5 + DOWN * 2, color=WHITE, stroke_width=3
        )

        # Labels
        l1_label = MathTex("L", font_size=32, color=YELLOW)
        l1_label.next_to(lightbulb1, LEFT, buff=0.5)

        l2_label = MathTex("L", font_size=32, color=YELLOW)
        l2_label.next_to(lightbulb2, RIGHT, buff=0.5)

        v_label = Text("V", font_size=32, color=WHITE)
        v_label.next_to(battery_body, LEFT, buff=0.5)

        # --- SHOW PARALLEL BULBS AND LIGHT THEM UP ---
        self.play(
            Write(
                VGroup(
                    battery_body,
                    positive_terminal,
                    negative_terminal,
                    plus_sign,
                    minus_sign,
                    v_label,
                    top_wire,
                    bottom_wire,
                    branch1_top,
                    lightbulb1,
                    branch1_bottom,
                    branch2_top,
                    lightbulb2,
                    branch2_bottom,
                    l1_label,
                    l2_label,
                )
            )
        )

        self.wait(0.5)

        # Create glow effects for both bulbs
        glow1 = Circle(radius=0.9, color=YELLOW, fill_opacity=0.3, stroke_opacity=0)
        glow1.move_to(lightbulb1[0].get_center())

        glow2 = Circle(radius=0.9, color=YELLOW, fill_opacity=0.3, stroke_opacity=0)
        glow2.move_to(lightbulb2[0].get_center())

        # Both bulbs light up simultaneously (key parallel property!)
        # Each gets full battery voltage V
        self.play(
            lightbulb1[0].animate.set_fill(YELLOW, opacity=0.7),
            lightbulb1[1].animate.set_color(WHITE),
            lightbulb1[2].animate.set_color(WHITE),
            lightbulb2[0].animate.set_fill(YELLOW, opacity=0.7),
            lightbulb2[1].animate.set_color(WHITE),
            lightbulb2[2].animate.set_color(WHITE),
            FadeIn(glow1),
            FadeIn(glow2),
            run_time=1,
        )

        self.wait(1)

        # --- REPLACE WITH EQUIVALENT SINGLE BULB ---
        self.play(
            FadeOut(lightbulb1),
            FadeOut(lightbulb2),
            FadeOut(glow1),
            FadeOut(glow2),
            FadeOut(branch1_top),
            FadeOut(branch1_bottom),
            FadeOut(branch2_top),
            FadeOut(branch2_bottom),
            FadeOut(l1_label),
            FadeOut(l2_label),
            run_time=1,
        )

        self.wait(0.5)

        # Show equivalent total resistance as single bulb L_T
        branch3_top = Line(
            RIGHT * 0.25 + UP * 2, RIGHT * 0.25 + UP * 1, color=WHITE, stroke_width=3
        )
        lightbulb3 = self.create_lightbulb(RIGHT * 0.25)
        branch3_bottom = Line(
            RIGHT * 0.25 + DOWN * 1,
            RIGHT * 0.25 + DOWN * 2,
            color=WHITE,
            stroke_width=3,
        )

        l3_label = MathTex(
            "L_T", font_size=32, color=YELLOW
        )  # Total equivalent resistance
        l3_label.next_to(lightbulb3, LEFT)

        self.play(
            Create(branch3_top),
            Create(branch3_bottom),
            FadeIn(lightbulb3),
            Write(l3_label),
            run_time=1,
        )

        self.wait(0.5)

        # Light up the equivalent bulb
        glow3 = Circle(radius=0.9, color=YELLOW, fill_opacity=0.3, stroke_opacity=0)
        glow3.move_to(lightbulb3[0].get_center())

        self.play(
            lightbulb3[0].animate.set_fill(YELLOW, opacity=0.7),
            lightbulb3[1].animate.set_color(WHITE),
            lightbulb3[2].animate.set_color(WHITE),
            FadeIn(glow3),
            run_time=1,
        )

        self.wait(2)

        # Complete the circuit
        self.play(FadeIn(right_wire))
        self.wait()
        self.play(FadeOut(glow3))
        self.wait()

    # --- HELPER FUNCTION: CREATE LIGHT BULB SYMBOL ---
    # Draws a simplified light bulb for circuit diagrams
    def create_lightbulb(self, center_position):
        # Glass bulb (circle)
        bulb = Circle(radius=0.7, color=YELLOW, stroke_width=3)
        bulb.move_to(center_position)

        # Filament (X pattern inside bulb)
        filament1 = Line(
            center_position + UP * 0.3 + LEFT * 0.3,
            center_position + DOWN * 0.3 + RIGHT * 0.3,
            color=ORANGE,
            stroke_width=2,
        )
        filament2 = Line(
            center_position + UP * 0.3 + RIGHT * 0.3,
            center_position + DOWN * 0.3 + LEFT * 0.3,
            color=ORANGE,
            stroke_width=2,
        )

        # Metal base/socket
        base = Rectangle(
            width=0.5, height=0.3, color=GRAY, fill_opacity=0.5, stroke_width=2
        )
        base.next_to(bulb, DOWN, buff=0)

        lightbulb = VGroup(bulb, filament1, filament2, base)

        return lightbulb
