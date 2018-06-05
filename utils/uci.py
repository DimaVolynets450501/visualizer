#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup
from .project import create_folder, get_absolute_path, save_file, get_page
from .database import Database, INSERT_SCRIPT, SELECT_SCRIPT, NUM_ROWS

sys.path.append('..')
import conf.config as cfg

PARSER = 'html.parser'
UCI_FOLDER = 'resources/uci'
UCI_SOURCE_PAGE = 'uci_page.hmtl'
BASE_UCI_URL_PART = 'https://archive.ics.uci.edu/ml'
UCI_NUM_ATTRIBUTES = 6
DATABASE_FOLDER = '/database/content.db'

class UCI_page:

    def __init__(self):
        self.uci_dataset_name = []
        self.uci_datasets_urls = []
        self.uci_pictures_urs = []
        self.uci_folder_urls = []
        self.uci_attributes = [[] for i in range(UCI_NUM_ATTRIBUTES)]

    def set_page(self, page):
        self.uci_page = page

    def set_parser(self):
        self.parser = BeautifulSoup(self.uci_page, PARSER)
        
    def set_dataset_amount(self):
        datasets = self.parser.find('p', attrs={'class':'big'})
        datasets = datasets.find_next('p', attrs={'class':'big'})
        self.dataset_amount = int(datasets.b.text)
        
    def parse_datasets_table(self):        
        table = self.parser.find('table', attrs={'border':'1'})
        table_line = table.find_next('tr')
        for i in range(self.dataset_amount):
            table_line = table_line.next_sibling
            self.add_dataset_name(table_line)
            self.add_dataset_url(table_line)
            self.add_picture_url(table_line)
            self.add_dataset_attributes(table_line)

    def save_uci_page(rootpath):
        create_folder(rootpath+"/"+UCI_FOLDER)
        save_file(rootpath+"/"+UCI_FOLDER+"/"+UCI_SOURCE_PAGE)

    def save_content_to_database(self):
        database = Database(cfg.ROOT_PROJECT_PATH+DATABASE_FOLDER)
        for i in range(self.dataset_amount):
            database.execute(INSERT_SCRIPT.format(i,\
                        self.uci_dataset_name[i],\
                        self.uci_datasets_urls[i],\
                        self.uci_pictures_urs[i],\
                        self.uci_folder_urls[i],\
                        self.uci_attributes[0][i],\
                        self.uci_attributes[1][i],\
                        self.uci_attributes[2][i],\
                        self.uci_attributes[3][i],\
                        self.uci_attributes[4][i],\
                        self.uci_attributes[5][i]))
        database.save()
        database.close()

    def add_dataset_name(self, parser):
        self.uci_dataset_name.append(parser.find('b').text.replace("'"," "))
    
    def add_picture_url(self, parser):
        self.uci_pictures_urs.append(parser.find('img').get('src'))

    def add_dataset_url(self, parser):
        self.uci_datasets_urls.append(parser.find('a').get('href'))

    def add_dataset_attributes(self, parser):
        parser = parser.find_next('p', attrs={'class':'normal'})
        for i in range(UCI_NUM_ATTRIBUTES):
            parser = parser.find_next('p', attrs={'class':'normal'})
            self.uci_attributes[i].append(parser.text)

    def add_datasets_folder_urls(self):
        for dataset_url in self.uci_datasets_urls:
            # print("-------------------------------------------------------------------")
            # print(BASE_UCI_URL_PART+"/"+dataset_url)
            url = self.get_dataset_folder_url(BASE_UCI_URL_PART+"/"+dataset_url)
            # print(url)
            # print("-------------------------------------------------------------------")
            self.uci_folder_urls.append(url)

    def get_dataset_folder_url(self, dataset_url):
        page = get_page(dataset_url)
        parser = BeautifulSoup(page, PARSER)
        try:
            url = parser.find('p').find('a').get('href')
        except AttributeError:
            print("Folder URL for {} not found!".format(dataset_url))
            return ""
        return url[3:]

    def get_dataset_amount(self):
        return self.dataset_amount

    def print_parsed_table(self):
        for i in range(self.dataset_amount):
            print(self.uci_datasets_urls[i],"--",self.uci_pictures_urs[i],"--",self.uci_attributes[0][i],"--",self.uci_attributes[1][i])

    def print_folders(self):
        for url in self.uci_folder_urls:
            print(url)
