#coding=utf-8
__author__ = 'wubiao'


import time
import datetime
import os
import requests

#配置参数=============================================================。
#需要注册的域名，两三个为宜
domains=["rssdegreecollege.co.in","goodfoodcatering.in","ananyapools.in","warrierfoundation.in"]
st=datetime.datetime.strptime("2016-03-04 23:56:00","%Y-%m-%d %H:%M:%S") #配置程序开始运行时间
email="domainindia@163.com" #用户名
password="wb19900321" #用户密码
ry=1 #注册年限
rd="2016-03-06" #注册时间 今天16号pending17号注册日期18号
cuid="13392391" #客户id
coid="46297369" #联系人id
#配置参数=============================================================。
config={"user_email":email,"user_pw":password,"domain_name":"","reg_years":ry, "reg_date":rd, "customer_id":cuid, "contact_id":coid ,"contact_submit":"立即加入"}


def run(domains,config):

    print("提交域名,开刷！！！！")
    j=1
    t1=datetime.datetime.now()

    while 1 :

        for i in domains:
            config["domain_name"]=i

            try :
                r = requests.post("http://tools.crusherexporters.com/post-domain.php", data=config)
                print(r.status_code)
                print(r.text)
                print(i)
                

            except:
                print("域名添加失败，要想搞到好域名需要靠毅力，刷下一个域名")
        
        
        
        t2=datetime.datetime.now()
        
        print("已经刷了：",(t2-t1).seconds,"s，幸好是程序要不然会累死的")
        print("第",j,"次提交，整了这么多次不会封我号吧")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        #程序开始刷域名到结束时间，一般40分钟哦即可，不用修改使用默认值
        tm=(t2-t1).seconds/(60)
        j+=1
        if(tm>=40) :
            break
    
    try :
        os._exit(0)
    except:
        print("刷新次数或者时间已经到了关闭程序")

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
    
    #根据域名个数多线程同时开刷 最好不要超过三个，可能会因网络问题卡死
    
    
    run(domains,config)

        

























