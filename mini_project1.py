#mini-project 1

from manim import *
class Animation2(Scene):
    def construct(self):
        robot = Triangle(color = PINK).scale(0.6)
        axes = NumberPlane(x_range = [-5,7,1], y_range = [-4,4,1],x_length = 20, y_length = 10)
        axes.to_edge(LEFT, buff=0.5).to_edge(UR, buff = -0.45)
        self.play(Write(axes), run_time = 2)
        self.play(Create(robot), run_time = 4)
        self.play(robot.animate.shift(UP*2.2), run_time = 5)
        
        self.wait()
        robot.rotate(PI/2)
        self.play(robot.animate.shift(LEFT*3), run_time = 5)
        self.wait()