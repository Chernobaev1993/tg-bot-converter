import requests
import lxml.html
from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    print(a.text)
