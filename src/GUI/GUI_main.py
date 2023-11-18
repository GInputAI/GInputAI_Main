import sys
import threading
from multiprocessing import Process, Manager
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainUI import Ui_MainWindow
from GInput import Record
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.ui.sh_ex_filepath.clicked.connect(lambda: self.open_file_dialog(self.ui.sh_ex_line_filepath))
        self.ui.sh_rec_onmouseclick.setChecked(True)
        self.ui.sh_rec_onmousemove.setChecked(True)
        self.ui.sh_rec_onkeyboard.setChecked(True)
        self.ui.sh_rec_onperfcounter.setChecked(True)
        self.ui.sh_rec_start.clicked.connect(lambda: self.RecordStart(self.ui.sh_rec_line_filename.text()))

        #Executor
        self.ui.sh_ex_start.clicked.connect(lambda: self.ExecStart(self.ui.sh_ex_line_filepath.text()))

        #Process

    @classmethod
    def RecordStart(cls, name):
        if ExecStatus.value:
            return None
        if __name__ == "__main__":
            ExecStatus.value = True
            p = Process(target=cls.RecordStartUtil, args=(name, ExecStatus))
            p.start()

    @staticmethod
    def RecordStartUtil(name, ExecStatus):
        Record.Start(name)
        ExecStatus.value = False

    @classmethod
    def ExecStart(cls, filepath):
        if not filepath or not filepath.endswith('.py'):
            return None
        if ExecStatus.value:
            return None
        if __name__ == "__main__":
            ExecStatus.value = True
            p = Process(target=cls.ExecStartUtil, args=(filepath, ExecStatus))
            p.start()

    @staticmethod
    def ExecStartUtil(filepath, ExecStatus):
        # Отдельное пространство имен для модуля
        module_namespace = {}
        try:
            with open(filepath) as f:
                module_code = f.read()
            exec(module_code, module_namespace)
        except Exception as e:
            print(f'Произошла ошибка при выполнении скрипта: {str(e)}')
        ExecStatus.value = False


    def open_file_dialog(self, label_upd):
        dialog = QFileDialog(self)
        dialog.setDirectory(os.path.dirname(os.path.abspath(__file__))[0:-8] + "/Scripts")
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        dialog.fileSelected.connect(label_upd.setText)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ExecStatus = Manager().Value(bool, False)


    window = MainWindow()
    window.show()

    sys.exit(app.exec())
