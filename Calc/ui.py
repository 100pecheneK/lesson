# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\Calc\culc.ui'
#
# Created: Sat Apr 27 10:11:51 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(180, 290)
        MainWindow.setMinimumSize(QtCore.QSize(180, 290))
        MainWindow.setMaximumSize(QtCore.QSize(180, 292))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"height: 50px;\n"
"border: none;\n"
"background-color: rgb(118, 118, 118);\n"
"}\n"
"\n"
"QLineEdit {\n"
"color: white;\n"
"border: none;\n"
"background-color: black;\n"
"}\n"
"\n"
"QMainWindow {\n"
"background-color: black;\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 181, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(180, 45))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(180, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 0, 1, 4)
        self.Button_M_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_M_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_M_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_M_2.setFont(font)
        self.Button_M_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 234, 0);\n"
"}")
        self.Button_M_2.setObjectName("Button_M_2")
        self.gridLayout.addWidget(self.Button_M_2, 3, 3, 1, 1)
        self.Button_X_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_X_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_X_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_X_2.setFont(font)
        self.Button_X_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 234, 0);\n"
"}")
        self.Button_X_2.setObjectName("Button_X_2")
        self.gridLayout.addWidget(self.Button_X_2, 2, 3, 1, 1)
        self.Button_P_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_P_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_P_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_P_2.setFont(font)
        self.Button_P_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 234, 0);\n"
"}")
        self.Button_P_2.setObjectName("Button_P_2")
        self.gridLayout.addWidget(self.Button_P_2, 4, 3, 1, 1)
        self.Button_C_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_C_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_C_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_C_2.setFont(font)
        self.Button_C_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.Button_C_2.setObjectName("Button_C_2")
        self.gridLayout.addWidget(self.Button_C_2, 1, 0, 1, 1)
        self.Button_PM_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_PM_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_PM_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_PM_2.setFont(font)
        self.Button_PM_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.Button_PM_2.setObjectName("Button_PM_2")
        self.gridLayout.addWidget(self.Button_PM_2, 1, 1, 1, 1)
        self.Button_PRO_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_PRO_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_PRO_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_PRO_2.setFont(font)
        self.Button_PRO_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.Button_PRO_2.setObjectName("Button_PRO_2")
        self.gridLayout.addWidget(self.Button_PRO_2, 1, 2, 1, 1)
        self.Button_D_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_D_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_D_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_D_2.setFont(font)
        self.Button_D_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 234, 0);\n"
"}")
        self.Button_D_2.setObjectName("Button_D_2")
        self.gridLayout.addWidget(self.Button_D_2, 1, 3, 1, 1)
        self.Button_R_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_R_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_R_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_R_2.setFont(font)
        self.Button_R_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color:rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 234, 0);\n"
"}")
        self.Button_R_2.setObjectName("Button_R_2")
        self.gridLayout.addWidget(self.Button_R_2, 5, 3, 1, 1)
        self.Button_Z_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_Z_2.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_Z_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_Z_2.setFont(font)
        self.Button_Z_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_Z_2.setObjectName("Button_Z_2")
        self.gridLayout.addWidget(self.Button_Z_2, 5, 2, 1, 1)
        self.Button_13 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_13.setMinimumSize(QtCore.QSize(90, 45))
        self.Button_13.setMaximumSize(QtCore.QSize(90, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_13.setFont(font)
        self.Button_13.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_13.setObjectName("Button_13")
        self.gridLayout.addWidget(self.Button_13, 5, 0, 1, 2)
        self.Button_14 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_14.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_14.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_14.setFont(font)
        self.Button_14.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_14.setObjectName("Button_14")
        self.gridLayout.addWidget(self.Button_14, 4, 0, 1, 1)
        self.Button_10 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_10.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_10.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_10.setFont(font)
        self.Button_10.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_10.setObjectName("Button_10")
        self.gridLayout.addWidget(self.Button_10, 4, 1, 1, 1)
        self.Button_12 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_12.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_12.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_12.setFont(font)
        self.Button_12.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_12.setObjectName("Button_12")
        self.gridLayout.addWidget(self.Button_12, 4, 2, 1, 1)
        self.Button_18 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_18.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_18.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_18.setFont(font)
        self.Button_18.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_18.setObjectName("Button_18")
        self.gridLayout.addWidget(self.Button_18, 3, 2, 1, 1)
        self.Button_11 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_11.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_11.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_11.setFont(font)
        self.Button_11.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_11.setObjectName("Button_11")
        self.gridLayout.addWidget(self.Button_11, 3, 1, 1, 1)
        self.Button_15 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_15.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_15.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_15.setFont(font)
        self.Button_15.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_15.setObjectName("Button_15")
        self.gridLayout.addWidget(self.Button_15, 3, 0, 1, 1)
        self.Button_19 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_19.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_19.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_19.setFont(font)
        self.Button_19.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_19.setObjectName("Button_19")
        self.gridLayout.addWidget(self.Button_19, 2, 0, 1, 1)
        self.Button_17 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_17.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_17.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_17.setFont(font)
        self.Button_17.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_17.setObjectName("Button_17")
        self.gridLayout.addWidget(self.Button_17, 2, 1, 1, 1)
        self.Button_16 = QtGui.QPushButton(self.gridLayoutWidget)
        self.Button_16.setMinimumSize(QtCore.QSize(45, 45))
        self.Button_16.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.Button_16.setFont(font)
        self.Button_16.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgb(98, 98, 100);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(175, 175, 175);\n"
"}")
        self.Button_16.setObjectName("Button_16")
        self.gridLayout.addWidget(self.Button_16, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_M_2.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_X_2.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_P_2.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_C_2.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_PM_2.setText(QtGui.QApplication.translate("MainWindow", "+/-", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_PRO_2.setText(QtGui.QApplication.translate("MainWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_D_2.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_R_2.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_Z_2.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_13.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_14.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_10.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_12.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_18.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_11.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_15.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_19.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_17.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_16.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))