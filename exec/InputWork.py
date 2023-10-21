import time
from pynput import mouse
from pynput.mouse import Controller as ControllerM
from pynput.keyboard import Controller as ControllerK, Key
import pickle

mouse_controller = ControllerM()
keyboard_controller = ControllerK()


def click_press(Button, Delay):
    time.sleep(Delay)
    mouse_controller.press(Button)


def click_release(Button, Delay):
    time.sleep(Delay)
    mouse_controller.release(Button)


def re_type_click(ButtonM, Delay, **kwargs):
    if True:
        return lambda: click_press(ButtonM, Delay)
    else:
        return lambda: click_release(ButtonM, Delay)


def on_move(x, y, Delay, **kwargs):
    time.sleep(Delay)
    mouse_controller.position = (x, y)


def on_press(ButtonK, Delay, **kwargs):
    time.sleep(Delay)
    keyboard_controller.press(ButtonK)


def on_release(ButtonK, Delay, **kwargs):
    time.sleep(Delay)
    keyboard_controller.release(ButtonK)

FuncList = {'on_click': re_type_click, 'on_move': on_move, 'on_press': on_press, 'on_release': on_release}

class RunScript():
    def Txt_to_Func(self):
        for i in range(len(self.reader)):
            self.reader[i] = FuncList[self.reader[i][0]](ButtonM = self.reader[i][-3],
                                                                      Delay = self.reader[i][-1], x = self.reader[i][1], y = self.reader[i][2],
                                                                      ButtonK = self.reader[i][1])
        self.reader = list(filter(lambda x: x != None, self.reader))
    def __init__(self, FilePath):
        with open(FilePath, "rb") as file:
            self.reader = pickle.load(file)
        self.Txt_to_Func()

    def __call__(self):
        for i in self.reader:
            i()

#Отработка скрипта
time.sleep(3)
TestObj = RunScript('../readers/read_script.pickle') #Это только __init__, массив значений упрощается до массива функций
while True:
    TestObj() #Это уже __call__, зацикленное воспроизведение