#!/usr/bin/python3
import os
from utils.uci import test_package, UCI_page
from utils.project import get_absolute_path
import conf.config as cfg

def setup_root_path():
    cfg.ROOT_PROJECT_PATH = get_absolute_path()

if __name__ == "__main__":
    setup_root_path()
    # UCI_page.print()
    test_package()
