from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')

# Drawing a square #
count = 0

# for count in range(4):
#     tim.forward(50)
#     tim.right(90)

# To draw alternate lines #

tim.penup()
tim.goto(-200, 0)

for count in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

screen = Screen()
screen.exitonclick()
