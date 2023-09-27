from Scoreboard import Scoreboard
from Snake import Snake
from turtle import Screen
from Food import Food
import time

START_POSITION = [(-40, 0), (-20, 0), (0, 0)]

while True:
    print("Choose Game options")
    print("0 For without wall")
    print("1 For with wall")
    print("2 To Exit Game")
    wall = int(input())
    if wall not in range(2):
        break

    print("Choose Difficulty level")
    print("1 For level 1")
    print("2 For level 2")
    print("3 For level 3")
    print("4 For level 4")
    print("5 For level 5")
    print("6 To Exit Game")

    difficulty = int(input())
    score_as_level = 2 * difficulty
    speed_as_difficulty = 1 - 0.194 * difficulty

    if difficulty not in range(1, 6):
        break

    snake = Snake(START_POSITION)
    food = Food()
    score = Scoreboard()
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.title("The Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    z_score = 0

    while game_is_on:
        snake.move(wall)
        screen.update()

        # detect colusion with food
        if snake.head.distance(food) < 15:
            food.refresh()
            z_score += score_as_level
            snake.grow()
            score.update(z_score)

        # detect colusion with wall
        if wall == 1:
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
                score.gameover()
                game_is_on = False

        # detect colusion with yoourself
        for segment in snake.segments[0:len(snake.segments) - 2]:
            if snake.head.distance(segment) < 15:
                score.gameover()
                game_is_on = False
        time.sleep(speed_as_difficulty)
    screen.exitonclick()



