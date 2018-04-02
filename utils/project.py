#!/usr/bin/python3
import os
import re
import csv
import numpy
import pandas as pd
import urllib.request as request
from threading import Thread

# DEFAULT_NUM_THREADS = 10 
URL_PATTERN = 'href="(?!Index)[\w|\-|\.]*"'

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

def get_page(url):
    r = request.urlopen(url)
    page = r.read().decode('iso-8859-1')
    return page
    
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

class DatasetImporter():

    def __init__(self, filename):
        print(os.path.splitext(filename))
        self.parse_data_from_txt(filename)

    def parse_data_from_txt(self, filename):
        f = open(filename,"r")
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        self.data = list(reader)

    def get_np_data(self):
        return numpy.array(self.data).astype('float')

def test_dataimporter():
    data_importer = DatasetImporter('/home/diman/study/visualizer/datasets/Wine/wine.data')
    print(X)
    # print(data_importer.get_np_data())

# def test_urllib():
#     data = urllib.request.urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/')
#     response = data.read()
#     response = response.decode('utf-8')
#     for filename in re.findall(URL_PATTERN, response):
#         print(filename[6:-1])
    
# class MultithreaderDownloader():

#     def __init__():
        
#     def calculate_interations(num_files):
#         self.steps = num_files // DEFAULT_NUM_THREADS
#         self.last_step = num_files - (self.steps * DEFAULT_NUM_THREADS)

#     def run_threads():
#         for step in range(self.steps):
#             for num in range(DEFAULT_NUM_THREADS):
#                 thread = Thread(target=worker, args=(counter,))
#                 thread.start()
#                 thread_list.append(thread)

#             for thread in thread_list:
#                 thread.join()

#     def worker():
        
        
