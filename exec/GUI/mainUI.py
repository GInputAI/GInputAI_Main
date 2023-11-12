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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
import files_ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 515)
        icon = QIcon()
        icon.addFile(u":/ico/ico/mouse_icon-icons.com_60636.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tab_main = QTabWidget(self.centralwidget)
        self.tab_main.setObjectName(u"tab_main")
        self.tab_main.setGeometry(QRect(0, 0, 881, 491))
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
        self.layoutWidget = QWidget(self.tab1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 40, 801, 131))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 10, 20, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"	qproperty-alignment: 'Qt::AlignBottom | Qt::AlignHCenter';\n"
"}")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, -1, -1, -1)
        self.sh_ex_line_filepath = QLineEdit(self.layoutWidget)
        self.sh_ex_line_filepath.setObjectName(u"sh_ex_line_filepath")
        self.sh_ex_line_filepath.setMaximumSize(QSize(16777215, 23))

        self.horizontalLayout.addWidget(self.sh_ex_line_filepath)

        self.sh_ex_filepath = QPushButton(self.layoutWidget)
        self.sh_ex_filepath.setObjectName(u"sh_ex_filepath")
        self.sh_ex_filepath.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/ico/ico/folder_open_FILL0_wght400_GRAD0_opsz24.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sh_ex_filepath.setIcon(icon1)

        self.horizontalLayout.addWidget(self.sh_ex_filepath)

        self.horizontalLayout.setStretch(0, 20)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sh_ex_start = QPushButton(self.layoutWidget)
        self.sh_ex_start.setObjectName(u"sh_ex_start")
        self.sh_ex_start.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.sh_ex_start)

        self.sh_ex_stop = QPushButton(self.layoutWidget)
        self.sh_ex_stop.setObjectName(u"sh_ex_stop")
        self.sh_ex_stop.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.sh_ex_stop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.sh_ex_scripteditor = QPushButton(self.layoutWidget)
        self.sh_ex_scripteditor.setObjectName(u"sh_ex_scripteditor")
        self.sh_ex_scripteditor.setMaximumSize(QSize(219, 85))

        self.horizontalLayout_3.addWidget(self.sh_ex_scripteditor)

        self.horizontalLayout_3.setStretch(0, 100)
        self.horizontalLayout_3.setStretch(1, 45)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.layoutWidget_5 = QWidget(self.tab1)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 250, 801, 121))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 0, 20, 0)
        self.label_5 = QLabel(self.layoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"	qproperty-alignment: 'Qt::AlignBottom | Qt::AlignHCenter';\n"
"}")

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.layoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-family: \"Noto Sans\";\n"
"	qproperty-alignment: 'Qt::AlignVCenter | Qt::AlignHCenter';\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(5, 10, -1, -1)
        self.sh_rec_onmouseclick = QCheckBox(self.layoutWidget_5)
        self.sh_rec_onmouseclick.setObjectName(u"sh_rec_onmouseclick")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.sh_rec_onmouseclick)

        self.sh_rec_onmousemove = QCheckBox(self.layoutWidget_5)
        self.sh_rec_onmousemove.setObjectName(u"sh_rec_onmousemove")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sh_rec_onmousemove)

        self.sh_rec_onmousescroll = QCheckBox(self.layoutWidget_5)
        self.sh_rec_onmousescroll.setObjectName(u"sh_rec_onmousescroll")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sh_rec_onmousescroll)

        self.sh_rec_onkeyboard = QCheckBox(self.layoutWidget_5)
        self.sh_rec_onkeyboard.setObjectName(u"sh_rec_onkeyboard")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sh_rec_onkeyboard)


        self.horizontalLayout_6.addLayout(self.formLayout)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.layoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-family: \"Noto Sans\";\n"
"	qproperty-alignment: 'Qt::AlignVCenter | Qt::AlignHCenter';\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.sh_rec_ontimetime = QRadioButton(self.layoutWidget_5)
        self.sh_rec_ontimetime.setObjectName(u"sh_rec_ontimetime")

        self.horizontalLayout_4.addWidget(self.sh_rec_ontimetime)

        self.sh_rec_onperfcounter = QRadioButton(self.layoutWidget_5)
        self.sh_rec_onperfcounter.setObjectName(u"sh_rec_onperfcounter")

        self.horizontalLayout_4.addWidget(self.sh_rec_onperfcounter)

        self.sh_rec_onprocesstime = QRadioButton(self.layoutWidget_5)
        self.sh_rec_onprocesstime.setObjectName(u"sh_rec_onprocesstime")

        self.horizontalLayout_4.addWidget(self.sh_rec_onprocesstime)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, -1, 5, -1)
        self.sh_rec_start = QPushButton(self.layoutWidget_5)
        self.sh_rec_start.setObjectName(u"sh_rec_start")
        self.sh_rec_start.setMinimumSize(QSize(0, 0))
        self.sh_rec_start.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_10.addWidget(self.sh_rec_start)

        self.sh_rec_stop = QPushButton(self.layoutWidget_5)
        self.sh_rec_stop.setObjectName(u"sh_rec_stop")
        self.sh_rec_stop.setMinimumSize(QSize(0, 0))
        self.sh_rec_stop.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_10.addWidget(self.sh_rec_stop)


        self.verticalLayout_17.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_7.addLayout(self.verticalLayout_17)

        self.sh_rec_recordeditor = QPushButton(self.layoutWidget_5)
        self.sh_rec_recordeditor.setObjectName(u"sh_rec_recordeditor")
        self.sh_rec_recordeditor.setMaximumSize(QSize(219, 85))

        self.horizontalLayout_7.addWidget(self.sh_rec_recordeditor)

        self.horizontalLayout_7.setStretch(1, 10)
        self.horizontalLayout_7.setStretch(2, 8)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tab_main.addTab(self.tab1, "")
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Executor", None))
        self.sh_ex_filepath.setText("")
        self.sh_ex_start.setText(QCoreApplication.translate("MainWindow", u"Start (f6)", None))
        self.sh_ex_stop.setText(QCoreApplication.translate("MainWindow", u"Stop (f6)", None))
        self.sh_ex_scripteditor.setText(QCoreApplication.translate("MainWindow", u"Script Editor", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recorder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Record on", None))
        self.sh_rec_onmouseclick.setText(QCoreApplication.translate("MainWindow", u"Mouse (Click)", None))
        self.sh_rec_onmousemove.setText(QCoreApplication.translate("MainWindow", u"Mouse (Move)", None))
        self.sh_rec_onmousescroll.setText(QCoreApplication.translate("MainWindow", u"Mouse (Scroll)", None))
        self.sh_rec_onkeyboard.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Time mode", None))
        self.sh_rec_ontimetime.setText(QCoreApplication.translate("MainWindow", u"time.time()", None))
        self.sh_rec_onperfcounter.setText(QCoreApplication.translate("MainWindow", u"perf_counter()", None))
        self.sh_rec_onprocesstime.setText(QCoreApplication.translate("MainWindow", u"process_time()", None))
        self.sh_rec_start.setText(QCoreApplication.translate("MainWindow", u"Start (f7)", None))
        self.sh_rec_stop.setText(QCoreApplication.translate("MainWindow", u"Stop (f6)", None))
        self.sh_rec_recordeditor.setText(QCoreApplication.translate("MainWindow", u"Record Editor", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Script Handler", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"AI Data/Learn", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi
