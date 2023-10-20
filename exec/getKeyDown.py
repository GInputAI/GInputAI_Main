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
    def Save_to_file(self):
        with open("../readers/read_script.pickle", "wb") as file:
            pickle.dump(reader, file)
            file.close()
    def __init__(self, reader, time_start):
        self.reader = list(reader[:])
        for i in range(len(self.reader)):
            self.reader[i][-1] += - time_start

        temp_reader = deepcopy(self.reader)
        for i in range(1, len(reader)):
            self.reader[i][-1] = self.reader[i][-1] - temp_reader[i - 1][-1]

        '''
        print(list(filter(lambda x: x[0] == 'on_click',self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_move', self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_press', self.reader))[0])
        print(list(filter(lambda x: x[0] == 'on_release', self.reader))[0])
        '''

        self.Txt_to_Func()
        print(self.reader)
        self.Save_to_file()




def start_listener_click(reader):
    with mouse.Listener(on_click=lambda x, y, b, p: reader.append(['on_click', x, y, b, p, time.perf_counter()])) as click_listener:
        click_listener.join()
def start_listener_move(reader):
    with mouse.Listener(on_move=lambda x, y: reader.append(['on_move', x, y, time.perf_counter()])) as mouse_listener:
        mouse_listener.join()
def start_listener_keyboard(reader):
    with keyboard.Listener(on_press=lambda key: reader.append(['on_press', key, time.perf_counter()]),
                           on_release = lambda key: reader.append(['on_release', key, time.perf_counter()])) as keyboard_listener:
        keyboard_listener.join()


if __name__ == "__main__":
    with Manager() as manager:
        reader = manager.list()

        Pclick = Process(target=start_listener_click, args=(reader, ))
        Pmove = Process(target=start_listener_move, args=(reader, ))
        Pkeybroad = Process(target=start_listener_keyboard, args=(reader, ))

        print('Для старта нажми ESC')
        while True:
            if kb.is_pressed('Esc'):
                break
        time.sleep(0.1) #Чтобы не было такого что ESC и запустил и закрыл
        print('Начало записи')

        time_start = time.perf_counter()
        Pclick.start()
        Pmove.start()
        Pkeybroad.start()

        while True:
            if kb.is_pressed('Esc'):
                break

        Pclick.terminate()
        Pmove.terminate()
        Pkeybroad.terminate()

        print('Запись завершена')

        save1 = Reformat(reader, time_start)

        print('Для воспроизведения нажми ESC')
        while True:
            if kb.is_pressed('Esc'):
                break

        with open('../readers/read_script.pickle', "rb") as file:
            inputs = pickle.load(file)

        for i in inputs:
            i()
