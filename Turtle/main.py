from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.hideturtle()
timmy.shape("arrow")
timmy.forward(100)
timmy.penup()
timmy.backward(200)
timmy.pendown()
timmy.left(90)
timmy.forward(100)


myscreen = Screen()
print(myscreen.canvheight)
print(myscreen.exitonclick())