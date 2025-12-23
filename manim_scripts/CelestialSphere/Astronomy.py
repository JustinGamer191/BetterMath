from manim import *
import pandas as pd
from tqdm import tqdm

# --- CELESTIAL SPHERE SETUP ---
# Creating the visual elements that represent Earth and celestial coordinates

# Earth's boundary - outer circle representing the celestial sphere
boundary = Circle(radius=2, color=GREEN)

# Celestial Equator - Earth's equator projected onto the celestial sphere
equator = Circle(radius=2, color=WHITE)
equator.stretch(
    0.2, dim=1
)  # Flatten vertically to create ellipse effect when viewed at angle

# Ecliptic - the plane of Earth's orbit around the Sun (tilted 23.4° from equator)
cEquator = Circle(radius=2, color=WHITE)
cEquator.stretch(0.2, dim=0)  # Flatten horizontally
cEquator.rotate(np.radians(90 + 23.4))  # Rotate to show Earth's axial tilt

# Sun marker - positioned at the Vernal Equinox (where ecliptic crosses celestial equator)
sun = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
sun.move_to([0, -0.4, 0])


# --- SCENE 1: INTRODUCTION TO THE CELESTIAL SPHERE ---
class CelestialSphere(Scene):
    def construct(self):
        # Title and description
        t1 = MathTex(r"\text{The Celestial Sphere}")
        t1.color = PURPLE
        t1.move_to([0, 3, 0])

        t2 = MathTex(r"\text{An imaginary sphere}")
        t3 = MathTex(r"\text{centered on Earth.}")

        t23 = VGroup(t2, t3)
        t23.arrange(DOWN).scale(0.5)
        t23.move_to([0, 2.25, 0])
        t23.color = PURPLE

        # Group all celestial sphere elements for easier manipulation
        earthDiagram = VGroup(boundary, equator, cEquator)

        # Display title
        self.play(Write(t1))

        # Draw the celestial sphere components
        self.play(Create(boundary), Create(equator), Create(cEquator))
        self.wait(0.5)

        # Zoom in dramatically to show detail
        self.play(earthDiagram.animate.scale(10), run_time=2.5)

        # Add descriptive text
        self.play(Write(t23))

        # Center all text elements
        self.play(VGroup(t1, t23).animate.move_to([0, 0, 0]))

        self.wait(1)

        # Clear text and recolor diagram elements for next scene
        self.play(FadeOut(VGroup(t1, t23)))
        boundary.color = PURPLE  # Celestial sphere boundary
        equator.color = RED  # Celestial equator
        cEquator.color = BLUE  # Ecliptic (plane of solar system)

        # Zoom back out to normal scale
        self.play(earthDiagram.animate.scale(0.1), run_time=2.5)

        self.wait(1)


# --- SCENE 2: EQUINOXES AND SOLSTICES ---
# Demonstrates how the Sun's position changes throughout the year
class EquatorEcliptic(Scene):
    def construct(self):
        # Set up colored celestial sphere from previous scene
        boundary.color = PURPLE
        equator.color = RED
        cEquator.color = BLUE
        self.add(VGroup(boundary, equator, cEquator))

        # --- LABEL: ECLIPTIC (PLANE OF SOLAR SYSTEM) ---
        # Create pointer line to ecliptic
        line1 = Line(
            [2 * np.cos(np.radians(23.4)), 2 * np.sin(np.radians(23.4)), 0],
            [3 * np.cos(np.radians(23.4)), 3 * np.sin(np.radians(23.4)), 0],
            color=BLUE,
        )
        t1 = MathTex(r"\text{Plane of the solar system}")
        t1.color = BLUE
        t1.scale(0.35)
        t1.move_to([3 * np.cos(np.radians(23.4)), 3 * np.sin(np.radians(23.4)), 0])
        t1.shift(0.25 * UP, 0.25 * RIGHT)

        # --- LABEL: CELESTIAL EQUATOR ---
        # Create pointer line to celestial equator
        line2 = Line(
            [-2, 0, 0],
            [-2 - np.cos(np.radians(-23.4)), np.sin(np.radians(23.4)), 0],
            color=RED,
        )
        t2 = MathTex(r"\text{Celestial Equator}")
        t3 = MathTex(r"\text{Equator of Earth extended to infinity.}")
        t23 = VGroup(t2, t3)
        t23.color = RED
        t23.arrange(DOWN)
        t23.scale(0.35)
        t23.move_to([-1 * np.cos(np.radians(-23.4)) - 2, np.sin(np.radians(23.4)), 0])
        t23.shift(0.25 * UP)
        bg23 = BackgroundRectangle(
            t23, fill_opacity=1, fill_color=BLACK
        )  # Background for readability

        # --- SEASONAL LABELS ---
        # Vernal (Spring) Equinox - March 20/21
        l3 = VGroup(
            MathTex(r"\text{Vernal Equinox}"),
            MathTex(
                r"\text{When the Celestial Equator intersects the Plane of the Solar System}"
            ),
        )
        l3.color = YELLOW
        l3.arrange(DOWN)
        l3.scale(0.35)
        l3.move_to(sun)
        l3.shift(0.75 * DOWN)
        bg3 = BackgroundRectangle(l3, fill_opacity=1, fill_color=BLACK)

        # Summer Solstice - June 20/21
        v2 = VGroup(
            MathTex(r"\text{Summer Solstice}"),
            MathTex(
                r"\text{When the Sun is at its highest Declination from the Celestial Equator}"
            ),
        )
        v2.color = YELLOW
        v2.arrange(DOWN)
        v2.scale(0.35)
        v2.move_to(sun)
        v2.shift(0.75 * DOWN)

        # Autumnal (Fall) Equinox - September 22/23
        v3 = VGroup(
            MathTex(r"\text{Autumnal Equinox}"),
            MathTex(r"\text{Directly above the Celestial Equator at Solar Noon}"),
        )
        v3.color = YELLOW
        v3.arrange(DOWN)
        v3.scale(0.35)
        v3.move_to(sun)
        v3.shift(0.75 * DOWN)

        # Winter Solstice - December 21/22
        v4 = VGroup(
            MathTex(r"\text{Winter Solstice}"),
            MathTex(
                r"\text{When the Sun is at its lowest Declination from the Celestial Equator}"
            ),
        )
        v4.color = YELLOW
        v4.arrange(DOWN)
        v4.scale(0.35)
        v4.move_to(sun)
        v4.shift(0.75 * DOWN)

        # --- ANIMATION SEQUENCE ---
        # Show and label the ecliptic
        self.play(Create(line1))
        self.play(Write(t1))
        self.wait(1)

        # Show and label the celestial equator
        self.play(Create(line2))
        self.add(bg23)
        self.play(Write(t23))
        self.wait(2)

        # Show Sun at Vernal Equinox
        self.play(Create(sun))
        self.add(bg3)
        self.play(Write(l3))
        self.wait(2)

        # Move Sun to Summer Solstice (1/4 orbit = 0.25 of path)
        self.play(
            MoveAlongPath(sun, cEquator, rate_func=lambda t: 0.25 * (t + 2)), run_time=2
        )
        self.play(Transform(l3, v2))
        self.wait(2)

        # Move Sun to Autumnal Equinox (1/2 orbit from vernal equinox)
        self.play(
            MoveAlongPath(sun, cEquator, rate_func=lambda t: 0.25 * (t + 3)), run_time=2
        )
        self.play(Transform(l3, v3))
        self.wait(2)

        # Move Sun to Winter Solstice (3/4 orbit)
        self.play(
            MoveAlongPath(sun, cEquator, rate_func=lambda t: 0.25 * (t)), run_time=2
        )
        self.play(Transform(l3, v4))
        self.wait(3)


# --- SCENE 3: MAPPING REAL STARS ---
# Uses actual astronomical data to plot stars on the celestial sphere
class Constellations(Scene):
    def construct(self):
        # Set up celestial sphere
        boundary.color = PURPLE
        equator.color = RED
        cEquator.color = BLUE
        self.add(VGroup(boundary, equator, cEquator))

        # --- LOAD STAR DATA FROM HIPPARCOS CATALOG ---
        # HYG Database contains 119,627 stars with position and brightness data
        df = pd.read_csv(r"./Data/hygdata_v41.csv")

        # Filter for visible stars (magnitude < 7, visible to naked eye in dark skies)
        df = df[df["mag"] < 7]

        # --- COORDINATE TRANSFORMATION: RA/DEC → CARTESIAN ---
        # Right Ascension (RA): measured in hours (0-24), convert to radians
        # Declination (Dec): measured in degrees (-90 to +90), convert to radians
        ra_all = np.radians(df["ra"] * 15)  # Multiply by 15 to convert hours to degrees
        dec_all = np.radians(df["dec"])

        # Convert spherical coordinates to Cartesian for 2D projection
        # x = cos(dec) * cos(ra)
        # y = cos(dec) * sin(ra)
        # z coordinate ignored for 2D celestial sphere projection
        x_all = np.cos(dec_all) * np.cos(ra_all)
        y_all = np.cos(dec_all) * np.sin(ra_all)
        positions_all = np.column_stack(
            [2 * x_all, 2 * y_all, np.zeros_like(x_all)]
        )  # Scale by 2 to match sphere radius

        # Create dictionary mapping star IDs to positions
        star_positions_all = {
            int(row.id): pos
            for row, pos in zip(df.itertuples(index=False), positions_all)
        }

        # Create visual dots for all visible stars
        stars_all = VGroup(
            *[
                Dot(point=pos, radius=0.025, color=WHITE)
                for pos in star_positions_all.values()
            ]
        )

        # --- FILTER FOR BRIGHTEST STARS (mag < 3) ---
        # These are the 183 brightest stars, easily visible from Earth
        df = df[df["mag"] < 3]

        # Repeat coordinate transformation for bright stars only
        ra_rad = np.radians(df["ra"] * 15)
        dec_rad = np.radians(df["dec"])
        x = np.cos(dec_rad) * np.cos(ra_rad)
        y = np.cos(dec_rad) * np.sin(ra_rad)
        positions = np.column_stack([2 * x, 2 * y, np.zeros_like(x)])

        star_positions = {
            int(row.id): pos for row, pos in zip(df.itertuples(index=False), positions)
        }

        # Create visual dots for brightest stars
        stars = VGroup(
            *[
                Dot(point=pos, radius=0.025, color=WHITE)
                for pos in star_positions.values()
            ]
        )
        self.play(Create(stars, run_time=2))

        # --- LABEL NORTH CELESTIAL POLE ---
        # The point in the sky directly above Earth's North Pole
        arrow = Arrow(start=[0, 0, 0], end=[0, 2.5, 0], color=YELLOW, buff=0)
        label = Text("North Celestial Pole", font_size=18, color=YELLOW).next_to(
            arrow, UP, buff=0.1
        )
        VGroup(arrow, label).rotate_about_origin(
            np.radians(23.4)
        )  # Account for Earth's tilt

        self.play(Create(arrow), Write(label))
        self.wait(1)

        # Explain the 183 brightest stars
        m1 = MathTex(
            r"\text{These are the 183 brightest stars out}",
            r"\text{of the trillions of stars in the Celestial Sphere.}",
        )
        m1.scale(0.5)
        m1.arrange(DOWN)
        m1.move_to([0, 3.5, 0])
        self.play(Write(m1))
        self.wait(2)

        # Remove coordinate grid and show all 16,000 visible stars
        self.play(FadeOut(equator, cEquator, arrow, label))
        self.play(Create(stars_all, run_time=2))
        self.wait(1)

        # Update text to reflect all visible stars shown
        m2 = MathTex(r"\text{And this is only 16,000 of the brightest stars.}")
        m2.scale(0.5)
        m2.arrange(DOWN)
        m2.move_to([0, 2.75, 0])
        self.play(Write(m2))
        self.play(FadeOut(m1))

        self.wait(2)

        # Clear the screen except for the bright stars
        self.play(FadeOut(m2, stars_all))
        self.wait(1)

        # --- FINALE: ZOOM INTO THE STARS ---
        # Poetic conclusion showing the beauty of the universe
        mconc = MathTex(r"\text{What a beautiful universe we live in.}")
        mconc.scale(0.5)
        mconc.move_to([0, 1, 0])
        mconc.color = YELLOW

        # Dramatic zoom into the stars, creating an immersive effect
        self.play(VGroup(stars, boundary).animate.scale(20), run_time=2)
        self.play(Write(mconc))
        self.wait(3)
