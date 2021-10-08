# parser.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sookmyungproject.settings")

import django
django.setup()

from mainapp.models import Notice

def parse_blog():
    req = requests.get('http://www.sookmyung.ac.kr/sookmyungkr/1288/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGc29va215dW5na3IlMkY2NiUyRmFydGNsTGlzdC5kbyUzRnBhZ2UlM0QxJTI2cm93JTNENTAlMjZzcmNoQ29sdW1uJTNEc2olMjZzcmNoV3JkJTNEJTI2YmJzQ2xTZXElM0Q1OCUyNmJic09wZW5XcmRTZXElM0QlMjZyZ3NCZ25kZVN0ciUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2aXNWaWV3TWluZSUzRGZhbHNlJTI2')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.find_all('a', attrs={'class':'artclLinkView'})
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        l_edit = "http://www.sookmyung.ac.kr/"+l
        Notice(title=t, link=l_edit).save()