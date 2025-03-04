from turtle import Turtle

FONT=("Courier",80,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0

    def update(self):
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align="center",font=FONT)

    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update()


    def r_point(self):
        self.r_score+=1
        self.clear()
        self.update()
