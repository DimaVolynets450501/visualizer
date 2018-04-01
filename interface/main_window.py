#!/usr/bin/python3

import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QHBoxLayout
from .content_table import ContentTable

APP_TITLE = 'Visualizer'
CLOSE_APP_SHORTCUT = 'Ctrl+Q'

class MainWindow(QWidget):

    def __init__(self, uci_page):
        super().__init__()
        self.uci_page = uci_page
        self.set_close_event()
        self.create_content_table()
        self.window_init()

    def window_init(self):
        self.setWindowTitle(APP_TITLE)
        # self.setGeometry(10, 10, 640, 480)
        self.show()

    def create_content_table(self):
        hlayout = QHBoxLayout()
        self.content_table = ContentTable(self, self.uci_page)
        hlayout.addWidget(self.content_table)
        self.setLayout(hlayout)
        
    def set_close_event(self):
        shortcut = QShortcut(QKeySequence("Ctrl+q"), self)
        shortcut.activated.connect(self.close)
