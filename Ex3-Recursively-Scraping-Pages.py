#Exercise Page=https://scrapingclub.com/exercise/list_basic/
import requests
from bs4 import BeautifulSoup

base_url="https://scrapingclub.com/exercise/list_basic/"

def singlePage(url):
    r=requests.get(base_url)
    data=r.text
    soup=BeautifulSoup(data,'lxml')
    items=soup.find_all("div",class_="col-lg-4 col-md-6 mb-4")
    for i in items:
        i=i.find("div",class_="card-body")
        print("Item Name: {}Item Price: {}".format(i.h4.text.lstrip('\n'),i.h5.text))

#get links to all product pages
r=requests.get(base_url)
soup=BeautifulSoup(r.text,'lxml')
pages=soup.find_all("a",class_="page-link")
pagelist=[]
for p in pages:
    isvalid=p.text if p.text.isdigit() else None
    if isvalid:
        pagelist.append(p.get('href'))

#loop through all pages
for i in pagelist:
    url=base_url+i
    singlePage(base_url)