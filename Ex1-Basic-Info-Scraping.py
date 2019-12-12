#Exercise Page=https://scrapingclub.com/exercise/detail_basic/
import requests
from bs4 import BeautifulSoup

url="https://scrapingclub.com/exercise/detail_basic/"

r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

itemInfo=soup.find("div",class_="card-body")
itemName=itemInfo.h3.text
itemPrice=itemInfo.h4.text
itemDescription=itemInfo.p.text 

print("Item Name: {} \nItem Price: {}\nItem Description: {}".format(itemName,itemPrice,itemDescription))