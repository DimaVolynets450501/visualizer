#!/usr/bin/python3
import os

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
