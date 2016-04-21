'''
Created on 2016-3-27

@author: admin
'''

import urllib.request
import os
import re

url="http://1616lu.com/html/tupian/qingchun/index_"
index=1
for i in range(1,24):
   
    openurl=(i==1)and "http://1616lu.com/html/tupian/qingchun/index.html" or url+str(i)+".html"
    imgHtml=urllib.request.urlopen(openurl).read().decode('utf-8')
    urls=re.findall(r'<li><a href="/html/tupian/qingchun/(.*)" target="_blank">',imgHtml)
    print("分析网页....")
    downurl="http://1616lu.com/html/tupian/qingchun/"
    for url in urls:
       
       
        #未能正确获得网页 就进行异常处理
        try:
           
            imgHtml=urllib.request.urlopen(downurl+url).read().decode('utf-8')
            imgurls=re.findall(r'<p><img src="http://pic.1100lu.net/(.*?)" alt="" /></p>',imgHtml)
           
            for imgurl in imgurls:
               
                res=urllib.request.urlopen("http://pic.1100lu.net/"+imgurl)
                if str(res.status)!='200':
                    print('未下载成功：')
                    continue
                filepath,name=os.path.split(imgurl)
                print("下载:",name)  
                filename=os.path.join(os.getcwd(),name)
                if os.path.exists(filename):
                    print("文件已存在",name,"跳过")
                    continue
                with open(filename,'wb') as f:
                    f.write(res.read())
                    print('下载完成\n',name)
                    index+=1
           
        except Exception as e:
            print('未下载成功：',url)

   
print("下载结束，一共下载了 %s 张图片"% (index-1))