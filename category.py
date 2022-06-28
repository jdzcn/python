#!/usr/bin/python3

import json
import requests

r=requests.get('http://172.96.193.223/sblog/getlist.php')

json_array = r.json()

store_list = []

for item in json_array:
    store_details = {'title':None, 'file':None}
    store_details['title'] = item[0]
    store_details['file'] = item[1]

    store_list.append(store_details)

for i in store_list:
    print(i['title']+':'+i['file']+'\n')