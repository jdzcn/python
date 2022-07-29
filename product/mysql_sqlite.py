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
        if '15' in item['tags']:
                sid=2
        else:
                sid=1
        name=item['name'].replace('景德镇御雅堂手绘','')
        gid=item['tags'].replace('1,','').split(',')[0]
        sql=f"insert into product (name,image,cid,sid,gid,spec,price) values('{name}','{item['images']}',{item['cid']},{sid},{gid},'{item['spec']}',{item['price']})"
        print(sql)
        db.execute(sql)
conn.commit()
conn.close()
print('Data convert successfully.')

