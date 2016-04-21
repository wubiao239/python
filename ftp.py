'''
Created on 2016-3-28

@author: wubiao
'''
from ftplib import FTP
f=FTP()
f.connect("188.226.198.191", 21)
f.login('root','wuiao123.')