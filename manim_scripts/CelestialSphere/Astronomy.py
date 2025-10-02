from manim import *
import pandas as pd
from tqdm import tqdm

boundary = Circle(radius=2, color=GREEN)

equator = Circle(radius=2, color=WHITE)
equator.stretch(0.2, dim=1) 

cEquator = Circle(radius=2, color=WHITE)
cEquator.stretch(0.2, dim=0) 
cEquator.rotate(np.radians(90 + 23.4))

sun = Circle(radius = 0.1, color = YELLOW, fill_opacity = 1)
sun.move_to([0,-0.4,0])
        
class CelestialSphere(Scene):
    def construct(self):
        t1 = MathTex(r"\text{The Celestial Sphere}")
        t1.color = PURPLE
        t1.move_to([0,3,0])
        
        t2 = MathTex(r"\text{An imaginary sphere}")
        t3 = MathTex(r"\text{centered on Earth.}")
        
        t23 = VGroup(t2, t3)
        t23.arrange(DOWN).scale(0.5)
        t23.move_to([0,2.25,0])
        t23.color = PURPLE
        
        earthDiagram = VGroup(boundary, equator, cEquator)
        
        self.play(Write(t1))
        
        self.play(Create(boundary), Create(equator), Create(cEquator))
        self.wait(0.5)
        self.play(earthDiagram.animate.scale(10), run_time = 2.5)
        
        self.play(Write(t23))

        self.play(VGroup(t1, t23).animate.move_to([0,0,0]))
        
        self.wait(1)
        
        self.play(FadeOut(VGroup(t1, t23)))
        boundary.color = PURPLE
        equator.color = RED
        cEquator.color = BLUE
        
        self.play(earthDiagram.animate.scale(0.1), run_time = 2.5)
        
        self.wait(1)
        
class EquatorEcliptic(Scene):
    def construct(self):
        boundary.color = PURPLE
        equator.color = RED
        cEquator.color = BLUE
        self.add(VGroup(boundary, equator, cEquator))
        line1 = Line([2*np.cos(np.radians(23.4)), 2*np.sin(np.radians(23.4)), 0], [3*np.cos(np.radians(23.4)), 3*np.sin(np.radians(23.4)), 0], color = BLUE)
        t1 = MathTex(r"\text{Plane of the solar system}")
        t1.color = BLUE
        t1.scale(0.35)
        t1.move_to([3*np.cos(np.radians(23.4)), 3*np.sin(np.radians(23.4)), 0])
        t1.shift(0.25*UP, 0.25*RIGHT)
        
        line2 = Line([-2, 0, 0], [-2 - np.cos(np.radians(-23.4)), np.sin(np.radians(23.4)), 0], color = RED)
        t2 = MathTex(r"\text{Celestial Equator}")
        t3 = MathTex(r"\text{Equator of Earth extended to infinity.}")
        t23 = VGroup(t2, t3)
        t23.color = RED
        t23.arrange(DOWN)
        t23.scale(0.35)
        t23.move_to([-1*np.cos(np.radians(-23.4)) - 2, np.sin(np.radians(23.4)), 0])
        t23.shift(0.25*UP)
        bg23 = BackgroundRectangle(t23, fill_opacity=1, fill_color=BLACK)
        
        l3 = VGroup(MathTex(r"\text{Vernal Equinox}"), MathTex(r"\text{When the Celestial Equator intersects the Plane of the Solar System}"))
        l3.color = YELLOW
        l3.arrange(DOWN)
        l3.scale(0.35)
        l3.move_to(sun)
        l3.shift(0.75*DOWN)
        bg3 = BackgroundRectangle(l3, fill_opacity=1, fill_color=BLACK)
        
        v2 = VGroup(MathTex(r"\text{Summer Solstice}"), MathTex(r"\text{When the Sun is at its highest Declination from the Celestial Equator}"))
        v2.color = YELLOW
        v2.arrange(DOWN)
        v2.scale(0.35)
        v2.move_to(sun)
        v2.shift(0.75*DOWN)
        
        v3 = VGroup(MathTex(r"\text{Autumnal Equinox}"), MathTex(r"\text{Directly above the Celestial Equator at Solar Noon}"))
        v3.color = YELLOW
        v3.arrange(DOWN)
        v3.scale(0.35)
        v3.move_to(sun)
        v3.shift(0.75*DOWN)
        
        v4 = VGroup(MathTex(r"\text{Winter Solstice}"), MathTex(r"\text{When the Sun is at its lowest Declination from the Celestial Equator}"))
        v4.color = YELLOW
        v4.arrange(DOWN)
        v4.scale(0.35)
        v4.move_to(sun)
        v4.shift(0.75*DOWN)
        
        self.play(Create(line1))
        self.play(Write(t1))
        self.wait(1)
        self.play(Create(line2))
        self.add(bg23)
        self.play(Write(t23))
        self.wait(2)
        
        self.play(Create(sun))
        self.add(bg3)
        self.play(Write(l3))
        self.wait(2)
        
        self.play(MoveAlongPath(sun, cEquator, rate_func = lambda t: 0.25*(t+2)), run_time = 2)
        self.play(Transform(l3, v2))
        self.wait(2)
        
        self.play(MoveAlongPath(sun, cEquator, rate_func = lambda t: 0.25*(t+3)), run_time = 2)
        self.play(Transform(l3, v3))
        self.wait(2)
        
        self.play(MoveAlongPath(sun, cEquator, rate_func = lambda t: 0.25*(t)), run_time = 2)
        self.play(Transform(l3, v4))
        self.wait(3)
        
class Constellations(Scene):
    def construct(self):
        boundary.color = PURPLE
        equator.color = RED
        cEquator.color = BLUE
        self.add(VGroup(boundary, equator, cEquator))
        
        df = pd.read_csv(r"./Data/hygdata_v41.csv")
        df = df[df['mag'] < 7]
        ra_all = np.radians(df['ra'] * 15)
        dec_all = np.radians(df['dec'])
        x_all = np.cos(dec_all) * np.cos(ra_all)
        y_all = np.cos(dec_all) * np.sin(ra_all)
        positions_all = np.column_stack([2 * x_all, 2 * y_all, np.zeros_like(x_all)])
        star_positions_all = {
            int(row.id): pos
            for row, pos in zip(df.itertuples(index=False), positions_all)
        }
        stars_all = VGroup(*[Dot(point=pos, radius=0.025, color=WHITE) for pos in star_positions_all.values()])
        
        df = df[df['mag'] < 3]
        
        ra_rad = np.radians(df['ra'] * 15)
        dec_rad = np.radians(df['dec'])
        x = np.cos(dec_rad) * np.cos(ra_rad)
        y = np.cos(dec_rad) * np.sin(ra_rad)
        positions = np.column_stack([2 * x, 2 * y, np.zeros_like(x)])
        
        star_positions = {
            int(row.id): pos
            for row, pos in zip(df.itertuples(index=False), positions)
        }

        stars = VGroup(*[Dot(point=pos, radius=0.025, color=WHITE) for pos in star_positions.values()])
        self.play(Create(stars, run_time = 2))
        

        
        arrow = Arrow(start=[0, 0, 0], end=[0, 2.5, 0], color=YELLOW, buff=0)
        label = Text("North Celestial Pole", font_size=18, color=YELLOW).next_to(arrow, UP, buff=0.1)
        VGroup(arrow, label).rotate_about_origin(np.radians(23.4))

        self.play(Create(arrow), Write(label))
        self.wait(1)
        
        m1 = MathTex(r"\text{These are the 183 brightest stars out}", r"\text{of the trillions of stars in the Celestial Sphere.}")
        m1.scale(0.5)
        m1.arrange(DOWN)
        m1.move_to([0,3.5,0])
        self.play(Write(m1))
        self.wait(2)
        
        self.play(FadeOut(equator, cEquator, arrow, label))
        self.play(Create(stars_all, run_time = 2))
        self.wait(1)
        
        m2 = MathTex(r"\text{And this is only 16,000 of the brightest stars.}")
        m2.scale(0.5)
        m2.arrange(DOWN)
        m2.move_to([0,2.75,0])
        self.play(Write(m2))
        self.play(FadeOut(m1))
        
        self.wait(2)

        self.play(FadeOut(m2, stars_all))
        self.wait(1)
        
        mconc = MathTex(r"\text{What a beautiful universe we live in.}")
        mconc.scale(0.5)
        mconc.move_to([0,1,0])
        mconc.color = YELLOW
        self.play(VGroup(stars, boundary).animate.scale(20), run_time = 2)
        self.play(Write(mconc))
        self.wait(3)
        
        
