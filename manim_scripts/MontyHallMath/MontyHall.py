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
        img1 = ImageMobject("goat.png").scale(0.05)
        img2 = ImageMobject("goat.png").scale(0.05)
        img3 = ImageMobject("car.png").scale(0.2)
        img1.shift(1.5*LEFT)
        img2.shift(1.5*RIGHT)
        self.play(FadeIn(img1, img2, img3))
        
        t1 = MathTex(r"\text{Monty Hall Problem, Part 2}")
        t2 = MathTex(r"\text{The mathematical approach to understanding}").scale(0.5)
        t3 = MathTex(r"\text{why swapping doors is the best option.}").scale(0.5)
        t1.move_to([0,3,0])
        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        
        self.wait(2)
        
        self.play(FadeOut(t1,t2,t3,img1,img2,img3))
        self.wait(2)
        
        t4 = MathTex(r"\text{Assume door 1 is chosen.}").scale(0.5)
        t5 = MathTex(r"\text{The probability of the car being behind the door is }", r"\frac{1}{3},").scale(0.5)
        t5[1].color = GOLD
        t6 = MathTex(r"\text{and the probability of it not being behind the door is }", r"\frac{2}{3}.").scale(0.5)
        t6[1].color = GOLD
        
        t4.move_to([0,3,0])
        t5.next_to(t4, DOWN)
        t6.next_to(t5, DOWN)
        
        self.play(Write(t4))
        self.play(door_group[0].animate.set_fill(GREEN, opacity=0.5))
        
        self.play(Write(t5))
        self.play(Write(t6))
        
        self.wait(1)
        
        t7 = MathTex(r"\text{Then Monty removes a door, revealing a Goat.}").scale(0.5)
        t7.next_to(door_group[1], DOWN)
        t8 = MathTex(r"\text{This does not affect the original probability of the car being behind your door.}").scale(0.5)
        t8.next_to(t7, DOWN)
        t9 = MathTex(r"\frac{1}{3}")
        t9.shift(1.5*LEFT)
        t10 = MathTex(r"\text{This means the probability that the car isn't behind your door is still }", r"\frac{2}{3}.").scale(0.5)
        t10.next_to(t8, DOWN)
        t10[1].color = GOLD
        t11 = MathTex(r'\frac{2}{3}')
        
        
        self.play(Write(t7))
        self.play(FadeIn(img2))
        self.play(FadeOut(img2, door_group[2]))
        self.play(Write(t8))
        self.play(Write(t9))
        
        self.wait(1)
        
        self.play(Write(t10))
        self.play(Write(t11))
        
        self.wait(2)