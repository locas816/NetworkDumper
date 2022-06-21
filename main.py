import sys
import os
import subprocess
import re
import time
import datetime
import pickle
import contextlib
import scapy

from scapy.all import (hexdump, AsyncSniffer, sniff, compile_filter, conf, Ether, IP, TCP,
                       UDP, ARP, ICMP, get_if_addr, rdpcap, wrpcap)

from PyQt5.QtWidgets import (QAction, QDateEdit, QDialog, QApplication, QMainWindow, QPushButton,
                             QLabel, QMessageBox, QTextEdit, QTreeWidget, QFileDialog, QTreeWidgetItem,
                             QSpinBox, QComboBox, QHBoxLayout, QLineEdit)
from PyQt5.QtCore import QTime, QTimer, Qt, pyqtSignal, QThread
from PyQt5.QtGui import QBrush, QColor, QMovie, QCursor
from PyQt5 import uic
from sqlite3 import connect
from io import StringIO

from classes.FirstWindow import FirstWindow

# the main window class
class PacketSniffer(QMainWindow):
    def __init__(self):
        super().__init__()

        # load template
        uic.loadUi("templates/MainWindow.ui", self)

        # Start first window
        self.FirstWindow = FirstWindow()
        self.FirstWindow.show()

# Run the code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = PacketSniffer()
    sys.exit(app.exec_())