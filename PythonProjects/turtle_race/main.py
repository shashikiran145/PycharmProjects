import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

#
# def move_forward():
#     new_turtle.forward(10)
#
#
# def move_backward():
#     new_turtle.back(10)
#
# def move_left():
#     new_turtle.left(45)
#
#
# def move_right():
#     new_turtle.right(45)
#
#
# def clear_screen():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_screen)

screen.setup(width=500, height=400)
user_input = screen.textinput(title="Who is going to win?", prompt="Choose a turtle")
print("You chose " + user_input)
colours = ["black", "red", "blue", "green", "yellow", "pink"]
y_positions = [-15, -45, -75, 15, 45, 75]
steps = [10, 12, 8, 11, 13, 9]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# if user_input:
#     is_race_on = True

while user_input:
    for turtle in all_turtles:
        turtle.forward(random.choice(steps))
        if turtle.xcor() > 240:
            result = turtle.color()
            screen.bye()
            if user_input == turtle.color():
                print("You win!")
                exit()
            else:
                print("You lost!")
                exit()


# if user_input == turtle.color():
#     print("You win!")
# else:
#     print("You Lose!")

screen.exitonclick()








# tim.color('black')
# tim.penup()
# tim.goto(x=-230, y=-15)
#
# tom.color('red')
# tom.penup()
# tom.goto(x=-230, y=-45)
#
# jim.color('blue')
# jim.penup()
# jim.goto(x=-230, y=-75)
#
# jom.color('green')
# jom.penup()
# jom.goto(x=-230, y=15)
#
# bim.color('yellow')
# bim.penup()
# bim.goto(x=-230, y=45)
#
# bom.color('pink')
# bom.penup()
# bom.goto(x=-230, y=75)