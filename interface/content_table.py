#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QTableWidget

class ContentTable(QTableWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.setColumnCount(3)
        self.setRowCount(3)
        self.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
