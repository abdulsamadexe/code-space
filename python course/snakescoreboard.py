from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.write(f"Score :: {self.score}",align="center",font=("times new roman",24,"normal"))
        self.hideturtle()
    def new_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score :: {self.score}",align="center",font=("times new roman",24,"normal"))
    def gameover(self):
        self.clear()
        self.write("Game over",align="center",font=("times new roman",24,"normal"))

