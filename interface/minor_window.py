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

colors_list = ['red',
          'purple',
          'lightgreen',
          'mediumblue',
          'pink',
          'red',
          'red',
          'red',
          'red',
          'red',
          'red']

import numpy as np
from seaborn import heatmap
from seaborn import pairplot

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
        # self.show()
        
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
        data = data.ix[:,1:]
        corr = data.corr()
        heatmap(corr, xticklabels=data.columns, yticklabels=data.columns, ax=ax, cmap="Reds")

    def draw_scatter_matrix(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        class_ = data['class']
        data = data.ix[:,1:]
        colors = list()
        palette = {1: "red", 2: "green", 3: "blue"}
        #
        for row in class_: colors.append(palette[row])
        # colors = class_.map(lambda x: color_wheel.get(x + 1))
        axs = scatter_matrix(data, c=colors ,alpha=0.6 ,figsize=(6, 6), diagonal='kde', ax=ax)
        n = len(data.columns)
        for x in range(n):
            for y in range(n):
                ax = axs[x, y]
                ax.xaxis.label.set_rotation(90)
                ax.yaxis.label.set_rotation(0)
                ax.yaxis.labelpad = 50

    def draw_pca(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        pca = PCA(n_components=2)
        class_ = data['class']
        classes = class_.drop_duplicates().tolist()
        data = data = data.ix[:,1:]
        transformed = pd.DataFrame(pca.fit_transform(data))
        for cl in classes:
            ax.scatter(transformed[class_==cl][0], transformed[class_==cl][1],\
                       label='Class {}'.format(cl), c=colors_list[cl])
        ax.legend()

    def draw_lda(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        lda = LDA(n_components=2)
        class_ = data['class']
        classes = class_.drop_duplicates().tolist()
        data = data.ix[:,1:]
        transformed = pd.DataFrame(lda.fit_transform(data, class_))
        for cl in classes:
            ax.scatter(transformed[class_==cl][0], transformed[class_==cl][1],\
                       label='Class {}'.format(cl), c=colors_list[cl])
        ax.legend()
