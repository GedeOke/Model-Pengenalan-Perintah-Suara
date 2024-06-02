import keyboard

def control_arrow(command):
    if command == "left":
        keyboard.press_and_release('left')
    elif command == "right":
        keyboard.press_and_release('right')
    elif command == "up":
        keyboard.press_and_release('up')
    elif command == "down":
        keyboard.press_and_release('down')