# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slpgui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from slptest import PressureTest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import time

lane = 1
PT = PressureTest()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RunTest = QtWidgets.QPushButton(self.centralwidget)
        self.RunTest.setGeometry(QtCore.QRect(10, 140, 481, 51))
        self.RunTest.setObjectName("RunTest")
        self.RunTest.clicked.connect(self.RunTest_chick)
        self.Lane1 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lane1.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.Lane1.setObjectName("Lane1")
        self.Lane2 = QtWidgets.QCheckBox(self.centralwidget)
        self.Lane2.setGeometry(QtCore.QRect(140, 90, 101, 41))
        self.Lane2.setObjectName("Lane2")
        self.lane3 = QtWidgets.QCheckBox(self.centralwidget)
        self.lane3.setGeometry(QtCore.QRect(260, 90, 101, 41))
        self.lane3.setObjectName("lane3")
        self.lane4 = QtWidgets.QCheckBox(self.centralwidget)
        self.lane4.setGeometry(QtCore.QRect(380, 90, 101, 41))
        self.lane4.setObjectName("lane4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 481, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.resultslabel = QtWidgets.QLabel(self.centralwidget)
        self.resultslabel.setGeometry(QtCore.QRect(20, 200, 67, 17))
        self.resultslabel.setObjectName("resultslabel")
        self.Chippic = QtWidgets.QLabel(self.centralwidget)
        self.Chippic.setGeometry(QtCore.QRect(500, 0, 291, 391))
        self.Chippic.setText("")
        self.Chippic.setPixmap(QtGui.QPixmap("chip.png"))
        self.Chippic.setScaledContents(True)
        self.Chippic.setObjectName("Chippic")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 471, 61))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Single Lane Pressure Test"))
        self.RunTest.setText(_translate("MainWindow", "Run Test"))
        self.Lane1.setText(_translate("MainWindow", "Lane 1"))
        self.Lane2.setText(_translate("MainWindow", "Lane 2"))
        self.lane3.setText(_translate("MainWindow", "Lane 3"))
        self.lane4.setText(_translate("MainWindow", "Lane 4"))
        self.resultslabel.setText(_translate("MainWindow", "Results:"))
        self.label.setText(_translate("MainWindow", "To select a lane for testing, check the box. Once all desired "
                                                    "lanes have been selected, click the “Run Test” button. All "
                                                    "selected lanes will be pressure-tested from left to right."))

    def RunTest_chick(self):
        self.textBrowser.clear()
        m = 'Lane #            Date              Pressure Test                 Clog Test'
        self.textBrowser.append(m)
        for i in range(4):
            lane = str(self.onCheckBox_toggled())
            if lane == 'None':
                break
            else:
                print(lane)
                x = PT.test_gui(lane)
                self.textBrowser.append(x)


    def onCheckBox_toggled(self):
        while True:
            if self.Lane1.isChecked():
                self.Lane1.setChecked(False)
                return '1'
            elif self.Lane2.isChecked():
                self.Lane2.setChecked(False)
                return '2'
            elif self.lane3.isChecked():
                self.lane3.setChecked(False)
                return '3'
            elif self.lane4.isChecked():
                self.lane4.setChecked(False)
                return '4'
            else:
                break


#  import testing_rc
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
