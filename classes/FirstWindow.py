import sys

from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QPushButton, QComboBox, QLineEdit, QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from scapy.all import get_if_list, compile_filter

import re
import os

class FirstWindow(QWidget):

    def __init__(self):
        super().__init__()

        # load template
        uic.loadUi("templates/FirstWindow.ui", self)

