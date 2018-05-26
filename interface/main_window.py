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
from utils.project import Normalization as Norm

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
        self.add_normilization_bar_menus()
        self.setMenuBar(self.qmenubar)

    def add_file_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&File')
        file_menu.addAction(self.open_file_action())
        file_menu.addAction(self.quit_app_action())
        file_menu.addAction(self.open_dataset_action())

    def add_visualizer_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&Visualizer')
        file_menu.addAction(self.histogram_plot_action())
        file_menu.addAction(self.andrew_plot_action())
        file_menu.addAction(self.parallel_plot_action())
        file_menu.addAction(self.radviz_plot_action())
        file_menu.addAction(self.heatmap_plot_action())
        file_menu.addAction(self.scatter_matrix_plot_action())
        file_menu.addAction(self.pca_plot_action())
        file_menu.addAction(self.lda_plot_action())

    def add_normilization_bar_menus(self):
        file_menu = self.qmenubar.addMenu('&Normilization')
        file_menu.addAction(self.norm_by_max_action())
        file_menu.addAction(self.norm_by_min_action())
        file_menu.addAction(self.norm_by_mean_action())
        file_menu.addAction(self.norm_by_minimax_action())
        file_menu.addAction(self.mean_norm_action())
        
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
            self.bak_data = self.dataset_data
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
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_andrew_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_andrew_curves(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_parallel_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_parallel_coordinates(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_radviz_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_radviz(self.dataset_data)
        cur_widget = self.central_widget.currentWidget()
        self.dataset_data = self.bak_data
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_heatmap_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_heatmap(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_scatter_matrix_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_scatter_matrix(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)

    def handle_pca_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_pca(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
        self.central_widget.addWidget(self.plot_window)
        self.central_widget.setCurrentWidget(self.plot_window)
        
    def handle_lda_plot_action(self):
        self.plot_window = PlotWindow()
        self.plot_window.draw_lda(self.dataset_data)
        self.dataset_data = self.bak_data
        cur_widget = self.central_widget.currentWidget()
        if cur_widget != self.content_table:
            self.central_widget.removeWidget(cur_widget)
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

    def andrew_plot_action(self):
        action = QAction("Plot Andrew's Curves", self)
        action.triggered.connect(self.handle_andrew_plot_action)
        return action

    def parallel_plot_action(self):
        action = QAction("Plot Parallel Coordinates", self)
        action.triggered.connect(self.handle_parallel_plot_action)
        return action

    def radviz_plot_action(self):
        action = QAction("Plot Radviz", self)
        action.triggered.connect(self.handle_radviz_plot_action)
        return action

    def heatmap_plot_action(self):
        action = QAction("Plot Heatmap", self)
        action.triggered.connect(self.handle_heatmap_plot_action)
        return action

    def scatter_matrix_plot_action(self):
        action = QAction("Plot Scatter Matrix", self)
        action.triggered.connect(self.handle_scatter_matrix_plot_action)
        return action

    def pca_plot_action(self):
        action = QAction("Plot PCA", self)
        action.triggered.connect(self.handle_pca_plot_action)
        return action

    def lda_plot_action(self):
        action = QAction("Plot LDA", self)
        action.triggered.connect(self.handle_lda_plot_action)
        return action
    
    def norm_by_max_action(self):
        action = QAction('Normilize data by max value', self)
        action.triggered.connect(self.handle_norm_by_max_action)
        return action

    def norm_by_min_action(self):
        action = QAction('Normilize data by min value', self)
        action.triggered.connect(self.handle_norm_by_min_action)
        return action

    def norm_by_mean_action(self):
        action = QAction('Normilize data by mean value', self)
        action.triggered.connect(self.handle_norm_by_mean_action)
        return action

    def norm_by_minimax_action(self):
        action = QAction('Normilize data by minimax method', self)
        action.triggered.connect(self.handle_norm_by_minimax_action)
        return action
    
    def mean_norm_action(self):
        action = QAction('Normilize data by mean method', self)
        action.triggered.connect(self.handle_norm_mean_action)
        return action
    
    def change_central_widget_event(self):
        shortcut = QShortcut(QKeySequence("Ctrl+n"), self)
        shortcut.activated.connect(self.handle_central_widget)

    def handle_norm_by_max_action(self):
        norm_data = Norm(self.dataset_data)
        norm_data.normilize_by_max_value()
        self.dataset_data = norm_data.get_normilized_data()

    def handle_norm_by_min_action(self):
        norm_data = Norm(self.dataset_data)
        norm_data.normilize_by_min_value()
        self.dataset_data = norm_data.get_normilized_data()

    def handle_norm_by_mean_action(self):
        norm_data = Norm(self.dataset_data)
        norm_data.normilize_by_mean_value()
        self.dataset_data = norm_data.get_normilized_data()

    def handle_norm_by_minimax_action(self):
        norm_data = Norm(self.dataset_data)
        norm_data.normilize_by_minimax()
        self.dataset_data = norm_data.get_normilized_data()

    def handle_norm_mean_action(self):
        norm_data = Norm(self.dataset_data)
        norm_data.mean_normilization()
        self.dataset_data = norm_data.get_normilized_data()
        
    def handle_central_widget(self):
        cur_widget = self.central_widget.currentWidget()
        self.central_widget.removeWidget(cur_widget)
        self.central_widget.setCurrentWidget(self.content_table)
