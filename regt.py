'''
Created on 2016-4-11

@author: wubiao
'''


__author__ = 'wubiao'


import requests
import time
import threading
import datetime
import os
import  json 
from tldextract import extract
import pytz
from xml.dom import minidom
domains = ["ampac.in", "bestbalajipackers.in", "rasalas.in", "clpr.in"] 
tz = pytz.timezone('Asia/Shanghai')
st = datetime.datetime.strptime("2016-04-16 03:55:00", "%Y-%m-%d %H:%M:%S") 
st = tz.localize(st)
class regThread(threading.Thread):
    def __init__(self, domain):
        threading.Thread.__init__(self)
        self.domain = domain

    def run(self):
        subdomain, maindomain, tld = extract(self.domain)
        checkurl = "https://test.httpapi.com/api/domains/available.json?auth-userid=646061&api-key=sP6NPKSyagaoitKcihSlMMdAEmot3zFq&domain-name=" + maindomain + "&tlds=" + tld
        regurl = "https://test.httpapi.com/api/domains/register.xml?auth-userid=646061&api-key=sP6NPKSyagaoitKcihSlMMdAEmot3zFq&domain-name=" + self.domain + "&years=1&ns=ns1.domain.com&ns=ns2.domain.com&customer-id=14663552&reg-contact-id=53312520&admin-contact-id=53312520&tech-contact-id=53312520&billing-contact-id=53312520&invoice-option=PayInvoice"


        def check():
            i = 1
            j=1
            t1 = datetime.datetime.now(tz)
            while 1 :

                try :
                    r = requests.get(checkurl,timeout=50)
                    res = json.loads(r.content.decode())
                    # print(res)
                    j=j+1
                    
                    print(self.domain, "alread check", j, "times")
                    status = res.get(self.domain).get('status')
                    # print(status)
                    if status and status.lower() == 'available':
                        print("available", self.domain)
                        break

                except:
                    print("request excption")

                t2 = datetime.datetime.now(tz)
                #if(i % 50 == 0):
                    #print(self.domain, "alread check", i , "times")

                tm = (t2 - t1).seconds / (60)

                if(tm >= 20) :
                    time.sleep(30)
                    if(tm>=60):
                        break
                i = i + 1   


        def reg():
            j = 1
            while 1 :
                try :


                    r = requests.get(regurl)
                    #print(r.text)
                    if(checksuccess(r.text)):
                        print(self.domain, "sale sucessful")
                        break

                     
                except Exception:
                    
                    print("try again!")
                j = j + 1
                if(j >= 8):
                    break

        def checksuccess(xml):
            doc = minidom.parseString(xml)
          
          
            root = doc.documentElement
          
         
            entrys = root.getElementsByTagName("entry")
          
            for entry in entrys:
            
            
                sta = entry.getElementsByTagName("string")[0].childNodes[0].nodeValue.lower()
                suc = entry.getElementsByTagName("string")[1].childNodes[0].nodeValue.lower()
                #print(sta,suc)
                if(sta == "status" and suc == "success"):
                
                    return True
                
            return False
        

        check()  
        reg()

        try :
            print("close programe")
            os._exit(0)
        except:
            print("close fail")



if __name__ == '__main__':
    print("regist time:", st)
    while 1 :
        now = datetime.datetime.now(tz)

        if now >= st:
            print("regist now:", now)
            break
        else:
            print("time:", now, "try it later")
        time.sleep(60)
    print ("multi thread to regist")

    for i in domains:
        t = regThread(i)
        t.start()
















