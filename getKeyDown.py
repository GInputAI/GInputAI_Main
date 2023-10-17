import pynput.mouse
from pynput import keyboard

with keyboard.Events() as keyboardEvents:
    for keyboardEvent in keyboardEvents:
        print(keyboardEvent)


with pynput.mouse.Events() as mouseEvents:
    for mouseEvent in mouseEvents:
        print(mouseEvent)


