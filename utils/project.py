#!/usr/bin/python3
import os
import re
import csv
import numpy
import pandas as pd
import urllib.request as request
import socket
from threading import Thread
from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox

URL_PATTERN = 'href="(?!Index)[\w|\-|\.]*"'
REMOTE_SERVER = "www.google.com"

DATASETS_FOLDER = '/home/diman/study/visualizer/datasets'
QMETHOD = 'QFileDialog.getOpenFileName()'
FILE_PATTERN = 'Data files (*.data);;Csv files (*.csv)'
APP_INFORMATION = 'Import dataset message'

def internet_on():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def get_absolute_path():
    return os.getcwd()

def create_folder(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_file(filepath, content):
    with open(filepath,"w") as f:
        f.write(content)

def read_file(filepath):
    with open(filepath,"r") as f:
        return f.read()

def file_is_exists(filename):
    return os.path.isfile(filename)

def get_page(url):
    r = request.urlopen(url)
    page = r.read().decode('iso-8859-1')
    return page

def import_dataset_action():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename,_ = QFileDialog.getOpenFileName(None, QMETHOD,\
            DATASETS_FOLDER, FILE_PATTERN, options=options)
    return filename

def information_dialod(message):
    QMessageBox.information(None, APP_INFORMATION, message, QMessageBox.Ok )

def information_download_dialod(message):
    return QMessageBox.information(None, APP_INFORMATION, message, QMessageBox.Ok|QMessageBox.No )

def info_import_dataset_dialog(message):
    msg_box = QMessageBox(QMessageBox.Information,APP_INFORMATION, message)
    ok_btn = msg_box.addButton("OK", QMessageBox.AcceptRole)
    show_btn = msg_box.addButton("Show Dataset", QMessageBox.AcceptRole)
    msg_box.exec_()

    if msg_box.clickedButton() == show_btn:
        return True
    else:
        return False

def custom_info__dialog( message):
    msg_box = QMessageBox(QMessageBox.Information, APP_INFORMATION, message)
    ok_btn = msg_box.addButton("OK", QMessageBox.AcceptRole)
    show_btn = msg_box.addButton("Show Dataset", QMessageBox.AcceptRole)
    msg_box.exec_()

    if msg_box.clickedButton() == show_btn:
        msg_box.close()

def download_data(url, folder):
    data = request.urlopen(url)
    response = data.read()
    response = response.decode('utf-8')
    
    for filename in re.findall(URL_PATTERN, response):        
        file_url = os.path.join(url, filename[6:-1])
        file_in_folder = os.path.join(folder, filename[6:-1])
        try:
            os.stat(folder)
        except:
            os.mkdir(folder)
        request.urlretrieve(file_url, file_in_folder)
        print(filename[6:-1])

class ColumnImporter():
    def __init__(self, filename):
        with open(filename) as f:
            content = f.readlines()
        self.cols = [x.strip() for x in content]
        
    def get_columns(self):
        return self.cols
    
class DatasetImporter():
    def __init__(self, filename, cols):
        self.data = pd.read_csv(filename, names=cols)

    def get_dataset(self):
        return self.data

class Normalization():
    def __init__(self, data_):
        self.class_ = data_['class']
        self.data = data_.ix[:,1:]

    def normilize_by_max_value(self):
        tmp = self.data
        self.data = tmp / tmp.max()

    def normilize_by_min_value(self):
        tmp = self.data
        self.data = tmp / tmp.min()

    def normilize_by_mean_value(self):
        tmp = self.data
        self.data = tmp / tmp.mean()

    def normilize_by_minimax(self):
        tmp = self.data
        self.data = (tmp - tmp.min())/(tmp.max() - tmp.min())

    def mean_normilization(self):
        tmp = self.data
        self.data = (tmp - tmp.mean())/(tmp.max() - tmp.min())

    def get_normilized_data(self):
        return pd.concat([self.class_, self.data], axis=1)

class AttributeChooser(QDialog):
    def __init__(self, cols_, parent):
        super(AttributeChooser, self).__init__(parent)
        self.cols = cols_
        self.init_ui(self.create_checkbox_list())

    def create_checkbox_list(self):
        self.model = QStandardItemModel()
        for col in self.cols:                   
            item = QStandardItem(col)
            item.setCheckable(True)
            self.model.appendRow(item)
        return self.model

    def init_ui(self, model):
        layout = QVBoxLayout()
        view = QListView(self)
        view.setModel(model)
        button = QPushButton("Ok")
        button.clicked.connect(self.set_new_cols)
        layout.addWidget(view)
        layout.addWidget(button)
        self.setLayout(layout)

    def set_new_cols(self):
        i = 0
        choosed_cols = ['class']
        while self.model.item(i):
            if self.model.item(i).checkState():
                choosed_cols.append(self.cols[i])
            i += 1
        self.cols = choosed_cols
        self.close()

    def get_data(self):
        self.exec_()
        return self.cols
