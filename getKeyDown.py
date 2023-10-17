from pynput import mouse, keyboard
from threading import Thread


def KeyboardEvent():
    with keyboard.Events() as keyboardEvents:
        for event in keyboardEvents:
            print(event.key)


def on_click(x, y, button, pressed):
    if pressed:
        print(button, [x, y])


keyboardThread = Thread(target=KeyboardEvent)
keyboardThread.start()

with mouse.Listener(on_click=on_click) as mouseListener:
    mouseListener.join()
