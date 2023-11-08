# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import files_ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 467)
        icon = QIcon()
        icon.addFile(u":/ico/ico/mouse_icon-icons.com_60636.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tab_main = QTabWidget(self.centralwidget)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_main.setGeometry(QRect(0, 0, 781, 471))
        self.tab_main.setStyleSheet(u"QTabBar::tab {\n"
"    width: 120px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    height: 30px; /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    padding: 5px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"    margin-right: 0px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u0441\u043f\u0440\u0430\u0432\u0430 \u043c\u0435\u0436\u0434\u0443 \u0432\u043a\u043b\u0430\u0434\u043a\u0430\u043c\u0438 */\n"
"}\n"
"QTabBar::tab {\n"
"    flex: 1;\n"
"    align-self: center;\n"
"}\n"
"")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.sh_start = QPushButton(self.tab1)
        self.sh_start.setObjectName(u"sh_start")
        self.sh_start.setGeometry(QRect(570, 370, 201, 41))
        self.file_path_label = QLabel(self.tab1)
        self.file_path_label.setObjectName(u"file_path_label")
        self.file_path_label.setGeometry(QRect(90, 380, 441, 20))
        self.tab_main.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayoutWidget = QWidget(self.tab2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 162, 103))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.tab_main.addTab(self.tab2, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.tab_main.addTab(self.tab4, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.tab_main.addTab(self.tab3, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.tab_main.addTab(self.tab5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GInput AI", None))
        self.sh_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.file_path_label.setText(QCoreApplication.translate("MainWindow", u"MIIAAYY", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Script Handler", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u044b\u0448\u044c (\u041a\u043b\u0438\u043a\u0438)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u044b\u0448\u044c (\u0412\u0441\u0435 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f)", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u043e\u043b\u043b", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Script Recorder", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"AI Data/Learn", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

