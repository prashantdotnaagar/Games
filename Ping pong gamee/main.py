from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

score=Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball()

screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    pong_ball.move()
    time.sleep(pong_ball.move_speed)
    if(pong_ball.ycor()>280 or pong_ball.ycor()<-280):
        pong_ball.turn_y()

    if(pong_ball.distance(r_paddle)<50 and pong_ball.xcor()>320 or pong_ball.distance(l_paddle)<50 and pong_ball.xcor()<-320):
        pong_ball.turn_x()

    #if right paddle misses
    if(pong_ball.xcor()>380):
        score.l_point()
        score.update_scoreboard()
        pong_ball.reset_position()

        # if left paddle misses
    if (pong_ball.xcor() < -380):
        score.r_point()
        score.update_scoreboard()
        pong_ball.reset_position()

screen.exitonclick()