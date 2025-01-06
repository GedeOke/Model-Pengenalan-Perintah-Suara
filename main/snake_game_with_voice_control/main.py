from turtle import Screen
from snake import Snake
import time

from voice_control import predict_mic

import os

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
is_moving = False  # Variabel untuk melacak gerakan ular

def start_moving():
    global is_moving
    is_moving = True

def reset_game():
    global is_moving
    is_moving = False
    snake.reset()  # Pastikan metode reset() ada dalam kelas Snake
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game reset. Press Space to start again.")

screen.listen()
screen.onkey(start_moving, "space")
screen.onkey(reset_game, "BackSpace")

# Menambahkan event handler untuk gerakan ular
def move_up():
    if is_moving:
        snake.up()

def move_down():
    if is_moving:
        snake.down()

def move_left():
    if is_moving:
        snake.left()

def move_right():
    if is_moving:
        snake.right()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if is_moving:
        command = predict_mic()
        if command == "atas":
            snake.up()
        elif command == "bawah":
            snake.down()
        elif command == "kiri":
            snake.left()
        elif command == "kanan":
            snake.right()
        snake.move()

screen.exitonclick()