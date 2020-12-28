# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'troughfiller.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time, os, sys
sys.path.append("/home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics")
from tfiller import troughF

t = troughF()

class Ui_MainWindow(object):

    firstNum = None
    userIsTypingSecondNumber = False

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 435)
        self.troughfgui = QtWidgets.QWidget(MainWindow)
        self.troughfgui.setObjectName("troughfgui")
        self.primefluid = QtWidgets.QPushButton(self.troughfgui)
        self.primefluid.setGeometry(QtCore.QRect(20, 50, 331, 101))
        self.primefluid.setObjectName("primefluid")
        self.primefluid.clicked.connect(self.primeFluid)
        self.sumtext = QtWidgets.QLabel(self.troughfgui)
        self.sumtext.setGeometry(QtCore.QRect(10, -10, 671, 71))
        font = QtGui.QFont()
        font.setItalic(True)
        self.sumtext.setFont(font)
        self.sumtext.setTextFormat(QtCore.Qt.PlainText)
        self.sumtext.setScaledContents(True)
        self.sumtext.setWordWrap(True)
        self.sumtext.setObjectName("sumtext")
        self.dateEdit = QtWidgets.QDateEdit(self.troughfgui)
        self.dateEdit.setGeometry(QtCore.QRect(680, 0, 110, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.calc_7 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_7.setGeometry(QtCore.QRect(400, 180, 81, 61))
        self.calc_7.setObjectName("calc_7")
        self.calc_7.clicked.connect(self.digit_pressed)
        self.calc_4 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_4.setGeometry(QtCore.QRect(400, 250, 81, 61))
        self.calc_4.setObjectName("calc_4")
        self.calc_4.clicked.connect(self.digit_pressed)
        self.calc_1 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_1.setGeometry(QtCore.QRect(400, 320, 81, 61))
        self.calc_1.setObjectName("calc_1")
        self.calc_1.clicked.connect(self.digit_pressed)
        self.calc_8 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_8.setGeometry(QtCore.QRect(500, 180, 81, 61))
        self.calc_8.setObjectName("calc_8")
        self.calc_8.clicked.connect(self.digit_pressed)
        self.calc_5 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_5.setGeometry(QtCore.QRect(500, 250, 81, 61))
        self.calc_5.setObjectName("calc_5")
        self.calc_5.clicked.connect(self.digit_pressed)
        self.calc_2 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_2.setGeometry(QtCore.QRect(500, 320, 81, 61))
        self.calc_2.setObjectName("calc_2")
        self.calc_2.clicked.connect(self.digit_pressed)
        self.calc_9 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_9.setGeometry(QtCore.QRect(600, 180, 81, 61))
        self.calc_9.setObjectName("calc_9")
        self.calc_9.clicked.connect(self.digit_pressed)
        self.calc_6 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_6.setGeometry(QtCore.QRect(600, 250, 81, 61))
        self.calc_6.setObjectName("calc_6")
        self.calc_6.clicked.connect(self.digit_pressed)
        self.calc_3 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_3.setGeometry(QtCore.QRect(600, 320, 81, 61))
        self.calc_3.setObjectName("calc_3")
        self.calc_3.clicked.connect(self.digit_pressed)
        self.calc_0 = QtWidgets.QPushButton(self.troughfgui)
        self.calc_0.setGeometry(QtCore.QRect(700, 180, 81, 61))
        self.calc_0.setObjectName("calc_0")
        self.calc_0.clicked.connect(self.digit_pressed)
        self.fifteenmil = QtWidgets.QPushButton(self.troughfgui)
        self.fifteenmil.setGeometry(QtCore.QRect(20, 170, 331, 101))
        self.fifteenmil.setObjectName("fifteenmil")
        self.fifteenmil.clicked.connect(self.Fifteen)
        self.thirtyfour = QtWidgets.QPushButton(self.troughfgui)
        self.thirtyfour.setGeometry(QtCore.QRect(20, 280, 331, 101))
        self.thirtyfour.setObjectName("thirtyfour")
        self.thirtyfour.clicked.connect(self.Thirtyfour)
        self.calc_plus = QtWidgets.QPushButton(self.troughfgui)
        self.calc_plus.setGeometry(QtCore.QRect(700, 250, 81, 61))
        self.calc_plus.setObjectName("calc_plus")
        self.calc_plus.clicked.connect(self.additions)
        self.calc_plus.setCheckable(True)
        self.calc_enter = QtWidgets.QPushButton(self.troughfgui)
        self.calc_enter.setGeometry(QtCore.QRect(700, 320, 81, 61))
        self.calc_enter.setObjectName("calc_enter")
        self.calc_enter.clicked.connect(self.enter_pressed)
        self.label = QtWidgets.QLabel(self.troughfgui)
        self.label.setGeometry(QtCore.QRect(400, 30, 381, 81))
        self.label.setObjectName("label")
        self.clear_display = QtWidgets.QPushButton(self.troughfgui)
        self.clear_display.setGeometry(QtCore.QRect(400, 120, 381, 51))
        self.clear_display.setObjectName("clear_display")
        self.clear_display.clicked.connect(self.cleartext)
        MainWindow.setCentralWidget(self.troughfgui)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        self.menubar.setObjectName("menubar")
        self.menuTrough_Filler = QtWidgets.QMenu(self.menubar)
        self.menuTrough_Filler.setObjectName("menuTrough_Filler")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuTrough_Filler.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trough Filler"))
        self.primefluid.setText(_translate("MainWindow", "Prime Fluid"))
        self.sumtext.setText(_translate("MainWindow", "This is the Auto Trough filler GUI. Select the desired operation by clicking the \"Prime Fluid\", \"34ml\", \"15ml\",  or use the key pad to enter a desired amount."))
        self.calc_7.setText(_translate("MainWindow", "7"))
        self.calc_4.setText(_translate("MainWindow", "4"))
        self.calc_1.setText(_translate("MainWindow", "1"))
        self.calc_8.setText(_translate("MainWindow", "8"))
        self.calc_5.setText(_translate("MainWindow", "5"))
        self.calc_2.setText(_translate("MainWindow", "2"))
        self.calc_9.setText(_translate("MainWindow", "9"))
        self.calc_6.setText(_translate("MainWindow", "6"))
        self.calc_3.setText(_translate("MainWindow", "3"))
        self.calc_0.setText(_translate("MainWindow", "0"))
        self.fifteenmil.setText(_translate("MainWindow", "15mL"))
        self.thirtyfour.setText(_translate("MainWindow", "34mL"))
        self.calc_plus.setText(_translate("MainWindow", "+"))
        self.calc_enter.setText(_translate("MainWindow", "Enter"))
        self.clear_display.setText(_translate("MainWindow", "Clear Display"))
        self.menuTrough_Filler.setTitle(_translate("MainWindow", "Tro&ugh Filler"))

    def one(self):
        self.label.setText('1')
        self.number = '1'
        self.digit_pressed()
        print('you pressed 1')
        return "1"

    def two(self):
        self.number = '2'
        self.digit_pressed()
        print('you pressed 2')
        return "2"

    def primeFluid(self):
        self.label.setText('PrimedFluid')
        time.sleep(5)
        self.label.clear()
        print('priming fluid done')
        return 'PrimeFluid done'

    def Fifteen(self):
        self.label.setText('15ml')
        time.sleep(5)
        self.label.clear()
        print('15ml Done')
        return '15'

    def Thirtyfour(self):
        self.label.setText('34ml')
        time.sleep(5)
        self.label.clear()
        print('34ml done')
        return '34'


    def cleartext(self):
        self.label.clear()
        self.calc_plus.setChecked(False)
        self.userIsTypingSecondNumber = False

    def digit_pressed(self):
        # button = self.number
        button = self.MainWindow.sender()
        print(button)
        if self.calc_plus.isChecked() and (not self.userIsTypingSecondNumber):
            newLabel = format(float(button.text()), '.15g')
            self.userIsTypingSecondNumber = True
        else:
            newLabel = format(float(self.label.text() + button.text()),'.15g')
        self.label.setText(newLabel)

    def additions(self):
        self.firstNum = float(self.label.text())
        self.calc_plus.setChecked(True)

    def enter_pressed(self):

        secondNum = float(self.label.text())
        print(secondNum)

        if self.calc_plus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            t.turn_on(newLabel)
            self.calc_plus.setChecked(False)
        else:
            t.turn_on(secondNum)
            print(self.label.text())

        self.userIsTypingSecondNumber = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
