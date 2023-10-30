import time
import keyboard as kb
from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput.mouse import Controller as ControllerM
from pynput import keyboard
from pynput.keyboard import Controller as ControllerK
from Geometry import math_grad

mouse = ControllerM()
keyboard = ControllerK()

def on_move(x, y):
    time.sleep(0.1)
    mouse.position = (x, y)

def grad_calc(xg, yg):
    return 960 + (xg / 0.15) // 1, 540 + (yg / 0.15) // 1

def go_to_pos(x, y):
    xg = x / 1920 * 90 - 45
    yg = y / 1080 * 90 - 45
    yg = 0
    print(xg, yg)
    on_move(*grad_calc(xg, yg))
def kb_press(but):
    time.sleep(0.2)
    keyboard.press(but)
    keyboard.release(but)
def kb_input(text, *args):
    for i in text:
        kb_press(i)
    if len(args) != 0:
        for i in args:
            kb_press(i)
def click_press():
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)

p = (960, 540)

while True:
    if kb.is_pressed('k'):
        kb_input('/kill', Key.enter)
        on_move(960, 570)
        time.sleep(1)
        click_press()

    if kb.is_pressed('l'):
        on_move(*grad_calc(*math_grad(*p, 90)))
        #on_move(*grad_calc(0,45))
    if kb.is_pressed('j'):
        p = mouse.position
    if kb.is_pressed('f6'):
        break
    if kb.is_pressed('o'):
        on_move(960, 510)
        time.sleep(0.3)
    if kb.is_pressed('p'):
        print(mouse.position)