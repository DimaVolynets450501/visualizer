#!/usr/bin/python3

import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QHBoxLayout, QMenuBar, QMainWindow
from PyQt5.QtWidgets import QAction
from .content_table import ContentTable

APP_TITLE = 'Visualizer'
CLOSE_APP_SHORTCUT = 'Ctrl+Q'

class MainWindow(QMainWindow):

    def __init__(self, uci_page):
        super().__init__()
        self.uci_page = uci_page
        self.add_menu_bar()
        self.create_content_table()
        self.window_init()

    def window_init(self):
        self.setWindowTitle(APP_TITLE)
        self.show()

    def create_content_table(self):
        self.content_table = ContentTable(self, self.uci_page)
        self.setCentralWidget(self.content_table)
        
    def add_menu_bar(self):
        self.qmenubar = QMenuBar(self)
        self.add_bar_menus()
        self.setMenuBar(self.qmenubar)

    def add_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&File')
        file_menu.addAction(self.open_file_action())
        file_menu.addAction(self.quit_app_action())

    def open_file_action(self):
        action = QAction('Open', self)
        action.setShortcut('Ctrl+O')
        action.setStatusTip('Open file with dataset')
        # action.triggered.connect(self.close)
        return action

    def quit_app_action(self):
        action = QAction('Exit', self)
        action.setShortcut('Ctrl+q')
        action.setStatusTip('Exit from visualizer')
        action.triggered.connect(self.close)
        return action
