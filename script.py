from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

url = "https://news.ycombinator.com"

csv_file = open('hackernews', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'link'])

def extract():
  all = soup.findAll("tr", class_="athing")
  for data in all:
    try:
      headline = data.find("a", class_="storylink").text
    except:
      headline = None
    try:
      link = data.find("a", class_="storylink")['href']
    except:
      link = None

    csv_writer.writerow([headline,link])

#how many pages to exctract
_num = 4 #<----------
for n in range(1,_num):
  r=requests.get(url + "/news?p=%s"%(n))
  soup = BeautifulSoup(r.content, "html.parser")
  extract()
  sleep(3)

csv_file.close()
