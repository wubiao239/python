'''
Created on 2016-4-13

@author: wubiao
'''


import requests
import re
import datetime
import sys

session = requests.Session()
today = datetime.datetime.today()
# keys=["school","college","education","university","hotel","class","foundation","study","hospital","medical","science","medicine","sanatorium","scientific","primary","technology","student","teacher"]
date = str(today.year) + "-" + "0" + str(today.month) + "-" + str(today.day)
yesterday = str(today.year) + "-" + "0" + str(today.month) + "-" + str(today.day-1)
start = 0
flimit = 200
res = "<td class=\"field_domain\"><a href=\"/goto/1/(.*?)>(.*?)</a>"

def login():
    i = 1
    while True:

        try:
            r = session.post("https://member.expireddomains.net/login/", data={"login":"wubiao386", "password":"wb123456", "rememberme":1, "button_submit":"Login"})
            print("login success")
            # print(r.text)
            break
        except:
            print("may be firewell ,login fail and login again")
        i = i + 1
        if(i > 10):
            print("try to 10 times,can't login")
            sys.exit(0)


def getalldomainsin():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")
        print("get .in")
        

        domains = []
        for i in range(2):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=124&ftlds[]=310&ftlds[]=311&ftlds[]=312&ftlds[]=313&ftlds[]=314&ftlds[]=315&flimit=" + str(flimit) + "&fginfo=2&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "education", "university", "hotel", "class", "foundation", "study", "hospital", "medical", "science", "medicine", "sanatorium", "scientific", "primary", "technology", "student", "teacher", "institution", "enterprise", "green", "solution", "group", "hostel", "faculty", "revolution", "baby","academy"])  
        print(".in over")
           
    except:
        print("find fail ")
         
       

def getalldomainscom():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")


        domains = []
        print("get .com")
        
        for i in range(5):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=2&flimit=" + str(flimit) + "&fginfo=2&fpr=3&fprm=10&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "university", "hotel", "hospital", "institution", "enterprise", "green", "solution", "baby","academy"])
        print(".com over")
         
    except:
        print("find fail ")                    






def getalldomainsnet():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")


        domains = []
        print("get .net")
        
        for i in range(3):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=3&flimit=" + str(flimit) + "&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "education", "university", "hotel", "foundation", "hospital", "primary", "technology", "student","academy" ])
        print("over .net")
            
    except:
        print("find fail ")
def getalldomainsca():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")


        domains = []
        print("get .ca")
        
        for i in range(3):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=58&flimit=" + str(flimit) + "&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "education", "university", "hotel", "class", "foundation", "study", "hospital", "medical", "science", "medicine", "sanatorium", "scientific", "primary", "technology", "student", "teacher", "institution", "enterprise", "green", "solution", "group", "hostel", "faculty", "revolution", "baby","academy"])
        print("over .ca")
            
    except:
        print("find fail ")          

def getalldomainsorg():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")


        domains = []
        print("get .org")
        
        for i in range(5):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=4&flimit=" + str(flimit) + "&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "education", "university", "hotel", "class", "foundation", "study", "hospital", "medical", "science", "medicine", "sanatorium", "scientific", "primary", "technology", "student", "teacher", "institution", "enterprise", "green", "solution", "group", "hostel", "faculty", "revolution", "baby", "child", "organization","academy"])   
        print(".org over")
           
    except:
        print("find fail ")
def getalldomainsru():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")


        domains = []
        print("get .ru")
        
        for i in range(5):
            start = i * flimit

            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start=" + str(start) + "&ftlds[]=207&flimit=" + str(flimit) + "&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate=" + date)

            s = r.text
            # print(s)
            g = re.findall(res, s)


            for i in g:

                domains.append(i[1])

        getkeydomains(list(set(domains)), ["school", "college", "university", "hotel", "hospital", "primary", "kid","academy"])   
        print(".ru over")
          
    except:
        print("find fail ")                 

def getkeydomains(domains, keys,expired=0):
    if(expired==0):
        
        f = open("pending domains" + ".txt", "a+")
        f.write(date+"====================================\n")
        keydomains = []
        for i in domains:
    
            for j in keys:
                if(j in i):
    
                    keydomains.append(i)
    
                    f.write(i + "\n")
                    
        f.close()
    else:
        f=open("-1 in expired.txt")
        keydomains = []
        for i in domains:
    
            for j in keys:
                if(j in i):
    
                    keydomains.append(i)
    
                    f.write(i + "\n")
        f.close()   

def getexpiredin():
    getalldomainsinfuyi()
    
def getalldomainsinfuyi():
    try:
        # r=session.get("https://member.expireddomains.net/domains/expiredin/")
        print("get pr -1 expired .in")
        

        domains = []
        for i in range(10):
            try:
                start = i * flimit
                j = 0
                while True:
                    try:
                        r = session.get("https://member.expireddomains.net/domains/expiredin/?start=" + str(start) + "&flimit=100&fprminus1=1&fwhois=22")
        
                        s = r.text
                        # print(s)
                        g = re.findall(res, s)
                        break
                    except:
                        j = j + 1
                        if(j >= 5):
                            break    
    
    
                for i in g:
                    
                    domains.append(i[1])
    
            
            
            except:
                
                continue
        getkeyindomainsfuyi(list(set(domains)), ["school", "college", "education", "university", "hotel",  "foundation", "study", "hospital",  "science", "scientific", "primary", "technology", "kid","group","enterprise","welfare","academy"])  
        
        print(".in over")
        #print(keydomains)  
    except:
        print(".in over") 


def getkeyindomainsfuyi(domains, keys):
    fp=open("expired-1in.txt","a+")
    fp.write(yesterday+"====================================\n")
    keydomains = []
    for i in domains:

        for j in keys:
            if(j in i):

                keydomains.append(i)
                fp.write(i+"\n")
    
    fp.close()
    return keydomains
 
def getdomains():
    login()
    getexpiredin()
    getalldomainsin()
    getalldomainsru()
    getalldomainsnet()
    getalldomainsca() 
    getalldomainsorg()
    getalldomainscom()       


if __name__ == "__main__":
    print("find pending", date, ".in domains")

    getdomains()



