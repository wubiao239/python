__author__ = 'wubiao'


from selenium import webdriver
import time
import threading
import datetime
import os


#配置参数=============================================================。
domains=["nimt.in","hyderabadflowerdecorations.in","redesigngroup.in","schooledudindigul.in"] #需要注册的域名，最好三个以内，你要是不填肯定注册不到

st=datetime.datetime.strptime("2015-09-21 03:54:00","%Y-%m-%d %H:%M:%S") #配置注册域名时间，别把时间设置到下个月就行
#配置参数=============================================================。

class regThread(threading.Thread):
    def __init__(self,domain):
        threading.Thread.__init__(self)
        self.domain = domain

    def run(self):
    	#配置参数=============================================================。
        #登录账号 1：账户名 2：密码
        #配置自己的账号：username填写登录名，password填写登录密码
        username="domainindia@163.com"
        password="wb19900321"
        #配置参数=============================================================。
        try :
            #browser = webdriver.Firefox() 
            browser = webdriver.Chrome()
        except:
            print("没有安装Firefox浏览器，浏览器版本过低，也可能被杀毒软件阻止")
            print("尼玛你啥都不装，怨我呀!! 5s 后自动关闭")
            time.sleep(5)
            try :
                os._exit(0)
            except:
                print("关闭程序！！！！")

        #打开登录页面
        def login(username,password):
            while 1 :
                try :
                    browser.get("http://www.domain-inc.org/login.php")

                    print("open website ok")

                    browser.find_element_by_name("txtUserName").send_keys(username)
                    browser.find_element_by_id("input_password").send_keys(password)
                    browser.find_element_by_css_selector("#cust-login-form button").click()

                    print("login ok register",self.domain)
                    break
                except:
                    print("矮油网速太渣，登录失败，重新登录！")
                    time.sleep(0.5)
                    

        
        login(username,password)

       	

        print("提交域名,开刷！！！！")
        j=1
        t1=datetime.datetime.now()
        while 1 :
            
            try :
            	
                #####能不能搞到主要还是看网速和放出时间#########

                browser.get("http://www.domain-inc.org/domain-registration/index.php")
                browser.find_element_by_id("ndomins-list").send_keys(self.domain)
                browser.find_element_by_class_name("uiButton").click()

               	browser.find_element_by_css_selector(".primary-result-section .primary-result:nth-last-child(1) button.select-domain").click()
               	#browser.find_element_by_id("go_btn").click()
                browser.find_element_by_id("checkout").click()
                browser.find_element_by_class_name("no-thanks-link").click()
                browser.find_element_by_id("pay_debit_button").click()
                print("域名购买成功")
                
                break
            except:
                print(self.domain,"添加失败，要想搞到好域名需要靠毅力，咱接着刷")
                time.sleep(0.2)
            
            time.sleep(0.2)
            t2=datetime.datetime.now()
            
            print("已经刷了：",(t2-t1).seconds,"s，幸好是程序要不然会累死的")
            print("第",j,"次提交，整了这么多次不会封我号吧")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #程序开始刷域名到结束时间，一般40分钟哦即可，不用修改使用默认值
            tm=(t2-t1).seconds/(60)
            j+=1
            if(j>=2000 or tm>=40) :
            	print("线程",self.domain,"结束！没搞到域名，谁知道，反正不想再刷了")
            	break

        browser.close()
        print("关闭浏览器")
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
    #print ("多开几个浏览器，不信我刷不到。")
    #根据域名个数多线程同时开刷 最好不要超过三个，可能会因网络问题卡死
    for i in domains:
    	#ds=i+"\n\r"
    	t = regThread(i)
    	t.start()
    













