#Exercise Page=https://scrapingclub.com/exercise/detail_json/
import requests
import re
import json
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/detail_json/"

r = requests.get(url)
data=r.text

soup=BeautifulSoup(data,"lxml")

#get to what we want
script=soup.find("script",string=re.compile('var obj ='))
json_text=re.search(r'^\s*var obj\s*=\s*({.*?})\s*;\s*$',script.string, flags=re.DOTALL | re.MULTILINE).group(1)

#validating json
json_text=json_text.replace("\"/static/img/\" + ","")
json_text=json_text.replace("\"96230-C\" + ","")

parsed=json.loads(json_text)
print("Item Name: {} \nItem Price: {}\nItem Description: {}".format(parsed['title'],parsed['price'],parsed['description']))