#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox


# TODO change hardcoded path
DATASETS_FOLDER = '/home/diman/study/visualizer/datasets'
QMETHOD = 'QFileDialog.getOpenFileName()'
FILE_PATTERN = 'Data files (*.data);;Csv files (*.csv)'
APP_INFORMATION = 'Import dataset message'

def import_dataset_action():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename,_ = QFileDialog.getOpenFileName(None, QMETHOD,\
            DATASETS_FOLDER, FILE_PATTERN, options=options)
    return filename

def information_dialod(message):
    QMessageBox.information(None, APP_INFORMATION, message, QMessageBox.Ok )
