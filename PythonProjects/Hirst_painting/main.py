import turtle

import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('hirst_painting.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     rgb_colors.append(color)
#
# print(rgb_colors)

colors_list = [(236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]
choice = random.choice(colors_list)
r = choice[0]
g = choice[1]
b = choice[2]

# Hirst paiting #
# size of the painting = 10x10 #
# spacing = 50 and size of the dot = 20 #

x_pos = -300
y_pos = -200
turtle.colormode(255)
tim = Turtle()
tim.shape('circle')
tim.penup()
tim.goto(x_pos, y_pos)

for a in range(10):
    for _ in range(10):
        choice = random.choice(colors_list)
        tim.dot(20, choice)
        tim.penup()
        tim.forward(50)
    y_pos = tim.ycor()
    tim.goto(x_pos, y_pos + 50)

screen = Screen()
screen.exitonclick()









