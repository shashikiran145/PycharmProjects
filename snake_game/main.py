from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)
screen.update()

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)


#    snake.move()

screen.exitonclick()


# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# snake = []
# for position in starting_positions:
#     segment = Turtle(shape='square')
#     segment.color('white')
#     segment.penup()
#     segment.goto(position)
#     snake.append(segment)

# for seg_num in range(len(snake) - 1, 0, -1):
#     new_x = snake[seg_num - 1].xcor()
#     new_y = snake[seg_num - 1].ycor()
#     snake[seg_num].goto(new_x, new_y)
# snake[0].forward(10)