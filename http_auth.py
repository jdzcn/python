#!/usr/bin/python3

import json
import requests
from requests.auth import HTTPBasicAuth

r=requests.get('http://172.96.193.223/admin/product.php',auth=HTTPBasicAuth('sb','songbin'))
print(r.status_code)

json_array = r.json()

store_list = []

for item in json_array:
    store_details = {'id':None,'name':None, 'cid':None,'images':None,'tags':None,'spec':None,'price':None}
    store_details['id'] = item['id']
    store_details['name'] = item['name']
    store_details['cid'] = item['cid']
    store_details['images'] = item['images']
    store_details['tags'] = item['tags']
    store_details['spec'] = item['spec']
    store_details['price'] = item['price']
    store_list.append(store_details)

for i in store_list:
    print(i['name'])