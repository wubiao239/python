__author__ = 'wubiao'
import requests
import time
import threading
import datetime
import os
from pyocr import tesseract
from PIL import Image

#配置参数=============================================================。
domains=["pimsrc.in"] #需要注册的域名，你要是不填肯定注册不到
st=datetime.datetime.strptime("2016-03-16 03:55:00","%Y-%m-%d %H:%M:%S") #配置注册域名时间，别把时间设置到下个月就行
#配置参数=============================================================。


'''
验证码生成url：
/userself/RndCode.asp?rndtype=LOGIN_RndCode
'/UserSelf/rndcode_check.asp?name=lg&rndcode='+val
登陆页action：
http://www.ourui.com/userself/login.asp
username 
userpass
rndcode
'''
class regThread(threading.Thread):
    def __init__(self,domain):
        threading.Thread.__init__(self)
        self.domain = domain

    def run(self):
     #配置参数=============================================================。
        #登录账号 1：账户名 2：密码
        #配置自己的账号：username填写登录名，password填写登录密码
        username="18339260346"
        password="wb19900321"
        #配置参数=============================================================。
       
        #打开登录页面
        
        def login(username,password):
            
            while 1 :
                name="code.jpg"
                threshold = 140  
                table = []  
                for i in range(256):  
                    if i < threshold:  
                        table.append(0)  
                    else:  
                        table.append(1) 
                try :
                    image = requests.get('http://www.ourui.com/userself/RndCode.asp?rndtype=LOGIN_RndCode')
                    #print(image.content)
                    f=open(name,"wb+")
                    f.write(image.content)
                    f.close()
                    imagefile = Image.open(name)
                        

                    #转化到亮度  
                    imgry = imagefile.convert('L')  
                    imgry.save('g'+name)  
                    #二值化  
                    #out = imgry.point(table,'1')
                    out = imgry.point(lambda x: 255 if x > 141 else 0)  
                    out.save('b'+name)  
                    #识别  
                    
                    
                    val=tesseract.image_to_string(out)
                    print(val)
                    imgreq=requests.get("http://www.ourui.com/UserSelf/rndcode_check.asp?name=lg&rndcode="+val)
                    print(imgreq.content)
                    if imgreq.content=="0" or imgreq.content=="":
                        continue
                    r = requests.post("http://www.ourui.com/userself/login.asp", data={"username":username,"userpass":password})
                    r.content
                    print("login ok register",self.domain)
                    
                    break
                except:
                    
                    time.sleep(1)
                    print("矮油网速太渣，登录失败，重新登录！")
                   

       
        login(username,password)
        print("提交域名,开刷！！！！")
        j=1
        t1=datetime.datetime.now()
        while 1 :
           
            try :

                r = requests.post("http://comin.supersite2.myorderbox.com/domain-registration/bulk-domain-registration.php", data={"domainnames":self.domain})
                print(r.status_code)
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print(self.domain,"添加完成，等待注册局注册域名，注册局全靠你啦.")
               
            except:
                print(self.domain,"添加失败，要想搞到好域名需要靠毅力，咱接着刷")
           
            time.sleep(0.1)
            t2=datetime.datetime.now()
           
            print("已经刷了：",(t2-t1).seconds,"s，幸好是程序要不然会累死的")
            print("第",j,"次提交，整了这么多次不会封我号吧")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #程序开始刷域名到结束时间，一般40分钟哦即可，不用修改使用默认值
            tm=(t2-t1).seconds/(60)
            j+=1
            if(tm>=120) :
                break
        

        print("线程",self.domain,"结束！搞没搞到域名，谁知道，反正不想再刷了")

        print("\n")
        try :
            os._exit()
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
    print ("多开几个浏览器，不信我刷不到。")
    #根据域名个数多线程同时开刷 最好不要超过三个，可能会因网络问题卡死
    for i in domains:
        t = regThread(i)
        t.start()













