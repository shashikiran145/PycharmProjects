import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')

# Drawing a square #
count = 0

# for count in range(4):
#     tim.forward(50)
#     tim.right(90)

# To draw alternate lines #

# tim.penup()
# tim.goto(-200, 0)
#
# for count in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Drawing different shapes #

# angle = 0
# colour = ["DarkSlateBlue", "blue2", "azure4", "cyan1", "chocolate", "CadetBlue", "CornFlowerBlue",
#           "DarkMagenta", "black", "BlueViolet", "DarkRed"]
#
# def draw_shape(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for sides_n in range(3, 11):
#     draw_shape(sides_n)
#     tim.color(random.choice(colour))

# Random Walk #

#colour = ["DarkSlateBlue", "blue2", "azure4", "cyan1", "chocolate", "CadetBlue", "CornFlowerBlue",
#          "DarkMagenta", "black", "BlueViolet", "DarkRed", "beige", "DarkSlateGray1"]

turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
#    colour_tuple = (r, g, b)
    tim.color(r, g, b)


move = [0, 90, 180, 270, 360]

tim.shape("arrow")
tim.pensize(5)
tim.speed(10)

for count in range(200):
    tim.forward(50)
    tim.setheading(random.choice(move))
    random_colour()




screen = Screen()
screen.exitonclick()
