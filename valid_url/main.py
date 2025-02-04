from valid_url import check_link, read_urls
from xml.dom.minidom import parseString
from xml.dom.minidom import parse
import requests
from csv import writer
import os
import csv


links = []

path = 'path_csvs'
files = []

urls = read_urls(path)

links = check_link(urls)

with open('broken_links.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(links)
    f_object.close()