#-*-coding: UTF-8-*-
from distutils.core import setup
import py2exe
 
setup(
     
    description = "图片下载",  
    zipfile=None,
    console=[{"script": "imgdown.py",  }],
    )