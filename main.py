from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake_obj = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake_obj.move_up, "Up")
screen.onkey(snake_obj.move_down, "Down")
screen.onkey(snake_obj.move_left, "Left")
screen.onkey(snake_obj.move_right, "Right")
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move()

    scoreboard.write_score()
    # detect collision with food
    if snake_obj.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake_obj.extend_snake()

    # detect collision with wall
    if snake_obj.head.xcor() > 280 or snake_obj.head.xcor() < -280 \
            or snake_obj.head.ycor() > 280 or snake_obj.head.ycor() < -280:
        game_is_on = False

    # detect collision with tail
    if snake_obj.check_collision():
        game_is_on = False

scoreboard.game_over()
#time.sleep(5)
#screen.bye()
screen.exitonclick()
