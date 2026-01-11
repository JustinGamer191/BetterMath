from manim import *
import numpy as np


class Introduction(Scene):
    def construct(self):
        # Create celestial bodies
        intro_sun = Circle(radius=0.4, color=YELLOW, fill_opacity=1)
        intro_sun_glow = Circle(radius=0.6, color=YELLOW, fill_opacity=0.3)
        intro_sun_group = VGroup(intro_sun_glow, intro_sun)

        intro_earth = Circle(
            radius=0.12, color=BLUE, fill_opacity=1, stroke_width=1, stroke_color=BLUE_E
        )
        intro_earth.shift(RIGHT * 2.5)

        # Show the two bodies
        self.play(FadeIn(intro_sun_group), FadeIn(intro_earth), run_time=1)
        self.wait(0.5)

        # Show Earth's orbit
        intro_orbit = Circle(
            radius=2.5, color=BLUE_D, stroke_opacity=0.4, stroke_width=2
        )
        self.play(Create(intro_orbit), run_time=1.5)
        self.wait(0.3)

        # Add test particle
        test_particle = Dot(color=RED, radius=0.08)
        test_particle.move_to(RIGHT * 3.2 + UP * 0.8)

        self.play(FadeIn(test_particle), run_time=0.5)
        self.wait(0.5)

        # Create force arrows
        sun_force_arrow = Arrow(
            test_particle.get_center(),
            intro_sun.get_center(),
            color=YELLOW,
            buff=0.3,
            max_tip_length_to_length_ratio=0.15,
        )
        earth_force_arrow = Arrow(
            test_particle.get_center(),
            intro_earth.get_center(),
            color=BLUE,
            buff=0.3,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(GrowArrow(sun_force_arrow), GrowArrow(earth_force_arrow), run_time=1)
        self.wait(1)

        # Physics simulation parameters
        dt = 0.02
        total_time = 5.0
        num_steps = int(total_time / dt)

        # Gravitational constants (adjusted for stability)
        G_sun = 4.0
        G_earth = 1.5

        # Initial conditions
        particle_pos = test_particle.get_center().copy()
        particle_vel = np.array([0.3, -0.5, 0])  # Small initial velocity

        earth_angle = np.arctan2(
            intro_earth.get_center()[1], intro_earth.get_center()[0]
        )
        earth_angular_velocity = 0.4

        # Store trajectory
        particle_trajectory = [particle_pos.copy()]
        earth_positions = [intro_earth.get_center().copy()]

        # Simulate the physics
        for step in range(num_steps):
            # Update Earth position
            earth_angle += earth_angular_velocity * dt
            earth_pos = 2.5 * np.array([np.cos(earth_angle), np.sin(earth_angle), 0])
            earth_positions.append(earth_pos.copy())

            # Calculate gravitational forces
            sun_pos = intro_sun.get_center()

            # Vector from particle to sun
            r_sun = sun_pos - particle_pos
            dist_sun = np.linalg.norm(r_sun)

            # Vector from particle to earth
            r_earth = earth_pos - particle_pos
            dist_earth = np.linalg.norm(r_earth)

            # Gravitational acceleration (a = GM/r^2 * direction)
            if dist_sun > 0.1:
                acc_sun = G_sun * r_sun / (dist_sun**3)
            else:
                acc_sun = np.array([0, 0, 0])

            if dist_earth > 0.1:
                acc_earth = G_earth * r_earth / (dist_earth**3)
            else:
                acc_earth = np.array([0, 0, 0])

            # Total acceleration
            total_acc = acc_sun + acc_earth

            # Update velocity and position (Verlet integration for better stability)
            particle_vel += total_acc * dt
            particle_pos += particle_vel * dt

            # Apply damping to prevent escape
            particle_vel *= 0.995

            # Store position
            if step % 3 == 0:
                particle_trajectory.append(particle_pos.copy())

        # Create traced path
        trace_path = TracedPath(
            test_particle.get_center,
            stroke_color=RED,
            stroke_opacity=0.5,
            stroke_width=2,
        )
        self.add(trace_path)

        # Set up Earth updater
        earth_angle_current = np.arctan2(
            intro_earth.get_center()[1], intro_earth.get_center()[0]
        )

        def earth_updater(mob, dt):
            nonlocal earth_angle_current
            earth_angle_current += earth_angular_velocity * dt
            new_pos = 2.5 * np.array(
                [np.cos(earth_angle_current), np.sin(earth_angle_current), 0]
            )
            mob.move_to(new_pos)

        intro_earth.add_updater(earth_updater)

        # Animate particle along trajectory with updating arrows
        for i in range(len(particle_trajectory) - 1):
            next_pos = particle_trajectory[i + 1]

            # Create new arrows pointing from particle to bodies
            new_sun_arrow = Arrow(
                next_pos,
                intro_sun.get_center(),
                color=YELLOW,
                buff=0.3,
                max_tip_length_to_length_ratio=0.15,
            )
            new_earth_arrow = Arrow(
                next_pos,
                intro_earth.get_center(),
                color=BLUE,
                buff=0.3,
                max_tip_length_to_length_ratio=0.15,
            )

            self.play(
                test_particle.animate.move_to(next_pos),
                Transform(sun_force_arrow, new_sun_arrow),
                Transform(earth_force_arrow, new_earth_arrow),
                run_time=0.03,
                rate_func=linear,
            )

        intro_earth.remove_updater(earth_updater)

        # Fade out all elements
        self.play(
            FadeOut(test_particle),
            FadeOut(trace_path),
            FadeOut(sun_force_arrow),
            FadeOut(earth_force_arrow),
            FadeOut(intro_sun_group),
            FadeOut(intro_earth),
            FadeOut(intro_orbit),
            run_time=1,
        )
        self.wait(0.5)


# Telescope helper function
def makeTelescope():
    # Create detailed telescope at L4
    telescope = VGroup()

    # Main tube (cylindrical body)
    tube = Rectangle(width=0.6, height=0.2, color=GREY, fill_opacity=1, stroke_width=2)
    tube.set_fill(DARK_GRAY)

    # Front aperture
    aperture = Circle(
        radius=0.12,
        color=DARK_BLUE,
        fill_opacity=1,
        stroke_width=2,
        stroke_color=BLUE_E,
    )
    aperture.move_to(tube.get_right() + LEFT * 0.05)

    # Lens detail
    lens = Circle(radius=0.08, color=BLUE_D, fill_opacity=0.5, stroke_width=1)
    lens.move_to(aperture.get_center())

    # Back end
    back = Rectangle(
        width=0.15, height=0.22, color=GREY_B, fill_opacity=1, stroke_width=2
    )
    back.move_to(tube.get_left() + RIGHT * 0.075)

    # Solar panels (two)
    panel1 = Rectangle(
        width=0.15,
        height=0.5,
        color=BLUE_E,
        fill_opacity=1,
        stroke_width=2,
        stroke_color=BLUE,
    )
    panel1.set_fill(DARK_BLUE)
    panel1.move_to(tube.get_center() + UP * 0.35)

    panel2 = Rectangle(
        width=0.15,
        height=0.5,
        color=BLUE_E,
        fill_opacity=1,
        stroke_width=2,
        stroke_color=BLUE,
    )
    panel2.set_fill(DARK_BLUE)
    panel2.move_to(tube.get_center() + DOWN * 0.35)

    # Antenna
    antenna_base = Circle(radius=0.04, color=GREY, fill_opacity=1)
    antenna_base.move_to(back.get_top() + UP * 0.02)
    antenna_rod = Line(antenna_base.get_center(), antenna_base.get_center() + UP * 0.15)
    antenna_rod.set_stroke(GREY, width=3)
    antenna_dish = Arc(
        radius=0.08, angle=PI, color=GREY_B, fill_opacity=1, stroke_width=2
    )
    antenna_dish.rotate(-PI / 2)
    antenna_dish.move_to(antenna_rod.get_end() + RIGHT * 0.04)

    # Small thruster
    thruster = Rectangle(width=0.08, height=0.06, color=GREY_BROWN, fill_opacity=1)
    thruster.move_to(back.get_bottom() + DOWN * 0.03)

    # Secondary mirror (inside tube)
    secondary = Circle(radius=0.04, color=LIGHT_GRAY, fill_opacity=1, stroke_width=1)
    secondary.move_to(tube.get_center() + RIGHT * 0.1)

    telescope.add(
        tube,
        back,
        aperture,
        lens,
        secondary,
        panel1,
        panel2,
        antenna_base,
        antenna_rod,
        antenna_dish,
        thruster,
    )

    return telescope


class LagrangePoints(MovingCameraScene):
    def construct(self):
        # Scale factor to fit in view
        scale = 3.5

        # Positions - place Sun at origin, Earth on positive x-axis
        sun_pos = np.array([0, 0, 0])
        earth_pos = np.array([scale, 0, 0])

        # Distance between Sun and Earth
        R = scale

        # Lagrange point positions (properly calculated for Sun-Earth system)
        # L1: between Sun and Earth (about 1.5 million km from Earth, ~1% of Sun-Earth distance)
        L1 = np.array([R * 0.99, 0, 0])

        # L2: beyond Earth on the far side (about 1.5 million km past Earth)
        L2 = np.array([R * 1.01, 0, 0])

        # L3: opposite side of Sun from Earth (essentially at Earth's orbital distance on opposite side)
        L3 = np.array([-R, 0, 0])

        # L4 and L5: form equilateral triangles with Sun and Earth
        # These are 60 degrees ahead (L4) and behind (L5) Earth in its orbit
        L4 = np.array([R * np.cos(np.pi / 3), R * np.sin(np.pi / 3), 0])
        L5 = np.array([R * np.cos(-np.pi / 3), R * np.sin(-np.pi / 3), 0])

        # Create Sun
        sun = Circle(radius=0.5, color=YELLOW, fill_opacity=1, stroke_width=0)
        sun.set_fill(YELLOW)
        sun_glow = Circle(radius=0.7, color=YELLOW, fill_opacity=0.3, stroke_width=0)
        sun_group = VGroup(sun_glow, sun).move_to(sun_pos)

        # Create Earth
        earth = Circle(
            radius=0.15, color=BLUE, fill_opacity=1, stroke_width=1, stroke_color=BLUE_E
        )
        earth.move_to(earth_pos)

        # Create Lagrange points
        L1_dot = Dot(L1, color=RED, radius=0.08)
        L2_dot = Dot(L2, color=PURPLE, radius=0.08)
        L3_dot = Dot(L3, color=ORANGE, radius=0.08)
        L4_dot = Dot(L4, color=GREEN, radius=0.08)
        L5_dot = Dot(L5, color=TEAL, radius=0.08)

        # Labels for Lagrange points
        L1_label = Text("L1", font_size=24, color=RED).next_to(L1_dot, LEFT, buff=0.15)
        L2_label = Text("L2", font_size=24, color=PURPLE).next_to(
            L2_dot, RIGHT, buff=0.15
        )
        L3_label = Text("L3", font_size=24, color=ORANGE).next_to(
            L3_dot, DOWN, buff=0.15
        )
        L4_label = Text("L4", font_size=24, color=GREEN).next_to(L4_dot, UP, buff=0.15)
        L5_label = Text("L5", font_size=24, color=TEAL).next_to(L5_dot, DOWN, buff=0.15)

        telescope = makeTelescope()
        telescope.scale(0.7)
        telescope.move_to(L4)

        # Create Earth's orbit
        earth_orbit = Circle(radius=R, color=BLUE_D, stroke_opacity=0.3, stroke_width=2)
        earth_orbit.move_to(sun_pos)

        # Triangular configuration lines (equilateral triangles)
        triangle = Polygon(
            sun_pos,
            earth_pos,
            L4,
            color=GREEN_D,
            stroke_opacity=0.4,
            stroke_width=2,
            fill_opacity=0,
        )
        triangle2 = Polygon(
            sun_pos,
            earth_pos,
            L5,
            color=TEAL_D,
            stroke_opacity=0.4,
            stroke_width=2,
            fill_opacity=0,
        )

        # Animation sequence
        self.play(FadeIn(sun_group), run_time=1)
        self.wait(0.3)

        self.play(Create(earth_orbit), run_time=2)
        self.wait(0.3)

        self.play(FadeIn(earth), run_time=0.8)
        self.wait(0.5)

        self.play(Create(triangle), Create(triangle2), run_time=2)
        self.wait(0.5)

        self.play(FadeIn(L1_dot), FadeIn(L1_label), run_time=0.4)
        self.play(FadeIn(L2_dot), FadeIn(L2_label), run_time=0.4)
        self.play(FadeIn(L3_dot), FadeIn(L3_label), run_time=0.4)
        self.play(FadeIn(L4_dot), FadeIn(L4_label), run_time=0.4)
        self.play(FadeIn(L5_dot), FadeIn(L5_label), run_time=0.4)

        self.wait(0.5)

        # Zoom out to show full system
        self.play(self.camera.frame.animate.scale(1.3), run_time=2)
        self.wait(0.5)

        # Zoom into L4
        self.play(self.camera.frame.animate.move_to(L4).scale(0.3), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(L4_dot), FadeOut(L4_label), run_time=0.3)
        self.play(FadeIn(telescope), run_time=1.5)

        self.wait(1)

        # Demonstrate L4 stability: push telescope away and watch it oscillate back
        # Save original position
        original_pos = telescope.get_center().copy()

        # Create a motion trail
        trail = TracedPath(
            telescope.get_center, stroke_color=GREEN, stroke_width=2, stroke_opacity=0.5
        )
        self.add(trail)

        # Push telescope to the right
        self.play(telescope.animate.shift(RIGHT * 0.8), run_time=1, rate_func=smooth)
        self.wait(0.3)

        # Oscillate back past equilibrium (damped harmonic motion)
        self.play(
            telescope.animate.move_to(original_pos + LEFT * 0.5),
            run_time=1.2,
            rate_func=smooth,
        )

        # Second oscillation (smaller amplitude)
        self.play(
            telescope.animate.move_to(original_pos + RIGHT * 0.3),
            run_time=1,
            rate_func=smooth,
        )

        # Third oscillation (even smaller)
        self.play(
            telescope.animate.move_to(original_pos + LEFT * 0.15),
            run_time=0.8,
            rate_func=smooth,
        )

        # Settle back to equilibrium
        self.play(
            telescope.animate.move_to(original_pos), run_time=0.8, rate_func=smooth
        )

        self.wait(1)

        # Now demonstrate vertical displacement
        self.play(FadeOut(trail), run_time=0.3)
        trail2 = TracedPath(
            telescope.get_center, stroke_color=GREEN, stroke_width=2, stroke_opacity=0.5
        )
        self.add(trail2)

        # Push upward
        self.play(telescope.animate.shift(UP * 0.6), run_time=1, rate_func=smooth)
        self.wait(0.3)

        # Oscillate back (vertical damped oscillation)
        self.play(
            telescope.animate.move_to(original_pos + DOWN * 0.4),
            run_time=1.2,
            rate_func=smooth,
        )

        self.play(
            telescope.animate.move_to(original_pos + UP * 0.2),
            run_time=1,
            rate_func=smooth,
        )

        # Settle
        self.play(
            telescope.animate.move_to(original_pos), run_time=0.8, rate_func=smooth
        )

        self.wait(1)

        # Zoom back out
        self.play(
            FadeOut(trail2),
            self.camera.frame.animate.move_to(ORIGIN).scale(3),
            run_time=2.5,
        )

        self.wait(2)
