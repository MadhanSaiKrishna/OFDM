from manim import*

class RectangularPulse(Scene):
    def construct(self):
        text = Text("Rectangular Pulse")
        self.play(Write(text))

class PulseSpectrum(Scene):
     def construct(self):
         self.play(Text("Pulse Spectrum"))

class OFDMSpectrum(Scene):
    def construct(self):
        self.play(Text("OFDM Spectrum"))

class cosinepulsespectrum(Scene):
    def construct(self):
        self.play(Text("Cosine Pulse Spectrum"))

class cosineofdmspectrum(Scene):
    def construct(self):
        self.play(Text("Cosine OFDM Spectrum"))
        
