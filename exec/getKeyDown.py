import time
from multiprocessing import Process, Manager
import keyboard as kb
from pynput import mouse
from pynput.mouse import Controller as ControllerM
from pynput import keyboard
from pynput.keyboard import Controller as ControllerK
from copy import deepcopy
import pickle

mouse_controller = ControllerM()
keyboard_controller = ControllerK()


class Reformat():
    def click_press(self, Button, Delay):
        time.sleep(Delay)
        mouse_controller.press(Button)

    def click_release(self, Button, Delay):
        time.sleep(Delay)
        mouse_controller.release(Button)
    def re_type_click(self, ButtonM, Delay, **kwargs):
        if True:
            return lambda: self.click_press(ButtonM , Delay)
        else:
            return lambda: self.click_release(ButtonM, Delay)

    def on_move(self, x, y, Delay, **kwargs):
        time.sleep(Delay)
        mouse.position = (x, y)

    def on_press(self, ButtonK, Delay, **kwargs):
        time.sleep(Delay)
        keyboard_controller.press(ButtonK)

    def on_release(self, ButtonK, Delay, **kwargs):
        time.sleep(Delay)
        keyboard_controller.release(ButtonK)


    FuncList = {'on_click': re_type_click, 'on_move': on_move, 'on_press': on_press, 'on_release': on_release}

    def Txt_to_Func(self):
        for i in range(len(self.reader)):
            self.reader[i] = lambda: self.FuncList[self.reader[i][0]](ButtonM = self.reader[i][-3],
                                                                      Delay = self.reader[i][-1], x = self.reader[i][1], y = self.reader[i][2],
                                                                      ButtonK = self.reader[i][1])
    def __init__(self, FilePath):
        with open(FilePath, "rb") as file:
            self.reader = pickle.load(file)
        '''
        print(list(filter(lambda x: x[0] == 'on_click',self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_move', self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_press', self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_release', self.reader))[0])
        '''
        self.Txt_to_Func()

def on_movel(x, y, reader):
    reader.append(['on_move', x, y, time.perf_counter()])
    time.sleep(0.04)

#time.slepp в on_movel с ним можно поиграться типо разную задержку попробовать

def start_listener_click(reader):
    with mouse.Listener(on_click=lambda x, y, b, p: reader.append(['on_click', x, y, b, p, time.perf_counter()])) as click_listener:
        click_listener.join()
def start_listener_move(reader):
    with mouse.Listener(on_move=lambda x, y: on_movel(x, y, reader)) as mouse_listener:
        mouse_listener.join()
def start_listener_keyboard(reader):
    with keyboard.Listener(on_press=lambda key: reader.append(['on_press', key, time.perf_counter()]),
                           on_release = lambda key: reader.append(['on_release', key, time.perf_counter()])) as keyboard_listener:
        keyboard_listener.join()

def record_script(ScriptName):
    if __name__ == "__main__":
        with Manager() as manager:
            reader = manager.list()

            Pclick = Process(target=start_listener_click, args=(reader, ))
            Pmove = Process(target=start_listener_move, args=(reader, ))
            Pkeybroad = Process(target=start_listener_keyboard, args=(reader, ))

            print('Для старта нажми f7' + '    |   script: ' + ScriptName)
            while True:
                if kb.is_pressed('f7'):
                    break
            time.sleep(0.1) #Чтобы не было такого что ESC и запустил и закрыл
            print('Начало записи ' + '    |   script: ' + ScriptName)

            time_start = time.perf_counter()
            Pclick.start()
            Pmove.start()
            Pkeybroad.start()

            while True:
                if kb.is_pressed('f7'):
                    break

            reader = list(reader[:])
            for i in range(len(reader)):
                reader[i][-1] += - time_start


            temp_reader = deepcopy(reader)
            for i in range(1, len(reader)):
                reader[i][-1] = reader[i][-1] - temp_reader[i - 1][-1]

            with open("../readers/" + ScriptName + '.pickle', "wb") as file:
                pickle.dump(reader, file)
                file.close()

            Pclick.terminate()
            Pmove.terminate()
            Pkeybroad.terminate()

            print('Файл сохранён' + '    |   script: ' + ScriptName)

record_script('go_to_mine')
