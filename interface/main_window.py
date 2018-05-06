#!/usr/bin/python3

import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QHBoxLayout, QMenuBar, QMainWindow
from PyQt5.QtWidgets import QAction,  QStackedWidget, QTableView
from .content_table import ContentTable
from .gui_actions import import_dataset_action, information_dialod, info_import_dataset_dialog
from .minor_window import PlotWindow

sys.path.append('..')
from utils.project import file_is_exists, ColumnImporter, DatasetImporter
from utils.pandas_model import PandasModel

APP_TITLE = 'Visualizer'
CLOSE_APP_SHORTCUT = 'Ctrl+Q'
NOT_SUCCESS_IMPORT_MESSAGE = 'You should create col_name.txt for importing this dataset'
SUCCESS_IMPORT_MESSAGE = 'Dataset was import successfully'
# TODO change hardcoded path
DATASET_COLUMN_FILE = '/home/diman/study/visualizer/datasets/Wine/column_names.txt'

class MainWindow(QMainWindow):

    def __init__(self, uci_page):
        super().__init__()
        self.uci_page = uci_page
        self.add_menu_bar()
        self.create_content_table()
        self.window_init()
        self.change_central_widget_event()

    def window_init(self):
        self.setWindowTitle(APP_TITLE)
        self.show()

    def create_content_table(self):
        self.content_table = ContentTable(self, self.uci_page)
        self.central_widget = QStackedWidget()
        self.central_widget.addWidget(self.content_table)
        self.central_widget.setCurrentWidget(self.content_table)
        self.setCentralWidget(self.central_widget)
        
    def add_menu_bar(self):
        self.qmenubar = QMenuBar(self)
        self.add_file_bar_menus()
        self.add_visualizer_bar_menus()
        self.setMenuBar(self.qmenubar)

    def add_file_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&File')
        file_menu.addAction(self.open_file_action())
        file_menu.addAction(self.quit_app_action())
        file_menu.addAction(self.open_dataset_action())

    def add_visualizer_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&Visualizer')
        file_menu.addAction(self.histogram_plot_action())
        # file_menu.addAction(self.quit_app_action())
        # file_menu.addAction(self.open_dataset_action())

    def set_dataset_file(self, filename):
        self.dataset_file = filename
        print(self.dataset_file)
        
    def handle_open_dataset_action(self):
        self.set_dataset_file(import_dataset_action())
        if not file_is_exists(DATASET_COLUMN_FILE):
            information_dialod(NOT_SUCCESS_IMPORT_MESSAGE)
        else:
            self.dataset_cols = ColumnImporter(DATASET_COLUMN_FILE).get_columns()
            dataset_importer = DatasetImporter(self.dataset_file, self.dataset_cols)
            self.dataset_data = dataset_importer.get_dataset()
            if info_import_dataset_dialog(SUCCESS_IMPORT_MESSAGE):
                self.show_pandas_table()

    def show_pandas_table(self):
        pd_table = QTableView()
        model = PandasModel(self.dataset_data)
        pd_table.setModel(model)
        self.central_widget.addWidget(pd_table)
        self.central_widget.setCurrentWidget(pd_table)
        
    def handle_hist_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_histogram(self.dataset_data)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)
        
    def open_file_action(self):
        action = QAction('Open', self)
        action.setShortcut('Ctrl+O')
        action.setStatusTip('Open file with dataset')
        action.triggered.connect(self.close)
        return action

    def quit_app_action(self):
        action = QAction('Exit', self)
        action.setShortcut('Ctrl+q')
        action.setStatusTip('Exit from visualizer')
        action.triggered.connect(self.close)
        return action

    def open_dataset_action(self):
        action = QAction('Import dataset', self)
        action.setShortcut('Ctrl+I')
        action.setStatusTip('Import dataset from folder with it')
        action.triggered.connect(lambda state: self.handle_open_dataset_action())
        return action

    def histogram_plot_action(self):
        action = QAction('Plot Histogram', self)
        action.triggered.connect(self.handle_hist_plot_action)
        return action

    def change_central_widget_event(self):
        shortcut = QShortcut(QKeySequence("Ctrl+n"), self)
        shortcut.activated.connect(self.handle_central_widget)

    def handle_central_widget(self):
        cur_widget = self.central_widget.currentWidget()
        self.central_widget.removeWidget(cur_widget)
        self.central_widget.setCurrentWidget(self.content_table)
