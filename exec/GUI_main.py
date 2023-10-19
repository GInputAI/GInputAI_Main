import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from desing import Ui_MainWindow

class ahk_application():
    def __init__(self):
        super(ahk_application, self).__init__()
        self.ui = Ui_MainWindow()