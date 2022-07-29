#!/usr/bin/python3
import requests
import json
import sqlite3

r=requests.get('http://172.96.193.223/product.php')
print(r.status_code)
json_array = r.json()
conn=sqlite3.connect('product.db')
db = conn.cursor()
print ("数据库打开成功")
for item in json_array:
        sql=f"insert into product values('{item['name']}','{item['images']}',{item['cid']},'{item['spec']}',{item['price']})"
        print(sql)

	# db.execute(sql)

conn.commit()
conn.close()
