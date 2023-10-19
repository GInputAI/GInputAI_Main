import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from getKeyDown import start
from InputWork import InputWork


class AHKApplication(QMainWindow):
    def __init__(self):
        super(AHKApplication, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(start)
        self.ui.pushButton_2.clicked.connect(lambda: InputWork(FilePatch='../readers/read_script.pickle').Exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AHKApplication()
    window.show()

    sys.exit(app.exec())
