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

        self.num_pushButton_1.clicked.connect(self.Click_Num_1)

        self.pushButton_ok.clicked.connect(self.Click_Ok)

    def Click_Num_1(self):
        str_editor_= self.str_lineEdit.text()
        str_button = self.num_pushButton_1.text()
        self.str_lineEdit.setText(str_editor_ + str_button)

    def Click_Ok(self):
        exit()

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()