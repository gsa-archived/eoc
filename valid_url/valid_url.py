import os
import csv
from urllib.request import urlopen
from urllib.error import *
import requests
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import urllib.parse
import html


def clean_xml(xml_string):
    soup = BeautifulSoup(xml_string, "lxml")
    cleaned_xml = str(soup)
    return ET.ElementTree(ET.fromstring(cleaned_xml)).getroot()

def clean_url(url):
    parsed = urllib.parse.urlsplit(url)
    safe_path = urllib.parse.quote(parsed.path, safe="/")
    safe_query = urllib.parse.quote(parsed.query, safe='&')
    safe_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, safe_path, safe_query, parsed.fragment))
    return safe_url

def check_link(locs):
    print('checking {}'.format(locs[:2]))
    fin = []
    errors = 0
    for i in locs:
        i = i.strip()
        if not i:
            continue
        #i = clean_url(i)
        try:
            html = urlopen(i)
        
        except HTTPError as e:
            print(i)
            print('HTTP error - \n{}'.format(e))
            fin.append([i,e])
            errors+=1
            continue
            
        except URLError as e:
            print(i)
            print('URL Error - \n{}'.format(e))
            fin.append([i,e])
            errors+=1
            continue

        else:
            fin.append([i,'Good'])
            continue
    print('There are {} errors'.format(errors))

def read_urls(fold_path):
    urls = []
    for file in os.listdir(fold_path):
        file_path = os.path.join(fold_path, file)
        with open(file_path, mode= 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader,None)
            for row in reader:
                urls.append(row[0].strip())
    return urls