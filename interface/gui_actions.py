#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox


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

def information_download_dialod(message):
    return QMessageBox.information(None, APP_INFORMATION, message, QMessageBox.Ok|QMessageBox.No )
    # msg_box.show()
    

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
