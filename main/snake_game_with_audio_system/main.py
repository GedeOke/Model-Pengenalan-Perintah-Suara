from turtle import Screen
from snake import Snake
import time
from audio_system import predict_mic

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    command = predict_mic()
    if command == "up":
        snake.up()
    elif command == "down":
        snake.down()
    elif command == "left":
        snake.left()
    elif command == "right":
        snake.right()

    snake.move()

screen.exitonclick()