from manim import *
import random
import copy


# Function that generates a card given a number and color
def getCard(num, color=WHITE):
    rect = Rectangle(color=color, height=1, width=0.75)
    indicator = MathTex(num, color=color)
    return VGroup(rect, indicator)


# Introduction scene
class Introduction(Scene):
    def construct(self):
        text1 = MathTex(
            r"\text{'No two decks have ever been shuffled in the same sequence'}"
        )
        text2 = MathTex(r"\text{Why?}")
        self.play(Write(text1))
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait()


# Shows the factorial growth of cards
class CardPermutations(Scene):
    def construct(self):
        # Generate the cards
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        positions = [-4.8 + x / 1.25 for x in range(13)]
        white = VGroup()
        red = VGroup()
        blue = VGroup()
        green = VGroup()

        for _ in range(len(cards)):
            white.add(getCard(cards[_]).move_to([positions[_], 0, 0]))
            red.add(getCard(cards[_], RED).move_to([positions[_], 0, 0]))
            blue.add(getCard(cards[_], BLUE).move_to([positions[_], 0, 0]))
            green.add(getCard(cards[_], GREEN).move_to([positions[_], 0, 0]))

        # Position the cards
        white.move_to([0, 1.5, 0])
        red.move_to([0, 0.5, 0])
        blue.move_to([0, -0.5, 0])
        green.move_to([0, -1.5, 0])

        # Display the card
        self.play(Write(white), Write(red), Write(blue), Write(green))
        self.wait()

        # Collapse the cards into one pile
        text1 = MathTex(r"\text{Deck}")
        text1.move_to([0, 3, 0])
        self.play(FadeIn(text1))

        # Place cards into a deck
        for _ in range(len(cards)):
            self.play(
                white[_].animate.move_to([0, 2, 0]),
                red[_].animate.move_to([0, 2, 0]),
                blue[_].animate.move_to([0, 2, 0]),
                green[_].animate.move_to([0, 2, 0]),
                run_time=0.2,
            )

        # The back design of each card
        logo = ImageMobject("./img/logo.png")
        gold_card = Rectangle(height=1, width=0.75, fill_opacity=1, color=GOLD)

        gold_card.move_to([0, 2, 0])
        logo.scale_to_fit_width(0.75)
        logo.move_to([0, 2, 0])

        self.add(gold_card, logo)
        self.add(logo)

        # Pull a random card from the deck
        entire_deck = VGroup(white, red, blue, green)
        amount = 52
        for _ in range(5):
            # Update counter for number of cards remaining
            current_amt = MathTex(amount)
            current_amt.move_to([0, 1, 0])
            self.play(Write(current_amt))
            self.play(current_amt.animate.move_to([-3 + _ * 1, -1, 0]))
            amount -= 1
            # Select from a random suit
            random_suit = random.randint(0, 3)
            # Select a random number from that suit
            random_number = random.randint(0, len(entire_deck[random_suit]) - 1)
            # Select the card with that suit and number
            pulled_card = entire_deck[random_suit][random_number]
            # Move it to the pulled card pile
            self.play(pulled_card.animate.move_to([0, 0, 0]))
            # Copy the card object
            pulled_card_copy = copy.copy(pulled_card)
            # Make only 1 card visible at a time
            black_card = Rectangle(height=1, width=0.75, fill_opacity=1, color=BLACK)
            self.add(black_card)
            self.add(pulled_card_copy)
            # Remove the pulled card from the deck
            entire_deck[random_suit].remove(pulled_card)

        # Function that generates a multiplcation symbol given a position
        def generate_multiplication(position):
            mult = MathTex(r"\times")
            mult.move_to(position)
            return mult

        # Adds the five symbols to a group
        mult_signs = VGroup()
        for _ in range(5):
            new_mult = generate_multiplication([-2.5 + _ * 1, -1, 0])
            mult_signs.add(new_mult)
        # ... text
        continuation = MathTex(r"\dots")
        continuation.move_to([2, -1, 0])
        # Show all text
        self.play(FadeIn(mult_signs, continuation))
        self.wait()


class Lottery(Scene):
    def construct(self):
        fact = MathTex(r"52!")
        actual = MathTex(r"8\times10^{67}")
        actual_expanded = MathTex(
            r"80000000000000000000000000000000000000000000000000000000000000000000"
        )

        jackpot_chance = MathTex(r"\frac{1}{292000000}")

        self.play(FadeIn(fact))
        self.play(FadeOut(fact), FadeIn(actual_expanded))
        self.play(FadeOut(actual_expanded), FadeIn(jackpot_chance))
        self.play(FadeOut(jackpot_chance))
        for _ in range(4):
            self.play(
                Write(MathTex(r"292\times10^6").move_to([-3 + _ * 3, 0, 0])),
                Write(MathTex(r"\times").move_to([-1.5 + _ * 3, 0, 0])),
            )
        self.play(Write(MathTex(r"\text{8 TIMES!!! IN A ROW!!!}").move_to([0, 1, 0])))
        self.play(
            FadeIn(actual.move_to([-5.5, 0, 0])),
            FadeIn(MathTex(r">").move_to([-4.35, 0, 0])),
        )
        self.wait()


class Aliens(Scene):
    def construct(self):
        # Some text
        age_years = MathTex(r"\text{13.8 billion years}")
        age_seconds = MathTex(r"435\times10^{15} \text{seconds}")
        universe_amount = MathTex(r"435\times10^{15} \text{universes}")
        population = MathTex(r"435\times10^{15} \frac{\text{decks}}{\text{second}}")

        total = MathTex(r"8\times10^{67} > ")

        # Displaying age of universe in seconds
        self.play(Write(age_years))
        self.play(Transform(age_years, age_seconds))
        self.play(age_years.animate.move_to([-4, 3, 1]))

        # Animating universes
        central_universe = Circle(
            radius=0.5, color=YELLOW, fill_opacity=0.3, stroke_width=3
        )

        # Create surrounding universes
        universes = VGroup()

        # Grid of universes
        grid_size = 15  # 15x15 = 225 universes visible
        spacing = 1.2

        for i in range(-grid_size, grid_size + 1):
            for j in range(-grid_size, grid_size + 1):
                if i == 0 and j == 0:
                    continue  # Skip center (our universe)

                # Create universe bubble
                position = np.array([i * spacing, j * spacing, 0])

                # Vary colors slightly for visual interest
                hue = (i + grid_size) / (2 * grid_size)
                color = interpolate_color(BLUE, PURPLE, hue)

                universe = Circle(
                    radius=0.4, color=color, fill_opacity=0.2, stroke_width=1.5
                ).move_to(position)

                # Add some visual variety - make distant ones smaller
                distance = np.linalg.norm(position)
                scale_factor = max(0.5, 1 - distance / 30)
                universe.scale(scale_factor)

                universes.add(universe)

        # Animate appearance
        self.play(Create(central_universe))

        # Show surrounding universes appearing in waves
        self.play(
            LaggedStart(*[Create(u) for u in universes], lag_ratio=0.005, run_time=3)
        )

        # Show universe amount
        self.play(Write(universe_amount.move_to([-4, 2, 1])))
        self.wait()

        self.play(universes.animate.scale(500), central_universe.animate.scale(500))

        # Create a single alien function
        def create_alien(scale=1.0, color=GREEN):
            # Head (circle)
            head = Circle(radius=0.3 * scale, color=color, fill_opacity=0.8)

            # Eyes (two small circles)
            left_eye = Circle(radius=0.08 * scale, color=BLACK, fill_opacity=1)
            left_eye.shift(LEFT * 0.1 * scale + UP * 0.05 * scale)
            right_eye = Circle(radius=0.08 * scale, color=BLACK, fill_opacity=1)
            right_eye.shift(RIGHT * 0.1 * scale + UP * 0.05 * scale)

            # Pupils (even smaller white dots)
            left_pupil = Circle(radius=0.03 * scale, color=WHITE, fill_opacity=1)
            left_pupil.move_to(left_eye.get_center())
            right_pupil = Circle(radius=0.03 * scale, color=WHITE, fill_opacity=1)
            right_pupil.move_to(right_eye.get_center())

            # Antennae
            left_antenna = Line(
                start=head.get_top() + LEFT * 0.1 * scale,
                end=head.get_top() + LEFT * 0.15 * scale + UP * 0.2 * scale,
                color=color,
                stroke_width=2,
            )
            left_ball = Circle(radius=0.05 * scale, color=color, fill_opacity=1)
            left_ball.move_to(left_antenna.get_end())

            right_antenna = Line(
                start=head.get_top() + RIGHT * 0.1 * scale,
                end=head.get_top() + RIGHT * 0.15 * scale + UP * 0.2 * scale,
                color=color,
                stroke_width=2,
            )
            right_ball = Circle(radius=0.05 * scale, color=color, fill_opacity=1)
            right_ball.move_to(right_antenna.get_end())

            # Body (rounded rectangle or ellipse)
            body = Ellipse(
                width=0.4 * scale, height=0.5 * scale, color=color, fill_opacity=0.8
            )
            body.next_to(head, DOWN, buff=0.05 * scale)

            # Arms
            left_arm = Line(
                start=body.get_corner(UL),
                end=body.get_corner(UL) + LEFT * 0.15 * scale + DOWN * 0.1 * scale,
                color=color,
                stroke_width=3,
            )
            right_arm = Line(
                start=body.get_corner(UR),
                end=body.get_corner(UR) + RIGHT * 0.15 * scale + DOWN * 0.1 * scale,
                color=color,
                stroke_width=3,
            )

            alien = VGroup(
                body,
                head,
                left_eye,
                right_eye,
                left_pupil,
                right_pupil,
                left_antenna,
                left_ball,
                right_antenna,
                right_ball,
                left_arm,
                right_arm,
            )

            return alien

        # Create a large crowd of aliens
        aliens = VGroup()

        # Grid arrangement for lots of aliens
        rows = 20
        cols = 30
        spacing_x = 1
        spacing_y = 1

        # Calculate offsets to center the grid
        offset_x = -(cols - 1) * spacing_x / 2
        offset_y = -(rows - 1) * spacing_y / 2

        alien_colors = [GREEN, TEAL, BLUE, PURPLE, PINK]

        for row in range(rows):
            for col in range(cols):
                # Random size variation
                scale = random.uniform(0.6, 1.0)

                # Random color
                color = random.choice(alien_colors)

                # Create alien
                alien = create_alien(scale=scale, color=color)

                # Position in grid
                x = offset_x + col * spacing_x + random.uniform(-0.05, 0.05)
                y = offset_y + row * spacing_y + random.uniform(-0.05, 0.05)
                alien.move_to([x, y, 0])

                aliens.add(alien)

        self.play(
            LaggedStart(
                *[FadeIn(alien, shift=UP * 0.1) for alien in aliens],
                lag_ratio=0.002,
                run_time=4
            )
        )
        population.move_to([-4, 1, 1])

        # Show total numbers
        backRect = BackgroundRectangle(age_years, universe_amount, population, buff=0.2)
        self.add(backRect)
        self.add(age_years, universe_amount)
        self.play(Write(population))
        self.play(
            FadeOut(aliens, central_universe, backRect),
            VGroup(age_years, universe_amount, population).animate.move_to([0, 0, 0]),
        )
        self.play(
            FadeIn(total.move_to([-1.5, 0, 0])),
            VGroup(age_years, universe_amount, population).animate.move_to([2, 0, 0]),
        )
        self.wait()
