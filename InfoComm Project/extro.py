from manim import*

class Extro(Scene):
    def construct(self):
        extro_Text = Text("Thank You", color= WHITE, font_size=50)
        self.play(Write(extro_Text))
        self.play(FadeOut(extro_Text))
        self.wait(1)