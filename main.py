from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

# Set up the screen
screen = Screen()
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
score = Score()

screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(800, 610)
screen.tracer(0)

# Listen for key presses
screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    score.update()

    # Detect collision with top and bottom walls
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 330 or
            ball.distance(paddle_left) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()