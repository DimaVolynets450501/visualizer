#!/usr/bin/python3

import os
import sys
from PyQt5.QtWidgets import QApplication
import configparser
from .uci import *
from .project import get_page, get_absolute_path

sys.path.append('..')
from interface.main_window import MainWindow
from conf import config

APP_CONFIG = {
    "IS_DATABASE_FILLED":0,
    "ROOT_PROJECT_PATH":"",
}
RELOAD_IS_REQUIRED = 0

class AppRunner():

    def __init__(self):
        self.init_project_path()
        self.load_uci_content()
        self.reload_config()
        # app = QApplication(sys.argv)
        # window = MainWindow()
        # sys.exit(app.exec_())

    def init_project_path(self):
        global RELOAD_IS_REQUIRED
        if not config.ROOT_PROJECT_PATH:
            config.ROOT_PROJECT_PATH = get_absolute_path()
            APP_CONFIG['ROOT_PROJECT_PATH'] = '"'+config.ROOT_PROJECT_PATH+'"'
            RELOAD_IS_REQUIRED = 1

    def load_uci_content(self):
        global RELOAD_IS_REQUIRED
        if config.IS_DATABASE_FILLED == 0:
            self.init_uci_page()
            self.parse_content_for_page()
            self.uci_page.save_content_to_database()
            config.IS_DATABASE_FILLED = 1
            APP_CONFIG['IS_DATABASE_FILLED'] = 1
            RELOAD_IS_REQUIRED = 1
        else:
            #TODO read from db if it's initialized
            self.init_uci_page()

    def reload_config(self):
        if RELOAD_IS_REQUIRED:
            filename = os.path.join(config.ROOT_PROJECT_PATH,'conf/config.py')
            print(filename)
            self.write_config(filename, APP_CONFIG)
            
    def init_uci_page(self):
        url = os.path.join(BASE_UCI_URL_PART,'datasets.html')
        self.uci_page = UCI_page()
        self.uci_page.set_page(get_page(url))
        self.uci_page.set_parser()
        self.uci_page.set_dataset_amount()

    def parse_content_for_page(self):
        self.uci_page.parse_datasets_table()
        self.uci_page.add_datasets_folder_urls()
        # self.write_config("/home/diman/study/visualizer/conf/config.py", APP_CONFIG)
            
    def write_config(self, filename, opts):
        with open(filename, 'w') as f:
            for k,v in opts.items():
                f.write("{}={}\n".format(k, v))
