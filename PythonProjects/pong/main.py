from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collisions with the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collisions with the paddle. If (== 330) doesn't work, use '>' or '<' sign
    if ball.distance(r_paddle) < 50 and ball.xcor() == 330 or ball.distance(l_paddle) < 50 and ball.xcor() == -330:
        ball.bounce_x()

    # Detect if the right paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_position()

    # Detect if the left paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_position()








screen.exitonclick()