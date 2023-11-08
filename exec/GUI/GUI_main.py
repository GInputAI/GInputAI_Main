import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sh_start.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        # Открываем диалог выбора файла
        dialog = QFileDialog(self)
        dialog.setDirectory("C:/Users/XUI/PycharmProjects/GInputAI_Main/exec")
        dialog.setAcceptMode(QFileDialog.AcceptOpen)  # Режим выбора одного файла
        dialog.fileSelected.connect(self.ui.file_path_label.setText)  # Подключаем слот для обновления QLabel
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
