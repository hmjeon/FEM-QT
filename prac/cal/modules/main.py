# -*- coding: utf-8 -*-

import sys, ui

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

'''
from PyQt5 import uic

calUI = '../_uiFiles/calculator.ui'
'''

class MainDialog(QDialog, ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        #uic.loadUi(calUI, self)
        self.setupUi(self)

        # Initialize the editor as zero
        self.a_lineEdit.setText("0")

        # Push button events for digits
        self.num_pushButton_1.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_2.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_3.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_4.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_5.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_6.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_7.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_8.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_9.clicked.connect(self.Clicked_Buttom)
        self.num_pushButton_0.clicked.connect(self.Clicked_Buttom)

        # Push button events for signs
        self.sign_pushButton_1.clicked.connect(self.Clicked_Buttom)
        self.sign_pushButton_2.clicked.connect(self.Clicked_Buttom)
        self.sign_pushButton_3.clicked.connect(self.Clicked_Buttom)
        self.sign_pushButton_4.clicked.connect(self.Clicked_Buttom)

        # Push button events for etc
        self.p_open_pushButton.clicked.connect(self.Clicked_Buttom)
        self.p_close_pushButton.clicked.connect(self.Clicked_Buttom)
        self.dot_pushButton.clicked.connect(self.Clicked_Buttom)
        self.per_pushButton.clicked.connect(self.Clicked_Buttom)

        # Push button events for result, reset and deletion
        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

    def Clicked_Buttom(self):

        button = self.sender()

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