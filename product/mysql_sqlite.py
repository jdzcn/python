#!/usr/bin/python3
import requests
import json
import sqlite3

       	r=requests.get('http://172.96.193.223/product.php')

        print(r.status_code)

        json_array = r.json()

        # for item in json_array:
        #     store_details = {'id':None,'name':None, 'cid':None,'images':None,'tags':None,'spec':None,'price':None}
        #     store_details['id'] = item['id']
        #     store_details['name'] = item['name']
        #     store_details['cid'] = item['cid']
        #     store_details['images'] = item['images']
        #     store_details['tags'] = item['tags']
        #     store_details['spec'] = item['spec']
        #     store_details['price'] = item['price']

	conn=sqlite3.connect('product.db')

	db = conn.cursor()

	print ("数据库打开成功")

	for item in json_array:
		sql='insert into product values('+item['name']+')'
		db.execute(sql)

	conn.commit()
	conn.close()
