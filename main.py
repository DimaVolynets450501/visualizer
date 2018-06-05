#!/usr/bin/python3
import os
from utils.uci import test_package, UCI_page
from utils.project import get_absolute_path, test_dataimporter
import conf.config as cfg
from utils.app_runner import AppRunner
from utils.database import test_database
from utils.visualizer import *

if __name__ == "__main__":
    app = AppRunner()
