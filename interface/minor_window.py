#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import radviz

import sys
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

sys.path.append('..')
from utils.visualizer import pd_hist

class PlotWindow(QDialog):
    def __init__(self):
        super(PlotWindow, self).__init__()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def draw_histogram(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        y = data['class']
        X = data.ix[:, 'Alcohol':]
        X_norm = (X - X.min())/(X.max() - X.min())
        self.transformed = pd.DataFrame(X)
        ax = self.transformed.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,xlabelsize=8, ylabelsize=8, grid=False)
        # # self.figure.plot()
        # plt.plot()
        self.canvas.draw()
        
