from manim import *
    

class Intro(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Fermi Estimations}", r"\text{Part 1: The Drake Equation}", r"\text{An estimation for the number of}", r"\text{advanced civilizations in our universe.}")
        t1.arrange(DOWN)
        t1[0].color = BLUE
        t1[1:].color = GOLD
        t1.scale(0.5)
        
        self.play(Write(t1[0]))
        self.play(Write(t1[1]))
        self.play(Write(t1[2]), Write(t1[3]))
        self.wait(1)
        self.play(FadeOut(t1[0],t1[2:]), t1[1].animate.move_to([0,3,0]))
        self.wait(1)
        
        t2 = MathTex(r"\text{First, lets define an advanced civilization}", r"\text{as one that can transmit and recieve radio waves.}")
        t2.color = GOLD
        t2.arrange(DOWN).scale(0.5)
        t2.next_to(t1[1], DOWN)
        
        self.play(Write(t2))
        
        def radioAnimation():
            dish = Arc(
                radius=3,
                start_angle=-PI/4,
                angle=PI/2,
                color=WHITE,
                stroke_width=8
            )
            
            dish.shift(2*LEFT, 1*DOWN)
            
            self.play(Create(dish), run_time=1.5)
            
            incident_angle = 10 * DEGREES
            wave_length = 4
            
            start_pos = LEFT * 5 + DOWN * 2
            
            incident_direction = np.array([np.cos(incident_angle), np.sin(incident_angle), 0])
            
            def create_wave(position, direction, color=PURPLE):
                wave_group = VGroup()
                num_waves = 1
                for i in range(num_waves):
                    offset = i * 0.3
                    wave_points = []
                    for t in np.linspace(0, wave_length, 100):
                        x = t * direction[0]
                        y = t * direction[1] + 0.3 * np.sin(4 * PI * t - offset * 2 * PI)
                        wave_points.append(position + np.array([x, y, 0]))
                    
                    wave_curve = VMobject()
                    wave_curve.set_points_smoothly(wave_points)
                    wave_curve.set_color(color)
                    wave_curve.set_stroke(width=3)
                    wave_group.add(wave_curve)
                return wave_group
            
            incident_wave = create_wave(start_pos, incident_direction, PURPLE)
            self.play(Create(incident_wave))
            
            collision_point = [1,-1,0]
            travel_distance = np.linalg.norm(collision_point - start_pos)
            
            self.play(
                incident_wave.animate.shift(incident_direction * (travel_distance - wave_length * 0.7)),
                run_time=2,
                rate_func=linear
            )
            
            self.play(
                Flash(collision_point, color=YELLOW, flash_radius=0.8),
                run_time=0.3
            )
            
            reflected_direction = np.array([np.cos(PI - incident_angle), np.sin(PI - incident_angle), 0])
            
            reflected_wave = create_wave(collision_point + DOWN + RIGHT, reflected_direction, PURPLE)
            
            self.play(
                FadeOut(incident_wave),
                FadeIn(reflected_wave),
                run_time=0.5
            )
            
            self.play(
                reflected_wave.animate.shift(reflected_direction * 6),
                run_time=2.5,
                rate_func=linear
            )
            self.wait(1)
            self.play(FadeOut(reflected_wave, dish))
        radioAnimation()
        self.wait()
        
        
        
        self.wait(2)
