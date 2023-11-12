import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sh_ex_filepath.clicked.connect(lambda: self.open_file_dialog(self.ui.sh_ex_line_filepath))

    def open_file_dialog(self, label_upd):
        # Открываем диалог выбора файла
        dialog = QFileDialog(self)
        dialog.setDirectory("C:/Users/XUI/PycharmProjects/GInputAI_Main/exec")
        dialog.setAcceptMode(QFileDialog.AcceptOpen)  # Режим выбора одного файла
        dialog.fileSelected.connect(label_upd.setText)  # Подключаем слот для обновления QLabel
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())