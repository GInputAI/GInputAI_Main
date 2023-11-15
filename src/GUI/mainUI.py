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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import files_ico_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(807, 515)
        icon = QIcon()
        icon.addFile(u":/ico/ico/mouse_icon-icons.com_60636.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
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
        self.sh_ex = QFrame(self.tab1)
        self.sh_ex.setObjectName(u"sh_ex")
        self.sh_ex.setGeometry(QRect(10, 40, 781, 131))
        self.sh_ex.setStyleSheet(u"QFrame#sh_ex {\n"
"   background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.sh_ex.setFrameShape(QFrame.StyledPanel)
        self.sh_ex.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.sh_ex)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 781, 131))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 10, 15, 10)
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
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, -1, -1, -1)
        self.sh_ex_line_filepath = QLineEdit(self.layoutWidget)
        self.sh_ex_line_filepath.setObjectName(u"sh_ex_line_filepath")
        self.sh_ex_line_filepath.setMaximumSize(QSize(16777215, 23))
        self.sh_ex_line_filepath.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.sh_ex_line_filepath)

        self.sh_ex_filepath = QPushButton(self.layoutWidget)
        self.sh_ex_filepath.setObjectName(u"sh_ex_filepath")
        self.sh_ex_filepath.setMinimumSize(QSize(31, 31))
        self.sh_ex_filepath.setMaximumSize(QSize(31, 31))
        self.sh_ex_filepath.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(210,210,210);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(225,225,225);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(210,210,210);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")
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
        self.sh_ex_start.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_2.addWidget(self.sh_ex_start)

        self.sh_ex_stop = QPushButton(self.layoutWidget)
        self.sh_ex_stop.setObjectName(u"sh_ex_stop")
        self.sh_ex_stop.setMaximumSize(QSize(16777215, 40))
        self.sh_ex_stop.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_2.addWidget(self.sh_ex_stop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.sh_ex_scripteditor = QPushButton(self.layoutWidget)
        self.sh_ex_scripteditor.setObjectName(u"sh_ex_scripteditor")
        self.sh_ex_scripteditor.setMaximumSize(QSize(215, 85))
        self.sh_ex_scripteditor.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_3.addWidget(self.sh_ex_scripteditor)

        self.horizontalLayout_3.setStretch(0, 100)
        self.horizontalLayout_3.setStretch(1, 45)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.sh_rec = QFrame(self.tab1)
        self.sh_rec.setObjectName(u"sh_rec")
        self.sh_rec.setGeometry(QRect(10, 240, 781, 141))
        self.sh_rec.setStyleSheet(u"QFrame#sh_rec {\n"
"   background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.sh_rec.setFrameShape(QFrame.StyledPanel)
        self.sh_rec.setFrameShadow(QFrame.Raised)
        self.layoutWidget_5 = QWidget(self.sh_rec)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 0, 781, 141))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 10, 15, 10)
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
        self.frame_recon = QFrame(self.layoutWidget_5)
        self.frame_recon.setObjectName(u"frame_recon")
        self.frame_recon.setStyleSheet(u"QFrame#frame_recon {\n"
"   background-color: rgba(0,0,0,0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 3px;\n"
"}")
        self.frame_recon.setFrameShape(QFrame.StyledPanel)
        self.frame_recon.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_recon)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 524, 91))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(3, -1, -1, -1)
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_14.addWidget(self.label_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(3)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(5, 5, -1, -1)
        self.sh_rec_onmouseclick = QCheckBox(self.layoutWidget_2)
        self.sh_rec_onmouseclick.setObjectName(u"sh_rec_onmouseclick")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.sh_rec_onmouseclick)

        self.sh_rec_onmousemove = QCheckBox(self.layoutWidget_2)
        self.sh_rec_onmousemove.setObjectName(u"sh_rec_onmousemove")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sh_rec_onmousemove)

        self.sh_rec_onmousescroll = QCheckBox(self.layoutWidget_2)
        self.sh_rec_onmousescroll.setObjectName(u"sh_rec_onmousescroll")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.sh_rec_onmousescroll)

        self.sh_rec_onkeyboard = QCheckBox(self.layoutWidget_2)
        self.sh_rec_onkeyboard.setObjectName(u"sh_rec_onkeyboard")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sh_rec_onkeyboard)


        self.horizontalLayout_14.addLayout(self.formLayout_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, -1, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_9.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.label_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 3, 0, -1)
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.sh_rec_ontimetime = QRadioButton(self.layoutWidget_2)
        self.sh_rec_ontimetime.setObjectName(u"sh_rec_ontimetime")

        self.horizontalLayout_12.addWidget(self.sh_rec_ontimetime)

        self.sh_rec_onperfcounter = QRadioButton(self.layoutWidget_2)
        self.sh_rec_onperfcounter.setObjectName(u"sh_rec_onperfcounter")

        self.horizontalLayout_12.addWidget(self.sh_rec_onperfcounter)

        self.sh_rec_onprocesstime = QRadioButton(self.layoutWidget_2)
        self.sh_rec_onprocesstime.setObjectName(u"sh_rec_onprocesstime")

        self.horizontalLayout_12.addWidget(self.sh_rec_onprocesstime)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, -1, 12, -1)
        self.sh_rec_line_filename = QLineEdit(self.layoutWidget_2)
        self.sh_rec_line_filename.setObjectName(u"sh_rec_line_filename")
        self.sh_rec_line_filename.setMaximumSize(QSize(16777215, 23))
        self.sh_rec_line_filename.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"	margin-right: 3px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.sh_rec_line_filename)

        self.sh_rec_start = QPushButton(self.layoutWidget_2)
        self.sh_rec_start.setObjectName(u"sh_rec_start")
        self.sh_rec_start.setMinimumSize(QSize(0, 28))
        self.sh_rec_start.setMaximumSize(QSize(16777215, 28))
        self.sh_rec_start.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_13.addWidget(self.sh_rec_start)

        self.sh_rec_stop = QPushButton(self.layoutWidget_2)
        self.sh_rec_stop.setObjectName(u"sh_rec_stop")
        self.sh_rec_stop.setMinimumSize(QSize(0, 28))
        self.sh_rec_stop.setMaximumSize(QSize(16777215, 28))
        self.sh_rec_stop.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_13.addWidget(self.sh_rec_stop)

        self.horizontalLayout_13.setStretch(0, 1000)
        self.horizontalLayout_13.setStretch(1, 350)
        self.horizontalLayout_13.setStretch(2, 350)

        self.verticalLayout_18.addLayout(self.horizontalLayout_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_18)


        self.horizontalLayout_7.addWidget(self.frame_recon)

        self.sh_rec_recordeditor = QPushButton(self.layoutWidget_5)
        self.sh_rec_recordeditor.setObjectName(u"sh_rec_recordeditor")
        self.sh_rec_recordeditor.setMaximumSize(QSize(215, 85))
        self.sh_rec_recordeditor.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_7.addWidget(self.sh_rec_recordeditor)

        self.horizontalLayout_7.setStretch(0, 1000)
        self.horizontalLayout_7.setStretch(1, 420)

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
        self.sh_ex_line_filepath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select .txt script path", None))
        self.sh_ex_filepath.setText("")
        self.sh_ex_start.setText(QCoreApplication.translate("MainWindow", u"Start (f6)", None))
        self.sh_ex_stop.setText(QCoreApplication.translate("MainWindow", u"Stop (f6)", None))
#if QT_CONFIG(whatsthis)
        self.sh_ex_scripteditor.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.sh_ex_scripteditor.setText(QCoreApplication.translate("MainWindow", u"Script Editor", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Recorder", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Record on", None))
        self.sh_rec_onmouseclick.setText(QCoreApplication.translate("MainWindow", u"Mouse (Click)", None))
        self.sh_rec_onmousemove.setText(QCoreApplication.translate("MainWindow", u"Mouse (Move)", None))
        self.sh_rec_onmousescroll.setText(QCoreApplication.translate("MainWindow", u"Mouse (Scroll)", None))
        self.sh_rec_onkeyboard.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Time mode", None))
        self.sh_rec_ontimetime.setText(QCoreApplication.translate("MainWindow", u"time.time()", None))
        self.sh_rec_onperfcounter.setText(QCoreApplication.translate("MainWindow", u"perf_counter()", None))
        self.sh_rec_onprocesstime.setText(QCoreApplication.translate("MainWindow", u"process_time()", None))
        self.sh_rec_line_filename.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter script name", None))
        self.sh_rec_start.setText(QCoreApplication.translate("MainWindow", u"Start (f7)", None))
        self.sh_rec_stop.setText(QCoreApplication.translate("MainWindow", u"Stop (f7)", None))
        self.sh_rec_recordeditor.setText(QCoreApplication.translate("MainWindow", u"Record Editor", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Script Handler", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"AI Data/Learn", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

