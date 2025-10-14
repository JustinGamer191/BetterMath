from manim import*
import random
class Intro(Scene):
    def construct(self):
        #Rock
        rock_shape = Polygon(
            [-2, 0, 0],
            [-1.8, 1.2, 0],
            [-1, 1.8, 0],
            [-0.5, 2.2, 0],
            [0.5, 2, 0],
            [1.3, 1.5, 0],
            [2, 0.8, 0],
            [2.2, 0, 0],
            [1, -0.8, 0],
            [0, -1.5, 0],
            [-1, -1, 0],
            color=WHITE,
            fill_color=GRAY,
            fill_opacity=1
        )
        
        
        #Paper
        paper_shape = Rectangle(
            width=5, height=3,  # Size of the paper
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1
        )
        lines = VGroup()  # Group to hold all lines
        line_spacing = 0.3  # Spacing between lines
        for y in range(-4, 5):  # Adjust range to fit the paper size
            line = Line(
                start=[-2.5, y * line_spacing, 0],  # Start of line
                end=[2.5, y * line_spacing, 0],    # End of line
                color=BLUE,
                stroke_width=0.8  # Thin lines
            )
            lines.add(line)
        paper = VGroup(paper_shape, lines)
        

        #Scissors
        blade_color = GRAY
        handle_color = RED

        left_blade = Polygon(
            [0, 0, 0], [1, 3, 0], [1, -2, 0],
            color=blade_color, fill_opacity=1
        ).shift(LEFT * 1)

        right_blade = Polygon(
            [0, 0, 0], [-1, 3, 0], [-1, -2, 0],
            color=blade_color, fill_opacity=1
        ).shift(RIGHT * 1)

        hinge = Dot(radius=0.1, color=YELLOW).shift(DOWN*1)

        right_handle = Circle(radius=0.5, color=handle_color, fill_opacity=1)
        right_handle.move_to([0, -2, 0])

        left_handle = Circle(radius=0.5, color=handle_color, fill_opacity=1)
        left_handle.move_to([0,-2,0])

        scissors = VGroup(left_blade, right_blade, hinge, left_handle, right_handle)

        rock_shape.scale(0.75)
        paper.scale(0.75)
        scissors.scale(0.75)

        rock_shape.move_to([-4.5,-1.5,0])
        paper.move_to([0,2,0])
        scissors.move_to([4.5,-1,0])


        ##Mystery
        triangle = Polygon(
            [-4, -2, 0],  # Bottom-left vertex
            [4, -2, 0],   # Bottom-right vertex
            [0, 4, 0],    # Top vertex
            color=BLUE
        ).shift(2.5*DOWN)

        triangle.scale(0.5)
        
        question_mark = Text("?", font_size=80, color=BLUE)
        question_mark.move_to(triangle.get_center())
        
        self.play(Write(rock_shape))
        self.play(Write(paper))
        self.play(Write(scissors))

        for _ in range(1):
            self.play(
            left_blade.animate.rotate(PI / 6, about_point=hinge.get_center()),
            right_blade.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            left_handle.animate.rotate(PI / 6, about_point=hinge.get_center()),
            right_handle.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            rock_shape.animate.scale(0.8),
            paper.animate.scale(1.25),
            run_time=1
            )

            self.play(
            left_blade.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            right_blade.animate.rotate(PI / 6, about_point=hinge.get_center()),
            left_handle.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            right_handle.animate.rotate(PI / 6, about_point=hinge.get_center()),
            rock_shape.animate.scale(1.25),
            paper.animate.scale(0.8),
            run_time=1
            )

            self.play(
            left_blade.animate.rotate(PI / 6, about_point=hinge.get_center()),
            right_blade.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            left_handle.animate.rotate(PI / 6, about_point=hinge.get_center()),
            right_handle.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            rock_shape.animate.scale(1.25),
            paper.animate.scale(0.8),
            run_time=1
            )

            self.play(
            left_blade.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            right_blade.animate.rotate(PI / 6, about_point=hinge.get_center()),
            left_handle.animate.rotate(-PI / 6, about_point=hinge.get_center()),
            right_handle.animate.rotate(PI / 6, about_point=hinge.get_center()),
            rock_shape.animate.scale(0.8),
            paper.animate.scale(1.25),
            run_time=1
            )

        self.play(FadeIn(triangle), FadeIn(question_mark), run_time = 4)
        self.play(FadeOut(rock_shape, paper, scissors))
        
        m1 = Text("Why is four-option Rock Paper\brScissors mathematically unfair?")
        m1.move_to([0,2,0])
        m1.color = BLUE
        
        self.play(FadeIn(m1))
        
        self.wait(2)