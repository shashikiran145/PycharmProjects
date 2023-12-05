from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

# Detect collision with food

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_scoreboard()

# Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()

# Detect collisions with itself

    for i in snake.segments[1:]:
        if i == snake.head:
            pass
        if snake.head.distance(i) < 10:
            score.reset_game()
            snake.reset()


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