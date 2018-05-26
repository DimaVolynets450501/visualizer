#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import radviz
from pandas.tools.plotting import scatter_matrix
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

import numpy as np
# from seaborn import heatmap

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
        self.canvas.draw()
        
    def draw_histogram(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        data = data.ix[:,1:]
        transformed = pd.DataFrame(data)
        self.figure = transformed.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,xlabelsize=6, ylabelsize=6, grid=False, ax=ax)
        [x.title.set_size(6) for x in self.figure.ravel()]

    def draw_andrew_curves(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        andrews_curves(data, 'class', ax=ax)

    def draw_parallel_coordinates(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # ax.legend(loc='top left')
        ax.tick_params(labelsize='small', rotation=90)
        parallel_coordinates(data, 'class', ax=ax)

    def draw_radviz(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        radviz(data, 'class', ax=ax)

    def draw_heatmap(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        data = data = data.ix[:,1:]
        ax.pcolor(data)
        plt.yticks(np.arange(len(data.columns)), data.columns)
        plt.xticks(np.arange(len(data.columns)), data.columns)

    def draw_scatter_matrix(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        data = data.ix[:,1:]
        axs = scatter_matrix(data, alpha=0.2, figsize=(6, 6), diagonal='kde', ax=ax)
        n = len(data.columns)
        for x in range(n):
            for y in range(n):
                ax = axs[x, y]
                ax.xaxis.label.set_rotation(45)
                ax.yaxis.label.set_rotation(0)
                # ax.yaxis.labelpad = 50
                # for tick in ax.get_xticklabels():
                    # tick.set_rotation(45)

    def draw_pca(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        pca = PCA(n_components=2)
        class_ = data['class']
        # print(class_)
        data = data = data.ix[:,1:]
        transformed = pd.DataFrame(pca.fit_transform(data))
        ax.scatter(transformed[class_==1][0], transformed[class_==1][1], label='Class 1', c='red')
        ax.scatter(transformed[class_==2][0], transformed[class_==2][1], label='Class 2', c='blue')
        ax.scatter(transformed[class_==3][0], transformed[class_==3][1], label='Class 3', c='lightgreen')
        ax.legend()

    def draw_lda(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        lda = LDA(n_components=2)
        class_ = data['class']
        # print(class_)
        data = data.ix[:,1:]
        transformed = pd.DataFrame(lda.fit_transform(data, class_))
        ax.scatter(transformed[class_==1][0], transformed[class_==1][1], label='Class 1', c='red')
        ax.scatter(transformed[class_==2][0], transformed[class_==2][1], label='Class 2', c='blue')
        ax.scatter(transformed[class_==3][0], transformed[class_==3][1], label='Class 3', c='lightgreen')
        ax.legend()
