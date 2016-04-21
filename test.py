import urllib.request
import urllib.parse

email="domainindia@163.com" #用户名
password="wb19900321" #用户密码
ry=1 #注册年限
rd="2015-10-24" #注册时间 今天16号pending17号注册日期18号
cuid="13392391" #客户id
coid="46297369" #联系人id
#配置参数=============================================================。
param={"user_email":email,"user_pw":password,"domain_name":"test.in","reg_years":ry, "reg_date":rd, "customer_id":cuid, "contact_id":coid ,"contact_submit":"立即加入"}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
params = urllib.parse.urlencode(param)
binary_data = params.encode()
res=urllib.request.Request("http://tools.crusherexporters.com/post-domain.php",data=binary_data,headers=headers)
f = urllib.request.urlopen(res)
print(f.read().decode())


























