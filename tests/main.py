#!/usr/bin/python3

import unittest
import sys

sys.path.append('..')
from utils.database import *
from utils.project import get_page, ColumnImporter
from utils.uci import *
import conf.config as cfg

CURRENT_DATASET_AMOUNT = 436
DATASET_COLUMN_FILE = '/home/diman/study/visualizer/datasets/Wine/column_names.txt'
cols = [ 'class',
         'Alcohol',
         'Malic acid',
         'Ash',
         'Alcalinity of ash',
         'Magnesium',
         'Total phenols',
         'Flavanoids',
         'Nonflavanoid phenols',
         'Proanthocyanins',
         'Color intensity',
         'Hue',
         'OD280/OD315 of diluted wines',
         'Proline']

class TestVisualizer(unittest.TestCase):

    def test_amount_uci_page(self):
            r = get_page('https://archive.ics.uci.edu/ml/datasets.html')
            uci_page = UCI_page()
            uci_page.set_page(r)
            uci_page.set_parser()
            uci_page.set_dataset_amount()
            self.assertEqual(CURRENT_DATASET_AMOUNT, uci_page.dataset_amount)

    def test_column_importer(self):
        cols_ = ColumnImporter(DATASET_COLUMN_FILE).get_columns()
        self.assertEqual(cols, cols_)

    def test_database(self):
        db = Database(cfg.ROOT_PROJECT_PATH + "/database/content.db")
        num_rows = db.execute(NUM_ROWS).fetchone()
        self.assertEqual(CURRENT_DATASET_AMOUNT, num_rows[0])

if __name__ == '__main__':
    unittest.main()
