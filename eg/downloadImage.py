#!/usr/bin/env python3  #可以让这个learning.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-    #表示.py文件本身使用标准UTF-8编码

import urllib.request
import re

#获取网页HTML代码
def getHTML(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

#从HTML中解析出图片url
def getImg(html):  
    reg=r'data-original="(.*?\.jpg)"'  
    imgre=re.compile(reg);  
    htmld=html.decode('utf-8')  
    imglist=re.findall(imgre, htmld)  
    return imglist 

def downloadToLocal(imgUrls):
	x = 1
	for url in imgUrls:
		urllib.request.urlretrieve(url,"/Users/maccarduo/Desktop/pic/%s.jpg" % x)
		x += 1
	print("下载完成")

if __name__ == '__main__':
 	 html = getHTML("http://www.nipic.com/topic/show_27140_1.html")
 	 downloadToLocal(getImg(html))