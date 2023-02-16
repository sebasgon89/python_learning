from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect_collition_with_food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

    #detect_collision_sith_wall
    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()

screen.exitonclick()