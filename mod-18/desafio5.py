import turtle as t
import random

davi = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

davi.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        davi.color(random_color())
        davi.circle(100)
        davi.setheading(davi.heading() + size_of_gap)

draw_spirograph(5)


my_screen = t.Screen()
my_screen.exitonclick()