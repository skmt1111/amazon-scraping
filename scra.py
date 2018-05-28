import requests
from bs4 import BeautifulSoup
import csv
import re
from time import sleep

def get_books_name(num):
    url = <URL> + str(num)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for title in soup.body.find_all(href=re.compile("http://www.amazon.co.jp")):
        if title.text != "" and title.text != "Amazon.co.jpで詳細を見る":
            with open('books2.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(title)

for i in range(249):
    i += 1
    get_books_name(i)
    sleep(2)
