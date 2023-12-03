from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_update = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.write(f"Score: {self.score_update}", False, 'center')
        self.hideturtle()

    def update(self):
        self.score_update = self.score_update + 1
        self.clear()
        self.write(f"Score: {self.score_update}", False, 'center')

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, 'center')





