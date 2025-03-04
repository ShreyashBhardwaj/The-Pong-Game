from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
paddle_left = Paddle(-350,0)
paddle_right = Paddle(350,0)
ball = Ball()
score=Score()


screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(800,610)
screen.tracer(0)

#For Animation
screen.listen()

screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")

screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    score.update()

    if ball.ycor()==290 or ball.ycor()==-290:
        ball.bounce_y()

    #Detect Collision with r_paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor()>330 or
            ball.distance(paddle_left) < 50 and ball.xcor()<-330):

        ball.bounce_x()


    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    if  ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()