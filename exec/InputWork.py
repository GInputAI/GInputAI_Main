import pynput
from pynput.mouse import Button, Controller as ControllerM
from pynput.keyboard import Controller as ControllerK
import time
import pickle


mouse = ControllerM()
keyboard = ControllerK()

MouseListButton = {'Button.left': Button.left, 'Button.right': Button.right}
KeyboardList = {'<Key.shift: <160>>': 'Shift'}


def click(x, y, Button):
    mouse.position = (x, y)
    mouse.click(Button)


def InputM(x, y, Button, Delay):
    time.sleep(Delay)
    click(x, y, Button)


def InputK(Button, Delay):
    time.sleep(Delay)
    keyboard.press(Button)
    keyboard.release(Button)


class InputWork():
    inputs = []

    def __init__(self, FilePatch):
        with open('../readers/read_script.pickle', "rb") as file:
            self.inputs = pickle.load(file)

    def Exec(self):
        for i in self.inputs:
            if len(i) == 4:
                InputM(i[0], i[1], i[2], i[3])
            else:
                InputK(i[0], i[1])


read_script1 = InputWork('../readers/read_script.pickle')
