'''
Created on 2016-3-27

@author: admin
'''

from ctypes import *

user32 = cdll.LoadLibray("user32.dll")
user32.lockWorkStation()