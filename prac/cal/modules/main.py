# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5 import uic

calUI = '../_uiFiles/calculator.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(calUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.Clicked_Buttom(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.Clicked_Buttom(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.Clicked_Buttom(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.Clicked_Buttom(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.Clicked_Buttom(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.Clicked_Buttom(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.Clicked_Buttom(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.Clicked_Buttom(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.Clicked_Buttom(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button = self.num_pushButton_0 : self.Clicked_Buttom(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button = self.sign_pushButton_1 : self.Clicked_Buttom(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button = self.sign_pushButton_2 : self.Clicked_Buttom(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button = self.sign_pushButton_3 : self.Clicked_Buttom(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button = self.sign_pushButton_4 : self.Clicked_Buttom(state, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

        self.p_open_pushButton.clicked.connect(lambda state, button=self.p_open_pushButton: self.Clicked_Buttom(state, button))
        self.p_close_pushButton.clicked.connect(lambda state, button=self.p_close_pushButton: self.Clicked_Buttom(state, button))
        self.dot_pushButton.clicked.connect(lambda state, button=self.dot_pushButton: self.Clicked_Buttom(state, button))
        self.per_pushButton.clicked.connect(lambda state, button=self.per_pushButton: self.Clicked_Buttom(state, button))

    def Clicked_Buttom(self, state, button):
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()

        exist_line_text = self.q_lineEdit.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            pass

    def Reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText("0")

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()