#!/usr/bin/python3

import os
import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QTableView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSlot

sys.path.append('..')
from utils.uci import BASE_UCI_URL_PART
from utils.project import download_data
from conf.config import ROOT_PROJECT_PATH

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
        self.set_table_sizes()
        self.init_table_behaviour()
        self.init_content()
        self.set_column_sizes()
        self.doubleClicked.connect(self.download_dataset)

    def set_table_sizes(self):
        self.setColumnCount(7)
        self.setRowCount(self.uci.dataset_amount)

    def init_content(self):
        for i in range(self.uci.dataset_amount):
            self.setItem(i, 0, QTableWidgetItem(self.uci.uci_dataset_name[i]))
            self.setItem(i, 1, QTableWidgetItem(self.uci.uci_attributes[0][i]))
            self.setItem(i, 2, QTableWidgetItem(self.uci.uci_attributes[1][i]))
            self.setItem(i, 3, QTableWidgetItem(self.uci.uci_attributes[2][i]))
            self.setItem(i, 4, QTableWidgetItem(self.uci.uci_attributes[3][i]))
            self.setItem(i, 5, QTableWidgetItem(self.uci.uci_attributes[4][i]))
            self.setItem(i, 6, QTableWidgetItem(self.uci.uci_attributes[5][i]))

    def init_table_behaviour(self):
        self.setHorizontalHeaderLabels(TABLE_HEADERS)
        self.setGridStyle(0)
        self.setShowGrid(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet(SELECTION_COLOR)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_column_sizes(self):
        header = self.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

    @pyqtSlot()
    def download_dataset(self):
        index = self.currentRow()
        folder_url = self.uci.uci_folder_urls[index]
        dataset_name = self.uci.uci_dataset_name[index]
        url = os.path.join(BASE_UCI_URL_PART, folder_url)
        dataset_folder = os.path.join(ROOT_PROJECT_PATH,'datasets', dataset_name)
        download_data(url, dataset_folder)
        # for currentQTableWidgetItem in self.tableWidget.selectedItems():
            # print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
