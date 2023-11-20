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


def Start(ScriptName, start_butt = 'f7', stop_butt = 'f7', move_ = True, click_ = True, keyboard_ = True, scroll_ = False, termialmode_ = True):
    if __name__ in ("Record", "GInput.Record"):
        with Manager() as manager:
            reader = manager.list()

            # Process __init__
            Pclick = Process(target=start_listener_click, args=(reader, )) if move_ else None
            Pmove = Process(target=start_listener_move2, args=(reader, )) if click_ else None
            Pmove_delay = Process(target=start_listener_move) if move_ else None
            Pkeybroad = Process(target=start_listener_keyboard, args=(reader, )) if keyboard_ else None

            # Start on button
            print(f'Для старта нажми {start_butt}') if termialmode_ else None
            while True:
                if kb.is_pressed('f7'):
                    break
            time.sleep(0.1)
            print('Начало записи') if termialmode_ else None

            time_start = time.perf_counter()

            Pmove_delay.start() if move_ else None
            Pclick.start() if click_ else None
            Pkeybroad.start() if keyboard_ else None
            Pmove.start() if move_ else None

            while True:
                if kb.is_pressed(stop_butt):
                    break

            # Recalc
            reader = list(map(lambda x: x[:-1] + [x[-1] - time_start], reader))
            temp = deepcopy(reader)
            for i in range(1, len(reader)):
                reader[i][-1] = reader[i][-1] - temp[i - 1][-1]

            # Save to .pickle
            try:
                with open("../../data/" + ScriptName + '.pickle', "wb") as file:
                    pickle.dump(reader, file)
                    file.close()
            except FileNotFoundError:
                os.makedirs("../../data")
                with open("../../data/" + ScriptName + '.pickle', "wb") as file:
                    pickle.dump(reader, file)
                    file.close()

            # Exit process
            Pmove.terminate() if move_ else None
            Pclick.terminate() if click_ else None
            Pkeybroad.terminate() if keyboard_ else None
            Pmove_delay.terminate() if move_ else None

            print('Файл сохранён') if termialmode_ else None