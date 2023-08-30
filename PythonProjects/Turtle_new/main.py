from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')

# Drawing a square
count = 0

for count in range(4):
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()
