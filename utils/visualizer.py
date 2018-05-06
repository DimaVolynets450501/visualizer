#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import radviz

cols =  ['Class', 'Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 
         'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 
         'Hue', 'OD280/OD315', 'Proline']
data = pd.read_csv('/home/diman/study/visualizer/datasets/Wine/wine.data', names=cols)
y = data['Class']
X = data.ix[:, 'Alcohol':]
X_norm = (X - X.min())/(X.max() - X.min())

def two_dm_plot():
    plt.scatter(X[y==1]['Flavanoids'], X[y==1]['NonflavanoidPhenols'], label='Class 1', c='red')
    plt.scatter(X[y==2]['Flavanoids'], X[y==2]['NonflavanoidPhenols'], label='Class 2', c='blue')
    plt.scatter(X[y==3]['Flavanoids'], X[y==3]['NonflavanoidPhenols'], label='Class 3', c='lightgreen')

    # Prettify the graph
    plt.legend()
    plt.xlabel('Flavanoids')
    plt.ylabel('NonflavanoidPhenols')

    # display
    plt.show()

def pca_plot():
    
    pca = PCA(n_components=3) #2-dimensional PCA
    transformed = pd.DataFrame(pca.fit_transform(X_norm))
    plt.scatter(transformed[0], transformed[1])
    plt.scatter(transformed[y==2][0], transformed[y==2][1], label='Class 2', c='blue')
    plt.scatter(transformed[y==3][0], transformed[y==3][1], label='Class 3', c='lightgreen')
    
    plt.legend()
    plt.show()

def parallel_plot():
    plt_feat =  ['Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 
         'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 
         'Hue', 'OD280/OD315', 'Proline']
    plt_feat1 =  ['MalicAcid', 'Ash', 'OD280/OD315', 'Magnesium','TotalPhenols']
    data_norm = pd.concat([X_norm[plt_feat1], y], axis=1)
    data2 = pd.concat([X[plt_feat1], y], axis=1)
    # Perform parallel coordinate plot
    parallel_coordinates(data_norm, 'Class')
    # parallel_coordinates(data_norm, 'Class')
    plt.show()

def andrew_curves():
    plt_feat =  ['Alcohol', 'MalicAcid', 'Ash', 'AlcalinityOfAsh', 'Magnesium', 'TotalPhenols', 
                 'Flavanoids', 'NonflavanoidPhenols', 'Proanthocyanins', 'ColorIntensity', 
                 'Hue', 'OD280/OD315', 'Proline']
    plt_feat1 =  ['MalicAcid', 'Ash', 'OD280/OD315', 'Magnesium','TotalPhenols']
    data_norm = pd.concat([X_norm[plt_feat1], y], axis=1)
    andrews_curves(data, 'Class')
    plt.show()

def pd_hist():
    data = pd.read_csv('/home/diman/study/visualizer/datasets/Wine/wine.data', names=cols)
    y = data['Class']
    X = data.ix[:, 'Alcohol':]
    X_norm = (X - X.min())/(X.max() - X.min())

    transformed = pd.DataFrame(X)
    return transformed.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,xlabelsize=8, ylabelsize=8, grid=False)
