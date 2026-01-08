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


directions = [0, 90, 180, 270]
davi.pensize(15)
davi.speed("fastest")


for _ in range(200):
    davi.color(random_color())
    davi.forward(30)
    davi.setheading(random.choice(directions))















screen = Screen()
screen.exitonclick()