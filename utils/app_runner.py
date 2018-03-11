#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication

sys.path.append('..')
from interface.main_window import MainWindow

class AppRunner():

    def __init__(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
