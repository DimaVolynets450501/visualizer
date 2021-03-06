#!/usr/bin/python3
import sys
import sqlite3

sys.path.append('..')
import conf.config as cfg

"""
uci_content table
--------------------------------------
sqlite> create table uci_content (
   ...> content_id integer PRIMARY KEY,
   ...> dataset_name text,
   ...> dataset_url text,
   ...> picture_url text,
   ...> folder_url text,
   ...> data_type text,
   ...> task text,
   ...> attribute_types text,
   ...> instances integer,
   ...> attributes integer,
   ...> year integer
   ...> );
--------------------------------------
"""

DATABASE_PATH = cfg.ROOT_PROJECT_PATH + "/database/content.db"
TABLE_NAME = 'uci_content'
INSERT_SCRIPT = "INSERT OR IGNORE INTO uci_content (content_id,"\
                                         "dataset_name,"\
                                         "dataset_url,"\
                                         "picture_url,"\
                                         "folder_url,"\
                                         "data_type,"\
                                         "task,"\
                                         "attribute_types,"\
                                         "instances,"\
                                         "attributes,year) "\
                 "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"

SELECT_SCRIPT = "SELECT {} FROM uci_content;"
NUM_ROWS = "SELECT COALESCE(MAX(content_id)+1, 0) FROM uci_content ;"

class Database:

    def __init__(self, path_to_db, with_row_factory=False):
        self.connection = sqlite3.connect(path_to_db)
        if with_row_factory == True:
            self.connection.row_factory = lambda cursor, row: row[0]
        self.db_cursor = self.connection.cursor()

    def execute(self, script):
        return self.db_cursor.execute(script)

    def save(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

def test_database():
    print(cfg.ROOT_PROJECT_PATH + "/database/content.db")
    db = Database(cfg.ROOT_PROJECT_PATH + "/database/content.db")
    result = db.execute('SELECT * FROM uci_content')
    print(result.fetchall())
