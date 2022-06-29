#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom
import requests

r=requests.get('http://172.96.193.223/sblog/getlistxml.php')


DOMTree = xml.dom.minidom.parseString(r.text)
collection = DOMTree.documentElement

blogs = collection.getElementsByTagName("blog")
 
for blog in blogs:
 
   title = blog.getElementsByTagName('title')[0]
   print ("title: %s" % title.childNodes[0].data)

   file = blog.getElementsByTagName('file')[0]
   print ("file: %s" % file.childNodes[0].data)
   print('---------------------------------------')
