from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

replay = True

while replay:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = ScoreBoard()
    screen.listen()

    screen.onkey(snake.u, "Up")
    screen.onkey(snake.d, "Down")
    screen.onkey(snake.l, "Left")
    screen.onkey(snake.r, "Right")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.07)
        snake.move()
        if snake.turtle_collection[0].distance(food) < 15:
            food.refresh()
            snake.add_length(snake.turtle_collection[-1].position())
            score.update_score()

        if snake.turtle_collection[0].xcor() > 285 or snake.turtle_collection[0].xcor() < -295 or snake.turtle_collection[
            0].ycor() > 295 or snake.turtle_collection[0].ycor() < -285:
            game_is_on = False
            replay = score.game_over()
            screen.clear()

        for x in snake.turtle_collection[1:]:
            if snake.turtle_collection[0].distance(x) < 8:
                game_is_on = False
                replay = score.game_over()
                screen.clear()
exit()
screen.exitonclick()
