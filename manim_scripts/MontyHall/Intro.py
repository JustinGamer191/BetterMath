from manim import *

def doors():
    door1 = Rectangle(width=1, height=2, color=RED).shift(1.5 * LEFT)
    door2 = Rectangle(width=1, height=2, color=RED)
    door3 = Rectangle(width=1, height=2, color=RED).shift(1.5 * RIGHT)
    return VGroup(door1, door2, door3)

class Intro(Scene):
    def construct(self):
        door_group = doors()
        self.play(Create(door_group))
        self.wait(1)
        
        text1 = MathTex(r"\text{Monty Hall Problem, Part 1}", color = GOLD).to_edge(UP)
        self.play(Write(text1))
        self.wait(1)

        text2 = MathTex(r"\text{Assume behind two of the doors was a goat,}", color = WHITE).scale(0.5)
        text2.next_to(text1, DOWN)
        self.play(Write(text2))
        img1 = ImageMobject("goat.png").scale(0.05)
        img2 = ImageMobject("goat.png").scale(0.05)
        img1.shift(1.5*LEFT)
        img2.shift(1.5*RIGHT)
        self.play(FadeIn(img1, img2))
        self.wait(1)

        text3 = MathTex(r"\text{and behind one of the doors was a car.}", color = WHITE).scale(0.5)
        text3.next_to(text2, DOWN)
        self.play(Write(text3))
        img3 = ImageMobject("car.png").scale(0.2)
        self.play(FadeIn(img3))
        self.wait(1)
        
        text4 = MathTex(r"\text{But you don't know which door has the car!}", color = RED).scale(0.5)
        text4.next_to(text3, DOWN)
        self.play(Write(text4))
        
        self.play(FadeOut(img1, img2, img3))
        # 123
        self.play(door_group[0].animate.shift(3*RIGHT), door_group[1].animate.shift(1.5*LEFT), door_group[2].animate.shift(1.5*LEFT))
        # 231
        self.play(door_group[0].animate.shift(1.5*LEFT), door_group[2].animate.shift(1.5*RIGHT))
        # 213
        self.play(door_group[0].animate.shift(1.5*LEFT), door_group[1].animate.shift(3*RIGHT), door_group[2].animate.shift(1.5*LEFT))
        # 132
        self.play(door_group[1].animate.shift(1.5*LEFT), door_group[2].animate.shift(1.5*RIGHT))
        # 123
        
        self.wait(1)
        self.play(FadeOut(text2, text3, text4))
        t1 = MathTex(r"\text{You pick a door, say door 1.}", color = WHITE).scale(0.5)
        t1.next_to(text1, DOWN)
        t2 = MathTex(r"\text{The probability of the car being behind door 1 is } \frac{1}{3}.", color = WHITE).scale(0.5)
        t2.next_to(t1, DOWN)
        self.play(Write(t1))
        self.play(door_group[0].animate.set_fill(GREEN, opacity=0.5))
        self.play(Write(t2))
        self.wait(1)
        self.play(FadeOut(t1, t2))
        t3 = MathTex(r"\text{Now let's say, Monty, who knows where the car is,}", color = WHITE).scale(0.5)
        t35 = MathTex(r"\text{opens door 3, revealing a goat.}", color = WHITE).scale(0.5)
        t3.next_to(text1, DOWN)
        self.play(Write(t3))
        t35.next_to(t3, DOWN)
        self.play(Write(t35))
        self.play(FadeIn(img2))
        self.wait(1)
        self.play(FadeOut(door_group[2], img2))
        t4 = MathTex(r"\text{Now suppose Monty offers you an opportunity}").scale(0.5)
        t45 = MathTex(r"\text{to swap doors. Do you take it?}").scale(0.5)
        t5 = MathTex(r"\text{YESSSSSSSSSSSSSS! Always.}").scale(0.5)
        self.play(FadeOut(t3,t35))
        t4.next_to(text1, DOWN)
        t45.next_to(t4, DOWN)
        t5.next_to(t45, DOWN)
        self.play(Write(t4))
        self.play(Write(t45))
        self.play(FadeIn(t5))
        self.play(door_group[0].animate.set_fill(BLACK, opacity=0.5), door_group[1].animate.set_fill(GREEN, opacity=0.5))
        self.play(FadeIn(img3), FadeIn(img1))
        self.wait(2)
        self.play(FadeOut(t5, img3, img1, t4, t45, text1, door_group[0], door_group[1]))
        self.wait(1)

class Explanation(Scene):
    def construct(self):
        t1 = MathTex(r"\text{But why?}", color = GOLD)
        t2 = MathTex(r"\text{To understand why swapping is the better option,}").scale(0.5)
        t3 = MathTex(r"\text{let's extend this scenario to 100 doors.}").scale(0.5)
        
        self.play(Write(t1))
        self.play(t1.animate.shift(3*UP))
        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        self.play(Write(t2))
        self.play(Write(t3))
        
        door1 = Rectangle(width=0.75, height=1.5, color=RED).shift(2 * LEFT)
        label1 = MathTex(r"1").shift(2 * LEFT).scale(0.75)
        door2 = Rectangle(width=0.75, height=1.5, color=RED).shift(1 * LEFT)
        label2 = MathTex(r"2").shift(1 * LEFT).scale(0.75)
        dots = MathTex(r"\cdots")
        door99 = Rectangle(width=0.75, height=1.5, color=RED).shift(1 * RIGHT)
        label99 = MathTex(r"99").shift(1 * RIGHT).scale(0.75)
        door100 = Rectangle(width=0.75, height=1.5, color=RED).shift(2 * RIGHT)
        label100 = MathTex(r"100").shift(2 * RIGHT).scale(0.75)
        
        self.play(Create(door1), Create(label1))
        self.play(Create(door2), Create(label2))
        self.play(Create(dots))
        self.play(Create(door99), Create(label99))
        self.play(Create(door100), Create(label100))
        
        t4 = MathTex(r"\text{Now let's assume you chose door 1 again.}").scale(0.5)
        t5 = MathTex(r"\text{And Monty, who knows where the car is,}").scale(0.5)
        t6 = MathTex(r"\text{removes all doors 2-100 except door 99.}").scale(0.5)
        t4.next_to(t1, DOWN)
        t5.next_to(t4, DOWN)
        t6.next_to(t5, DOWN)
        
        self.play(FadeOut(t2,t3))
        self.play(Write(t4))
        self.play(door1.animate.set_fill(GREEN, opacity=0.5))
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(FadeOut(door2, door100, dots, label2, label100))
        
        t7 = MathTex(r"\text{Now when Monty presents you with the opportunity}").scale(0.5)
        t7.next_to(t1, DOWN)
        t8 = MathTex(r"\text{to switch, you would obviously do so!}").scale(0.5)
        t8.next_to(t7, DOWN)
        img1 = ImageMobject("goat.png").scale(0.05).move_to([-2,0,0])
        img3 = ImageMobject("car.png").scale(0.2).move_to([1,0,0])
        self.play(FadeOut(t4,t5,t6))
        self.play(Write(t7))
        self.play(Write(t8))
        self.play(FadeOut(door1, label1, door99, label99), FadeIn(img1, img3))
        
        self.wait(2)
        