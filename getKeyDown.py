import time
from multiprocessing import Process, Manager
import keyboard
from pynput import mouse


def on_click(x, y, button, pressed, reader, time_start):
    if pressed:
        reader.append([x, y, button, time.time() - time_start])


def start_listener(reader, time_start):
    with mouse.Listener(on_click=lambda x, y, b, p: on_click(x, y, b, p, reader, time_start)) as listener:
        listener.join()


if __name__ == "__main__":
    with Manager() as manager:
        reader = manager.list()
        p = Process(target=start_listener, args=(reader, time.time()))
        p.start()

        while True:
            if keyboard.is_pressed('q'):
                break

        p.terminate()
        p.join()

        print(reader[:])  # Вывести все элементы списка reader
        with open("readers\read_script.txt", "w") as file:
            for item in reader[:]:
                file.write(str(item) + "\n")
                