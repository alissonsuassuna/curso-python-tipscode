import turtle as turtle_module
import random
turtle_module.colormode(255)
davi = turtle_module.Turtle()
davi.speed("fastest")
davi.penup()
davi.hideturtle()

color_list = [(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101),
              (30, 43, 64), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161),
              (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73),
              (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219),
              (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

davi.setheading(225)
davi.forward(300)
davi.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    davi.dot(20, random.choice(color_list))
    davi.forward(50)

    if dot_count % 10 == 0:
        davi.setheading(90)
        davi.forward(50)
        davi.setheading(180)
        davi.forward(500)
        davi.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()