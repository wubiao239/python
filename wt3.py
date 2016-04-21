# -*- coding: utf-8 -*-
__author__ = 'wubiao'



import time
import threading
import datetime
import os
import requests


#配置参数=============================================================。
domains=["rssdegreecollege.co.in","goodfoodcatering.in","ananyapools.in","warrierfoundation.in"] #需要注册的域名，两三个为宜
st=datetime.datetime.strptime("2016-03-04 23:56:00","%Y-%m-%d %H:%M:%S") #配置程序开始运行时间
email="domainindia@163.com" #用户名
password="wb19900321" #用户密码
ry=1 #注册年限
rd="2016-03-06" #注册时间 今天16号pending17号注册日期18号
cuid="13392391" #客户id
coid="46297369" #联系人id
#配置参数=============================================================。
config={"user_email":email,"user_pw":password,"domain_name":"","reg_years":ry, "reg_date":rd, "customer_id":cuid, "contact_id":coid,"contact_submit":"立即加入" }

class regThread(threading.Thread):
    def __init__(self,domain,config):
        threading.Thread.__init__(self)
        self.domain = domain
        self.config=config

    def run(self):
        
       

        print("提交域名,",self.domain,"开刷！！！！")
        j=1
        t1=datetime.datetime.now()
        self.config["domain_name"]=self.domain
        while 1 :
            
            try :
                r = requests.post("http://tools.crusherexporters.com/post-domain.php", data=self.config)
                print(r.status_code)
                print(r.text)
                print(self.domain)
                
                
            except:
                print(self.domain,"提交失败，要想搞到好域名需要靠毅力，咱接着刷")
            
            
            t2=datetime.datetime.now()
            
            print("已经刷了：",(t2-t1).seconds,"s，幸好是程序要不然会累死的")
            print("第",j,"次提交，整了这么多次不会封我号吧")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #程序开始刷域名到结束时间，一般40分钟哦即可，不用修改使用默认值
            tm=(t2-t1).seconds/(60)
            j+=1
            if(tm>=40) :
                break
        

        print("线程",self.domain,"结束！搞没搞到域名，谁知道，反正不想再刷了")

        print("\n")
        try :
            os._exit(0)
        except:
            print("时间已经到了关闭程序")


if __name__=='__main__':
    print("开始注册域名时间：",st)
    while 1 :
        now=datetime.datetime.now()
        if now > st:
            print("开始注册，亲爱的域名我来了")
            break
        else:
            print("当前时间：",now,"还没到，尼玛等的我花都谢了")
        time.sleep(60)
    print ("多线程开刷，不信我刷不到。")
    #根据域名个数多线程同时开刷 最好不要超过三个，可能会因网络问题卡死
    for i in domains:
        t = regThread(i,config)
        t.start()




















