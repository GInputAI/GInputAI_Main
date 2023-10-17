from pynput import keyboard, mouse
from threading import Thread


def KeyboardEvent():
    with keyboard.Events() as keyboardEvents:
        for keyboardEvent in keyboardEvents:
            print(keyboardEvent)


def MouseEvent():
    with mouse.Events() as events:
        for event in events:
            print(event)


thread1 = Thread(target=KeyboardEvent)
thread2 = Thread(target=MouseEvent)
thread1.start()
thread2.start()

