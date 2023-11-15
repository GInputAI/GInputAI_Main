import os
import time
from multiprocessing import Process, Manager
import keyboard as kb
from pynput import mouse
from pynput import keyboard
from copy import deepcopy
import pickle

def on_movel(x, y, reader):
    reader.append(['on_move', x, y, time.perf_counter()])
    time.sleep(0.0325)

def start_listener_click(reader):
    with mouse.Listener(on_click=lambda x, y, b, p: reader.append(['on_click', x, y, b, p, time.perf_counter()])) as click_listener:
        click_listener.join()

def start_listener_move():
    with mouse.Listener(on_move=lambda x, y: time.sleep(0.04)) as mouse_listener:
        mouse_listener.join()

def start_listener_move2(reader):
    with mouse.Listener(on_move=lambda x, y: reader.append(['on_move', x, y, time.perf_counter()])) as mouse_listener:
        mouse_listener.join()

def start_listener_keyboard(reader):
    with keyboard.Listener(on_press=lambda key: reader.append(['on_press', key, time.perf_counter()]),
                           on_release = lambda key: reader.append(['on_release', key, time.perf_counter()])) as keyboard_listener:
        keyboard_listener.join()


def Start(ScriptName):
    if __name__ in ("Record", "GInput.Record"):
        with Manager() as manager:
            reader = manager.list()

            Pclick = Process(target=start_listener_click, args=(reader, ))
            Pmove = Process(target=start_listener_move2, args=(reader, ))
            Pmove_delay = Process(target=start_listener_move)
            Pkeybroad = Process(target=start_listener_keyboard, args=(reader, ))

            print('Для старта нажми f7')
            while True:
                if kb.is_pressed('f7'):
                    break
            time.sleep(0.1)
            print('Начало записи')

            time_start = time.perf_counter()
            Pmove_delay.start()
            Pclick.start()
            Pkeybroad.start()
            Pmove.start()

            while True:
                if kb.is_pressed('f7'):
                    break

            reader = list(reader[:])
            for i in range(len(reader)):
                reader[i][-1] += - time_start


            temp_reader = deepcopy(reader)
            for i in range(1, len(reader)):
                reader[i][-1] = reader[i][-1] - temp_reader[i - 1][-1]

            if not os.path.exists("../../data"):
                os.makedirs("..../data")
            with open("../../data/" + ScriptName + '.pickle', "wb") as file:
                pickle.dump(reader, file)
                file.close()

            Pmove.terminate()
            Pclick.terminate()
            Pkeybroad.terminate()
            Pmove_delay.terminate()

            print('Файл сохранён')