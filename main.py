#!/usr/bin/python3
import os
from utils.uci import test_package, UCI_page
from utils.project import get_absolute_path
import conf.config as cfg
from utils.app_runner import AppRunner
from utils.database import test_database

def setup_root_path():
    cfg.ROOT_PROJECT_PATH = get_absolute_path()

if __name__ == "__main__":
    setup_root_path()
    # app = AppRunner()
    # test_urllib()
    # UCI_page.print()
    test_package()
    # test_database()
