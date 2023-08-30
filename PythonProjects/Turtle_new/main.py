from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')

# Drawing a square
count = 0

for count in range(0, 5):
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
