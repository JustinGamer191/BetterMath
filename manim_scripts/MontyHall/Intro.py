from manim import *


# --- HELPER FUNCTION: CREATE THREE DOORS ---
# Standard setup for the Monty Hall Problem
def doors():
    door1 = Rectangle(width=1, height=2, color=RED).shift(1.5 * LEFT)
    door2 = Rectangle(width=1, height=2, color=RED)
    door3 = Rectangle(width=1, height=2, color=RED).shift(1.5 * RIGHT)
    return VGroup(door1, door2, door3)


# --- SCENE 1: INTRODUCTION TO THE MONTY HALL PROBLEM ---
# One of the most counterintuitive probability problems
# Named after game show host Monty Hall from "Let's Make a Deal"
class Intro(Scene):
    def construct(self):
        # --- SETUP: THREE DOORS ---
        door_group = doors()
        self.play(Create(door_group))
        self.wait(1)

        # Title
        text1 = MathTex(r"\text{Monty Hall Problem, Part 1}", color=GOLD).to_edge(UP)
        self.play(Write(text1))
        self.wait(1)

        # --- PROBLEM SETUP: 2 GOATS, 1 CAR ---
        # Behind two doors: goats (worthless prizes)
        # Behind one door: car (valuable prize)
        # You want the car!
        text2 = MathTex(
            r"\text{Assume behind two of the doors was a goat,}", color=WHITE
        ).scale(0.5)
        text2.next_to(text1, DOWN)
        self.play(Write(text2))

        # Show goats behind doors 1 and 3
        img1 = ImageMobject("goat.png").scale(0.05)
        img2 = ImageMobject("goat.png").scale(0.05)
        img1.shift(1.5 * LEFT)
        img2.shift(1.5 * RIGHT)
        self.play(FadeIn(img1, img2))
        self.wait(1)

        # Show car behind door 2 (middle door)
        text3 = MathTex(
            r"\text{and behind one of the doors was a car.}", color=WHITE
        ).scale(0.5)
        text3.next_to(text2, DOWN)
        self.play(Write(text3))
        img3 = ImageMobject("car.png").scale(0.2)
        self.play(FadeIn(img3))
        self.wait(1)

        # KEY POINT: You don't know which door has the car!
        # This creates the uncertainty that makes the problem interesting
        text4 = MathTex(
            r"\text{But you don't know which door has the car!}", color=RED
        ).scale(0.5)
        text4.next_to(text3, DOWN)
        self.play(Write(text4))

        # --- SHUFFLE ANIMATION ---
        # Visually demonstrates the uncertainty
        # The car could be behind ANY door with equal probability
        self.play(FadeOut(img1, img2, img3))

        # Shuffle sequence (permutations of door positions)
        # 123 → 231 → 213 → 132 → 123
        self.play(
            door_group[0].animate.shift(3 * RIGHT),
            door_group[1].animate.shift(1.5 * LEFT),
            door_group[2].animate.shift(1.5 * LEFT),
        )  # 231
        self.play(
            door_group[0].animate.shift(1.5 * LEFT),
            door_group[2].animate.shift(1.5 * RIGHT),
        )  # 213
        self.play(
            door_group[0].animate.shift(1.5 * LEFT),
            door_group[1].animate.shift(3 * RIGHT),
            door_group[2].animate.shift(1.5 * LEFT),
        )  # 132
        self.play(
            door_group[1].animate.shift(1.5 * LEFT),
            door_group[2].animate.shift(1.5 * RIGHT),
        )  # 123

        self.wait(1)

        # --- STEP 1: MAKE YOUR INITIAL CHOICE ---
        self.play(FadeOut(text2, text3, text4))
        t1 = MathTex(r"\text{You pick a door, say door 1.}", color=WHITE).scale(0.5)
        t1.next_to(text1, DOWN)

        # INITIAL PROBABILITY: P(car behind door 1) = 1/3
        # This is a fundamental probability: 1 car among 3 doors
        t2 = MathTex(
            r"\text{The probability of the car being behind door 1 is } \frac{1}{3}.",
            color=WHITE,
        ).scale(0.5)
        t2.next_to(t1, DOWN)

        self.play(Write(t1))
        self.play(
            door_group[0].animate.set_fill(GREEN, opacity=0.5)
        )  # Highlight chosen door
        self.play(Write(t2))
        self.wait(1)

        # --- STEP 2: MONTY REVEALS A GOAT ---
        # CRITICAL: Monty KNOWS where the car is and ALWAYS reveals a goat
        # He cannot reveal the car
        # He cannot reveal your chosen door
        # This is NOT a random reveal - it's strategic information!
        self.play(FadeOut(t1, t2))
        t3 = MathTex(
            r"\text{Now let's say, Monty, who knows where the car is,}", color=WHITE
        ).scale(0.5)
        t35 = MathTex(r"\text{opens door 3, revealing a goat.}", color=WHITE).scale(0.5)
        t3.next_to(text1, DOWN)
        self.play(Write(t3))
        t35.next_to(t3, DOWN)
        self.play(Write(t35))

        # Reveal goat behind door 3
        self.play(FadeIn(img2))
        self.wait(1)
        self.play(FadeOut(door_group[2], img2))

        # --- STEP 3: THE CHOICE - STAY OR SWITCH? ---
        # Monty asks: Do you want to switch to door 2?
        # Intuition says: Doesn't matter, 50/50 chance now
        # REALITY: You should ALWAYS switch! (Wins 2/3 of the time)
        t4 = MathTex(r"\text{Now suppose Monty offers you an opportunity}").scale(0.5)
        t45 = MathTex(r"\text{to swap doors. Do you take it?}").scale(0.5)
        t5 = MathTex(r"\text{YESSSSSSSSSSSSSS! Always.}").scale(0.5)

        self.play(FadeOut(t3, t35))
        t4.next_to(text1, DOWN)
        t45.next_to(t4, DOWN)
        t5.next_to(t45, DOWN)
        self.play(Write(t4))
        self.play(Write(t45))
        self.play(FadeIn(t5))

        # Switch to door 2 and reveal the car!
        self.play(
            door_group[0].animate.set_fill(BLACK, opacity=0.5),  # Deselect door 1
            door_group[1].animate.set_fill(GREEN, opacity=0.5),  # Select door 2
        )
        self.play(
            FadeIn(img3), FadeIn(img1)
        )  # Show car behind door 2, goat behind door 1
        self.wait(2)

        # Clean up for next scene
        self.play(FadeOut(t5, img3, img1, t4, t45, text1, door_group[0], door_group[1]))
        self.wait(1)


# --- SCENE 2: EXPLANATION WITH 100 DOORS ---
# Makes the counterintuitive result more obvious
# This is a pedagogical technique: extend to extreme case
class Explanation(Scene):
    def construct(self):
        # --- WHY SHOULD YOU SWITCH? ---
        t1 = MathTex(r"\text{But why?}", color=GOLD)
        t2 = MathTex(r"\text{To understand why swapping is the better option,}").scale(
            0.5
        )
        t3 = MathTex(r"\text{let's extend this scenario to 100 doors.}").scale(0.5)

        self.play(Write(t1))
        self.play(t1.animate.shift(3 * UP))
        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        self.play(Write(t2))
        self.play(Write(t3))

        # --- SETUP: 100 DOORS ---
        # Same problem, but with 100 doors instead of 3
        # Initial probability: P(car behind door 1) = 1/100
        # P(car behind doors 2-100) = 99/100

        # Visual representation (show doors 1, 2, ..., 99, 100)
        door1 = Rectangle(width=0.75, height=1.5, color=RED).shift(2 * LEFT)
        label1 = MathTex(r"1").shift(2 * LEFT).scale(0.75)
        door2 = Rectangle(width=0.75, height=1.5, color=RED).shift(1 * LEFT)
        label2 = MathTex(r"2").shift(1 * LEFT).scale(0.75)
        dots = MathTex(r"\cdots")  # Represents doors 3-98
        door99 = Rectangle(width=0.75, height=1.5, color=RED).shift(1 * RIGHT)
        label99 = MathTex(r"99").shift(1 * RIGHT).scale(0.75)
        door100 = Rectangle(width=0.75, height=1.5, color=RED).shift(2 * RIGHT)
        label100 = MathTex(r"100").shift(2 * RIGHT).scale(0.75)

        self.play(Create(door1), Create(label1))
        self.play(Create(door2), Create(label2))
        self.play(Create(dots))
        self.play(Create(door99), Create(label99))
        self.play(Create(door100), Create(label100))

        # --- THE SCENARIO WITH 100 DOORS ---
        t4 = MathTex(r"\text{Now let's assume you chose door 1 again.}").scale(0.5)
        t5 = MathTex(r"\text{And Monty, who knows where the car is,}").scale(0.5)

        # KEY INSIGHT: Monty removes 98 goats, leaving only door 99
        # He MUST leave the car if it's in doors 2-100
        # This concentrates the 99/100 probability onto door 99!
        t6 = MathTex(r"\text{removes all doors 2-100 except door 99.}").scale(0.5)
        t4.next_to(t1, DOWN)
        t5.next_to(t4, DOWN)
        t6.next_to(t5, DOWN)

        self.play(FadeOut(t2, t3))
        self.play(Write(t4))

        # You pick door 1: P(car) = 1/100
        self.play(door1.animate.set_fill(GREEN, opacity=0.5))

        self.play(Write(t5))
        self.play(Write(t6))

        # Monty eliminates doors 2-98 and 100 (all goats)
        # Only doors 1 (your choice) and 99 remain
        self.play(FadeOut(door2, door100, dots, label2, label100))

        # --- THE OBVIOUS CHOICE ---
        # Now it's clear: Would you rather stick with 1/100 chance
        # or switch to 99/100 chance?
        t7 = MathTex(r"\text{Now when Monty presents you with the opportunity}").scale(
            0.5
        )
        t7.next_to(t1, DOWN)
        t8 = MathTex(r"\text{to switch, you would obviously do so!}").scale(0.5)
        t8.next_to(t7, DOWN)

        # Show the truth: goat behind door 1, car behind door 99
        img1 = ImageMobject("goat.png").scale(0.05).move_to([-2, 0, 0])
        img3 = ImageMobject("car.png").scale(0.2).move_to([1, 0, 0])

        self.play(FadeOut(t4, t5, t6))
        self.play(Write(t7))
        self.play(Write(t8))
        self.play(FadeOut(door1, label1, door99, label99), FadeIn(img1, img3))

        self.wait(2)
