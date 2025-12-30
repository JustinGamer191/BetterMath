from manim import *
import numpy as np


# Brilliant Partnership #4
# Examples of vectors
class First(Scene):
    def construct(self):
        v1 = Vector([2, 1])

        v2 = MathTex(r"\vec{v} = \begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix}")

        self.play(Write(v1))

        self.play(FadeOut(v1))

        self.play(Write(v2))

        self.wait()


# Telescope helper function
def create_telescope(earth_pos, radial_dir, earth_radius):
    # Telescope base (tripod stand)
    base_start = earth_pos + radial_dir * earth_radius
    tripod = VGroup(
        Line(base_start, base_start + radial_dir * 0.08, color=GRAY, stroke_width=2),
        Line(
            base_start + LEFT * 0.03,
            base_start + radial_dir * 0.06,
            color=GRAY,
            stroke_width=1.5,
        ),
        Line(
            base_start + RIGHT * 0.03,
            base_start + radial_dir * 0.06,
            color=GRAY,
            stroke_width=1.5,
        ),
    )

    # Telescope tube (angled to point at stars)
    tube_start = base_start + radial_dir * 0.08

    # Angle the telescope (45 degrees from radial)
    angle = PI / 4
    tube_dir = np.array(
        [
            radial_dir[0] * np.cos(angle) - radial_dir[1] * np.sin(angle),
            radial_dir[0] * np.sin(angle) + radial_dir[1] * np.cos(angle),
            0,
        ]
    )

    tube = Rectangle(
        width=0.12,
        height=0.03,
        color=WHITE,
        fill_color=DARK_GRAY,
        fill_opacity=1,
        stroke_width=1,
    )
    tube.move_to(tube_start + tube_dir * 0.06)
    tube.rotate(angle + np.arctan2(radial_dir[1], radial_dir[0]))

    # Lens (front of telescope)
    lens_pos = tube_start + tube_dir * 0.12
    lens = Dot(lens_pos, radius=0.02, color=LIGHT_GRAY)

    # Eyepiece (back of telescope)
    eyepiece_pos = tube_start
    eyepiece = Dot(eyepiece_pos, radius=0.015, color=GRAY)

    telescope = VGroup(tripod, tube, lens, eyepiece)

    return telescope


class MultipleOrbits(MovingCameraScene):
    # Solar system style with multiple orbiting bodies

    def construct(self):
        # Central star
        star = Dot(ORIGIN, radius=0.35, color=YELLOW)
        star_glow = Dot(ORIGIN, radius=0.5, color=ORANGE, fill_opacity=0.3)

        # Planet data: (radius, orbit_radius, color, speed)
        planets_data = [
            (0.08, 1.2, RED, 2.5),  # Mercury-like
            (0.10, 1.8, ORANGE, 1.8),  # Venus-like
            (0.12, 2.5, BLUE, 1.2),  # Earth-like
            (0.09, 3.2, RED_E, 0.8),  # Mars-like
        ]

        planets = []
        orbits = []

        for radius, orbit_r, color, speed in planets_data:
            # Create orbit path
            orbit = Circle(radius=orbit_r, color=WHITE, stroke_opacity=0.15)
            orbits.append(orbit)

            # Create planet
            planet = Dot(radius=radius, color=color)
            planet.move_to(RIGHT * orbit_r)
            planet.speed = speed
            planets.append(planet)

        # Add to scene
        self.play(
            FadeIn(star_glow),
            FadeIn(star),
            *[Create(o) for o in orbits],
            *[FadeIn(p) for p in planets],
            run_time=2,
        )

        # Add orbit updaters
        for planet in planets:
            planet.add_updater(lambda m, dt: m.rotate(dt * m.speed, about_point=ORIGIN))

        self.wait(6)

        # Clear the updaters
        for planet in planets:
            planet.clear_updaters()

        mercury = planets[0]

        position_vector = Arrow(
            start=ORIGIN,
            end=mercury.get_center(),
            color=YELLOW,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )

        # VELOCITY VECTOR: tangent to orbit (perpendicular to position)
        # For circular orbit, velocity is perpendicular to radius
        planet_pos = mercury.get_center()

        # Tangent direction: rotate position 90 degrees (counterclockwise)
        tangent = np.array([-planet_pos[1], planet_pos[0], 0])
        tangent = tangent / np.linalg.norm(tangent)  # Normalize

        velocity_vector = Arrow(
            start=mercury.get_center(),
            end=mercury.get_center() + tangent * 1.0,  # Scale for visibility
            color=GREEN,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )

        # Animate the vectors appearing
        self.play(GrowArrow(position_vector), run_time=1)

        self.wait()

        self.play(GrowArrow(velocity_vector), run_time=1)

        self.wait()

        # Fade out the vectors before zooming
        self.play(
            FadeOut(position_vector),
            FadeOut(velocity_vector),
            run_time=0.5,
        )

        # ZOOM IN ON EARTH
        earth = planets[2]

        # Method 1: Move and scale the camera frame
        self.play(
            self.camera.frame.animate.set(width=1.5).move_to(earth),
            run_time=2,
        )

        # CREATE TELESCOPE on top of Earth
        earth_pos = earth.get_center()
        earth_radius = 0.12

        # Direction pointing "up" (away from sun/origin)
        radial_dir = earth_pos / np.linalg.norm(earth_pos)

        telescope = create_telescope(earth_pos, radial_dir, earth_radius)

        self.play(FadeIn(telescope), run_time=1)

        self.wait()
