from manim import*

class FDM_bg(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=RED,
        )
        self.add(cos_func)
        label = Text("t", font_size=25).next_to(cos_func, DOWN)
        self.play(Write(label))
        self.play(Create(cos_func), run_time = 2)