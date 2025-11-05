from turtle import Turtle, Screen
import random

davi = Turtle()

colors = ["DarkGreen", "blue", "índigo", "PaleVioletRed", "PeachPuff", "teal", "DeepSkyBlue", "wheat"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        davi.forward(100)
        davi.right(angle)


for shape_side_n in range(3, 10):
    davi.color(random.choice(colors))
    draw_shape(shape_side_n)








screen = Screen()
screen.exitonclick()