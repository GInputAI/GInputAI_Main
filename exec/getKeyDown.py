import time
from multiprocessing import Process, Manager
import keyboard
from pynput import mouse
from pynput import keyboard as keyboard_event
from copy import deepcopy


def KeyboardEvent(reader, time_start):
    with keyboard_event.Events() as keyboardEvents:
        for event in keyboardEvents:
            reader.append([event.key, time.time() - time_start])


def on_click(x, y, button, pressed, reader, time_start):
    if pressed:
        reader.append([x, y, button, time.time() - time_start])


def start_listener(reader, time_start):
    with mouse.Listener(on_click=lambda x, y, b, p: on_click(x, y, b, p, reader, time_start)) as listener:
        listener.join()


if __name__ == "__main__":
    with Manager() as manager:
        reader = manager.list()
        p2 = Process(target=KeyboardEvent, args=(reader, time.time()))
        p = Process(target=start_listener, args=(reader, time.time()))
        p.start()
        p2.start()

        while True:
            if keyboard.is_pressed('q'):
                break

        p.terminate()
        p2.terminate()

        reader = list(reader[:])
        reader2 = deepcopy(reader)
        for i in range(1, len(reader)):
            reader[i][-1] = reader[i][-1] - reader2[i - 1][-1]
        with open("../readers/read_script.txt", "w") as file:
            for item in reader[:]:
                file.write(str(item) + "\n")
                