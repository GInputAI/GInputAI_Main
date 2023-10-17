from multiprocessing import Process

import keyboard
import mouse
from pynput import mouse

inputFile = open("input.txt", "w")


def on_click(x, y, button, pressed):
    if pressed:
        inputFile.write(str(button))
        print(button, [x, y])


def on_key_press(event):
    inputFile.write(event.name)
    print(event.name)


keyboard.on_press(on_key_press)


def start_listener():
    listener = mouse.Listener(on_click=on_click, keyboard_click=on_key_press)
    listener.start()
    listener.join()


if __name__ == "__main__":
    p = Process(target=start_listener)
    p.start()
    while True:
        if keyboard.is_pressed('q'):
            inputFile.close()
            break
    p.terminate()
