import time
from pynput.mouse import Controller as ControllerM
from pynput.keyboard import Controller as ControllerK, Key
import pickle
from copy import deepcopy
import keyboard as kb

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

class RunScript():
    def Txt_to_Func(self):
        for i in range(len(self.reader)):
            func_name = self.reader[i][0]
            fargs = self.reader[i][1:]
            if func_name == 'on_click':
                fargs = self.reader[i][3], self.reader[i][5]
                if self.reader[i][4]:
                    func_name = 'on_clickT'
                else:
                    func_name = 'on_clickF'

            self.reader[i] = lambda func=FuncList[func_name], args=fargs: func(*args)


        self.reader = deepcopy(list(filter(lambda x: x != None, self.reader)))
    def __init__(self, ScriptName):
        with open('../readers/' + ScriptName + '.pickle', "rb") as file:
            self.reader = pickle.load(file)
        self.Txt_to_Func()

    def __call__(self):
        print(len(self.reader))
        for i in self.reader:
            i()
        print('Done')

#Отработка скрипта
go_to_mine = RunScript('go_to_mine')
go_to_scala = RunScript('read_script')

print('Для старта нажми f7')
while True:
    if kb.is_pressed('f7'):
        break
go_to_mine()
go_to_scala()
