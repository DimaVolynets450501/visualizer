#!/usr/bin/python3
import os
import re
import urllib.request as request
from threading import Thread

DEFAULT_NUM_THREADS = 10 
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
        
        
