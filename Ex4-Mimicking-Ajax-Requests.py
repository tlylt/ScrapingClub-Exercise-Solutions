#Exercise Page = https://scrapingclub.com/exercise/ajaxdetail/
import requests
import json

#ajax link found by inspecting the network XHR Request
ajax_url="https://scrapingclub.com/exercise/ajaxdetail/"

r=requests.get(ajax_url)
item=json.loads(r.text)

print("Item Name: {}\nItem Price: {}\nItem Description: {}".format(item['title'],item['price'],item['description']))