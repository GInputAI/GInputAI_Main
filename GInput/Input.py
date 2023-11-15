import time
from pynput.mouse import Controller as ControllerM
from pynput.keyboard import Controller as ControllerK
import pickle
from copy import deepcopy

mouse_controller = ControllerM()
keyboard_controller = ControllerK()


def click_press(Button, Delay):
    time.sleep(Delay)
    mouse_controller.press(Button)

def click_release(Button, Delay):
    time.sleep(Delay)
    mouse_controller.release(Button)

def on_move(x, y, Delay):
    time.sleep(Delay)
    mouse_controller.position = (x, y)

def on_press(ButtonK, Delay):
    time.sleep(Delay)
    keyboard_controller.press(ButtonK)

def on_release(ButtonK, Delay):
    time.sleep(Delay)
    keyboard_controller.release(ButtonK)


FuncList = {'on_move': lambda x, y, z: on_move(x, y, z),
            'on_press': lambda x, y: on_press(x, y),
            'on_release': lambda x, y: on_release(x, y),
            'on_clickT': lambda x, y: click_press(x, y),
            'on_clickF': lambda x, y: click_release(x, y)}

class Record():
    def Txt_to_Func(self):
        for i in range(len(self.reader)):
            func_name = self.reader[i][0]
            fargs = self.reader[i][1:]
            #fargs[-1] = fargs[-1] - 0.00001 #Очень имбовая строка надо поиграться с ней, чисто можно убрать все ассемблер инструкции лишние при записи
            if func_name == 'on_click':
                fargs = self.reader[i][3], self.reader[i][5]
                if self.reader[i][4]:
                    func_name = 'on_clickT'
                else:
                    func_name = 'on_clickF'

            self.reader[i] = lambda func=FuncList[func_name], args=fargs: func(*args)


        self.reader = deepcopy(list(filter(lambda x: x != None, self.reader)))
    def __init__(self, ScriptName):
        with open('../data/' + ScriptName + '.pickle', "rb") as file:
            self.reader = pickle.load(file)
        self.Txt_to_Func()

    def __call__(self):
        print('Inputs count: ', len(self.reader))
        for i in self.reader:
            i()
        print('Done')