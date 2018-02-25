#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup, Comment
import re

def test_package():
    r = requests.get('https://archive.ics.uci.edu/ml/datasets.html')
    # print(r.status_code)
    # print(r.headers['content-type'])
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', attrs={'border':'1'})
    # print(table)
    #skip inner <tr> and first row of table
    f_table = table.find_next('tr')
    f_table = f_table.next_sibling
    print(f_table)
    print("HREF:", f_table.find('a').get('href'))
    print("SRC:", f_table.find('img').get('src'))
    print(type(f_table.find(text=lambda text:isinstance(text, Comment))))
    descr = f_table.find_next('p', attrs={'class':'normal'})
    print(descr)
    descr = descr.find_next('p', attrs={'class':'normal'})
    print(descr)
    print(descr.find_next('p', attrs={'class':'normal'}))
    f_table = f_table.find_next('tr')
    f_table = f_table.find_next('tr')
    print('///////////////////////////////////////////////')
    print(f_table)
    f_table = f_table.next_sibling
    # f_table = f_table.find_next('tr')
    # f_table = f_table.find_next('tr')
    print('///////////////////////////////////////////////')
    print(f_table)
    # print('///////////////////////////////////////////////')
    # print(f_table.find('a').get('href'))
    # print(f_table.find('img').get('src'))
    # print(f_table.find('td'))
    # print(f_table.find_next('td'))

    
    # # url = table.select('a[href^="datasets/"]')[0]
    # print(soup.select('a[href^="datasets/"]'))
    # print(soup.select('table[border~=1]')[0])
    # print(soup.find_next('table'))
    # print(soup.select('a[href^="datasets/"]'))
    # print(soup.find('a[href="datasets/"]'))
    # print(soup.find("table"))
    # parser = UCIParser()
    # parser.feed(r.text)
    
