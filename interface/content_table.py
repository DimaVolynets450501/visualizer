#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QTableView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt

TABLE_HEADERS = ["Name",
                 "Data Types",
                 "Default Task",
                 "Attribute Types",
                 "Instances",
                 "Attributes",
                 "Year"]

SELECTION_COLOR = "QTableWidget::item:selected{ background-color: rgba(150,200,255,170);}"

class ContentTable(QTableWidget):

    def __init__(self, parent, uci_page):
        super().__init__(parent)
        self.uci = uci_page
        self.setColumnCount(7)
        self.setRowCount(self.uci.dataset_amount)
        self.setHorizontalHeaderLabels(TABLE_HEADERS)
        self.init_content()
        self.setGridStyle(0)
        self.setShowGrid(False)
        self.set_sections_sizes()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(SELECTION_COLOR)

    def init_content(self):
        for i in range(self.uci.dataset_amount):
            self.setItem(i, 0, QTableWidgetItem(self.uci.uci_dataset_name[i]))
            self.setItem(i, 1, QTableWidgetItem(self.uci.uci_attributes[0][i]))
            self.setItem(i, 2, QTableWidgetItem(self.uci.uci_attributes[1][i]))
            self.setItem(i, 3, QTableWidgetItem(self.uci.uci_attributes[2][i]))
            self.setItem(i, 4, QTableWidgetItem(self.uci.uci_attributes[3][i]))
            self.setItem(i, 5, QTableWidgetItem(self.uci.uci_attributes[4][i]))
            self.setItem(i, 6, QTableWidgetItem(self.uci.uci_attributes[5][i]))

    def set_sections_sizes(self):
        header = self.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
