from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")


screen.bgcolor('black')
snake = Snake()
food = Food()
screen.tracer(0)
screen.listen()
score_snake = Scoreboard()


screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score_snake.score_increase()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        score_snake.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            score_snake.reset()
            snake.reset()




screen.exitonclick()
