# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pgui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from ppptest import PressureTest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import time

chip_numb = 1
PT = PressureTest()


class Ui_ChipPressureTest(object):
    def setupUi(self, ChipPressureTest):
        ChipPressureTest.setObjectName("ChipPressureTest")
        ChipPressureTest.resize(1132, 861)
        self.centralwidget = QtWidgets.QWidget(ChipPressureTest)
        self.centralwidget.setObjectName("centralwidget")
        self.InitRobot = QtWidgets.QPushButton(self.centralwidget)
        self.InitRobot.setGeometry(QtCore.QRect(30, 10, 181, 51))
        self.InitRobot.setObjectName("InitRobot")
        self.InitRobot.clicked.connect(self.init_click)
        self.HomeRobot = QtWidgets.QPushButton(self.centralwidget)
        self.HomeRobot.setGeometry(QtCore.QRect(240, 10, 171, 51))
        self.HomeRobot.setObjectName("HomeRobot")
        self.HomeRobot.clicked.connect(self.home_click)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 110, 131, 141))
        self.label_9.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.checkBox_chip16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip16.setGeometry(QtCore.QRect(1030, 280, 92, 23))
        self.checkBox_chip16.setObjectName("checkBox_chip16")
        self.checkBox_chip14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip14.setGeometry(QtCore.QRect(770, 280, 92, 23))
        self.checkBox_chip14.setObjectName("checkBox_chip14")
        self.checkBox_chip15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip15.setGeometry(QtCore.QRect(900, 280, 92, 23))
        self.checkBox_chip15.setObjectName("checkBox_chip15")
        self.checkBox_chip13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip13.setGeometry(QtCore.QRect(640, 280, 92, 23))
        self.checkBox_chip13.setObjectName("checkBox_chip13")
        self.checkBox_chip12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip12.setGeometry(QtCore.QRect(420, 280, 92, 23))
        self.checkBox_chip12.setObjectName("checkBox_chip12")
        self.checkBox_chip11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip11.setGeometry(QtCore.QRect(290, 280, 92, 23))
        self.checkBox_chip11.setObjectName("checkBox_chip11")
        self.checkBox_chip10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip10.setGeometry(QtCore.QRect(160, 280, 92, 23))
        self.checkBox_chip10.setObjectName("checkBox_chip10")
        self.checkBox_chip9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip9.setGeometry(QtCore.QRect(30, 280, 92, 23))
        self.checkBox_chip9.setObjectName("checkBox_chip9")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(940, 10, 171, 51))
        self.Exit.setObjectName("Exit")
        self.Exit.clicked.connect(QApplication.quit)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 510, 1111, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.results = QtWidgets.QLabel(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(20, 480, 670, 17))
        self.results.setObjectName("results")
        self.checkBox_chip1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip1.setGeometry(QtCore.QRect(30, 90, 92, 23))
        self.checkBox_chip1.setObjectName("checkBox_chip1")
        self.RunTest = QtWidgets.QPushButton(self.centralwidget)
        self.RunTest.setGeometry(QtCore.QRect(440, 10, 471, 51))
        self.RunTest.setObjectName("RunTest")
        self.RunTest.clicked.connect(self.RunTest_chick)
        self.checkBox_chip2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip2.setGeometry(QtCore.QRect(160, 90, 92, 23))
        self.checkBox_chip2.setObjectName("checkBox_chip2")
        self.checkBox_chip3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip3.setGeometry(QtCore.QRect(290, 90, 92, 23))
        self.checkBox_chip3.setObjectName("checkBox_chip3")
        self.checkBox_chip4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip4.setGeometry(QtCore.QRect(420, 90, 92, 23))
        self.checkBox_chip4.setObjectName("checkBox_chip4")
        self.checkBox_chip5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip5.setGeometry(QtCore.QRect(650, 90, 92, 23))
        self.checkBox_chip5.setObjectName("checkBox_chip5")
        self.checkBox_chip6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip6.setGeometry(QtCore.QRect(760, 90, 92, 23))
        self.checkBox_chip6.setObjectName("checkBox_chip6")
        self.checkBox_chip7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip7.setGeometry(QtCore.QRect(900, 90, 92, 23))
        self.checkBox_chip7.setObjectName("checkBox_chip7")
        self.checkBox_chip8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chip8.setGeometry(QtCore.QRect(1030, 90, 92, 23))
        self.checkBox_chip8.setObjectName("checkBox_chip8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(260, 110, 131, 141))
        self.label_13.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(130, 110, 131, 141))
        self.label_14.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 110, 131, 141))
        self.label_15.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(740, 110, 131, 141))
        self.label_16.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 110, 131, 141))
        self.label_10.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(870, 110, 131, 141))
        self.label_17.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1000, 110, 131, 141))
        self.label_18.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(740, 300, 131, 141))
        self.label_19.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 300, 131, 141))
        self.label_11.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(870, 300, 131, 141))
        self.label_20.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1000, 300, 131, 141))
        self.label_21.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(130, 300, 131, 141))
        self.label_22.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 300, 131, 141))
        self.label_12.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(260, 300, 131, 141))
        self.label_23.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(390, 300, 131, 141))
        self.label_24.setStyleSheet("image: url(:/newPrefix/pppbacker.JPG);")
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("backer.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        ChipPressureTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChipPressureTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 22))
        self.menubar.setObjectName("menubar")
        self.menuPPP_Pressure_Test = QtWidgets.QMenu(self.menubar)
        self.menuPPP_Pressure_Test.setObjectName("menuPPP_Pressure_Test")
        ChipPressureTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChipPressureTest)
        self.statusbar.setObjectName("statusbar")
        ChipPressureTest.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPPP_Pressure_Test.menuAction())

        self.retranslateUi(ChipPressureTest)
        QtCore.QMetaObject.connectSlotsByName(ChipPressureTest)

    def retranslateUi(self, ChipPressureTest):
        _translate = QtCore.QCoreApplication.translate
        ChipPressureTest.setWindowTitle(_translate("ChipPressureTest", "MainWindow"))
        self.InitRobot.setText(_translate("ChipPressureTest", "Init Robot"))
        self.HomeRobot.setText(_translate("ChipPressureTest", "Home Robot"))
        self.checkBox_chip16.setText(_translate("ChipPressureTest", "Chip 16"))
        self.checkBox_chip14.setText(_translate("ChipPressureTest", "Chip 14"))
        self.checkBox_chip15.setText(_translate("ChipPressureTest", "Chip 15"))
        self.checkBox_chip13.setText(_translate("ChipPressureTest", "Chip 13"))
        self.checkBox_chip12.setText(_translate("ChipPressureTest", "Chip 12"))
        self.checkBox_chip11.setText(_translate("ChipPressureTest", "Chip 11"))
        self.checkBox_chip10.setText(_translate("ChipPressureTest", "Chip 10"))
        self.checkBox_chip9.setText(_translate("ChipPressureTest", "Chip 9"))
        self.Exit.setText(_translate("ChipPressureTest", "Exit"))
        self.results.setText(_translate("ChipPressureTest", "Results:                               (PT = Pressure Test)            (CT = Clog Test)"))
        self.checkBox_chip1.setText(_translate("ChipPressureTest", "Chip 1"))
        self.RunTest.setText(_translate("ChipPressureTest", "Run Test"))
        self.checkBox_chip2.setText(_translate("ChipPressureTest", "Chip 2"))
        self.checkBox_chip3.setText(_translate("ChipPressureTest", "Chip 3"))
        self.checkBox_chip4.setText(_translate("ChipPressureTest", "Chip 4"))
        self.checkBox_chip5.setText(_translate("ChipPressureTest", "Chip 5"))
        self.checkBox_chip6.setText(_translate("ChipPressureTest", "Chip 6"))
        self.checkBox_chip7.setText(_translate("ChipPressureTest", "Chip 7"))
        self.checkBox_chip8.setText(_translate("ChipPressureTest", "Chip 8"))
        self.menuPPP_Pressure_Test.setTitle(_translate("ChipPressureTest", "PPP Pressure Test"))

    def init_click(self):
        time.sleep(2)
        self.textBrowser.setText('Initlize Completed')

    def home_click(self):
        time.sleep(4)
        self.textBrowser.setText('Homing Completed')
        self.InitRobot.setText('Wussup fool')

    def RunTest_chick(self):
        self.textBrowser.clear()
        m = 'Chip #             Date                Lane1 (PT/CT)                       Lane2 (PT/CT)                  Lane3 (PT/CT)                     Lane4 (PT/CT)'
        self.textBrowser.append(m)
        for i in range(16):
            chip_numb = str(self.onCheckBox_toggled())
            if chip_numb == 'None':
                break
            else:
                print(chip_numb)
                x = PT.test_gui(chip_numb)
                self.textBrowser.append(x)
                # also add a method that cleans up the presentation of the data

    def onCheckBox_toggled(self):
        while True:
            if self.checkBox_chip1.isChecked():
                self.checkBox_chip1.setChecked(False)
                return '1'
            elif self.checkBox_chip2.isChecked():
                self.checkBox_chip2.setChecked(False)
                return '2'
            elif self.checkBox_chip3.isChecked():
                self.checkBox_chip3.setChecked(False)
                return '3'
            elif self.checkBox_chip4.isChecked():
                self.checkBox_chip4.setChecked(False)
                return '4'
            elif self.checkBox_chip5.isChecked():
                self.checkBox_chip5.setChecked(False)
                return '5'
            elif self.checkBox_chip6.isChecked():
                self.checkBox_chip6.setChecked(False)
                return '6'
            elif self.checkBox_chip7.isChecked():
                self.checkBox_chip7.setChecked(False)
                return '7'
            elif self.checkBox_chip8.isChecked():
                self.checkBox_chip8.setChecked(False)
                return '8'
            elif self.checkBox_chip9.isChecked():
                self.checkBox_chip9.setChecked(False)
                return '9'
            elif self.checkBox_chip10.isChecked():
                self.checkBox_chip10.setChecked(False)
                return '10'
            elif self.checkBox_chip11.isChecked():
                self.checkBox_chip11.setChecked(False)
                return '11'
            elif self.checkBox_chip12.isChecked():
                self.checkBox_chip12.setChecked(False)
                return '12'
            elif self.checkBox_chip13.isChecked():
                self.checkBox_chip13.setChecked(False)
                return '13'
            elif self.checkBox_chip14.isChecked():
                self.checkBox_chip14.setChecked(False)
                return '14'
            elif self.checkBox_chip15.isChecked():
                self.checkBox_chip15.setChecked(False)
                return '15'
            elif self.checkBox_chip16.isChecked():
                self.checkBox_chip16.setChecked(False)
                return '16'
            else:
                break
        # add the rest of the checkBox's

    def numb_checkbox_clicked(self):
        chip = []
        for i in range(1, 3):
            if self.checkBox_chip1.checkState():
                print('up')


#  import testing_rc
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ChipPressureTest = QtWidgets.QMainWindow()
    ui = Ui_ChipPressureTest()
    ui.setupUi(ChipPressureTest)
    ChipPressureTest.show()
    sys.exit(app.exec_())
