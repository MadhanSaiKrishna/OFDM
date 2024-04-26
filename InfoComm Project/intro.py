from manim import *

class TextIntroduction(Scene):
    def construct(self):
        intro_text = Text("Welcome to our Presentation!", font_size=50, color=BLUE)
        self.play(Write(intro_text))
        self.play(FadeOut(intro_text))
        self.wait(2) 
        intro_madhan = Text("Madhan Sai Krishna\n   2023102030", font_size=32, color= WHITE)
        intro_praveen = Text("Nethavath Praveen\n   2023102013", font_size = 30, color= WHITE)
        intro_dinesh = Text("Nagalla Dinesh\n   202310xxxx", font_size = 30, color= WHITE)
        
        self.play(Write(intro_madhan))
        self.wait(1)
        self.play(intro_madhan.animate.shift(UP*2), run_time = 4)
        self.play(FadeIn(intro_praveen))
        self.wait(1)
        self.play(intro_praveen.animate.shift(LEFT*4), run_time = 4)
        self.wait(1)
        self.play(FadeIn(intro_dinesh))
        self.play(intro_dinesh.animate.shift(RIGHT*4), run_time = 4)
        self.wait(1)
        
        
        self.play(FadeOut(intro_madhan), FadeOut(intro_dinesh), FadeOut(intro_praveen))
        self.wait(2)
        self.play(Write(Text('Introduction to "The History of OFDM"')))
