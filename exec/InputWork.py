import pynput
from pynput.mouse import Button, ControllerM
from pynput.keyboard import Controller as Controllerk
import time

mouse = ControllerM()
MouseListButton = {'Button.left': Button.left, 'Button.right': Button.right}



def click(x, y, Button):
    mouse.position = (x, y)
    mouse.click(Button)

def InputM(x, y, Button, Delay):
    click(x, y, Button)
    time.sleep(Delay)
def InputK(x, y, Button, Delay):
    click(x, y, Button)
    time.sleep(Delay)

class InputWork():
    inputs = []
    def __init__(self, FilePatch):
        with open(FilePatch, 'r') as f:
            for i in f:
                self.inputs.append(eval(i))
    def Exec(self):
        for i in self.inputs:
            if len(i) == 4:
                InputM(self.inputs[0], self.inputs[1], MouseListButton[self.inputs[2]], self.inputs[3])
            else:
                InputK(self.inputs[0], self.inputs[1])

read_script1 = InputWork('../readers/read_script.txt')
read_script1.Exec()