'''
Created on 2016-4-13

@author: wubiao
'''


import requests
import re
import datetime
import sys

session=requests.Session()
today=datetime.datetime.today()
#keys=["school","college","education","university","hotel","class","foundation","study","hospital","medical","science","medicine","sanatorium","scientific","primary","technology","student","teacher"]
date=str(today.year)+"-"+"0"+str(today.month)+"-"+str(today.day)
start=0
flimit=200
res="<td class=\"field_domain\"><a href=\"/goto/1/(.*?)>(.*?)</a>"

def login():
    i=1
    while True:
        
        try:
            r = session.post("https://member.expireddomains.net/login/", data={"login":"wubiao386", "password":"wb123456", "rememberme":1,"button_submit":"Login"})
            print("login success")
            #print(r.text)
            break
        except:
            print("may be firewell ,login fail and login again")
        i=i+1
        if(i>10):
            print("try to 10 times,can't login")
            sys.exit(0)
            

def getalldomainsin():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        print("get .in")
        print("==================================================")
        
        domains=[]
        for i in range(1):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=124&ftlds[]=310&ftlds[]=311&ftlds[]=312&ftlds[]=313&ftlds[]=314&ftlds[]=315&flimit="+str(flimit)+"&fginfo=2&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
              
        getkeydomains(list(set(domains)),["school","college","education","university","hotel","class","foundation","study","hospital","medical","science","medicine","sanatorium","scientific","primary","technology","student","teacher"])  
        print(".in over")
        print("==================================================")   
    except:
        print("find fail ") 

def getalldomainscom():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        
        
        domains=[]
        print("get .com")
        print("==================================================")
        for i in range(5):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=2&flimit="+str(flimit)+"&fginfo=2&fpr=3&fprm=10&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
            
        getkeydomains(list(set(domains)),["school","college","university","hotel","hospital"])
        print(".com over")
        print("==================================================")   
    except:
        print("find fail ")                    



    

       
def getalldomainsnet():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        
        
        domains=[]
        print("get .net")
        print("==================================================")
        for i in range(3):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=3&flimit="+str(flimit)+"&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
            
        getkeydomains(list(set(domains)),["school","college","education","university","hotel","foundation","hospital","primary","technology","student"])
        print("over .net")
        print("==================================================")    
    except:
        print("find fail ")
def getalldomainsca():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        
        
        domains=[]
        print("get .ca")
        print("==================================================")
        for i in range(3):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=58&flimit="+str(flimit)+"&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
            
        getkeydomains(list(set(domains)),["school","college","education","university","hotel","foundation","hospital","primary","technology","student"])
        print("over .ca")
        print("==================================================")    
    except:
        print("find fail ")          
        
def getalldomainsorg():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        
        
        domains=[]
        print("get .org")
        print("==================================================")
        for i in range(5):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=4&flimit="+str(flimit)+"&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
            
        getkeydomains(list(set(domains)),["school","college","university","hotel","hospital","primary","kid"])   
        print(".org over")
        print("==================================================")   
    except:
        print("find fail ")
def getalldomainsru():
    try:
        #r=session.get("https://member.expireddomains.net/domains/expiredin/")
        
        
        domains=[]
        print("get .ru")
        print("==================================================")
        for i in range(5):
            start=i*flimit
            
            r = session.get("https://member.expireddomains.net/domains/pendingdelete/?start="+str(start)+"&ftlds[]=207&flimit="+str(flimit)+"&fginfo=2&fpr=1&fprm=10&fpr0=1&fenddate="+date)
        
            s=r.text
            #print(s)
            g=re.findall(res,s)
            
            
            for i in g:
                
                domains.append(i[1])
            
        getkeydomains(list(set(domains)),["school","college","university","hotel","hospital","primary","kid"])   
        print(".ru over")
        print("==================================================")   
    except:
        print("find fail ")                 
               
def getkeydomains(domains,keys):
    f=open(date+"-domains"+".txt","a+")
    keydomains=[]
    for i in domains:
        
        for j in keys:
            if(j in i):
                
                keydomains.append(i)
                
                f.wite(i)
    f.close()

def getdomains():
    login()
    getalldomainsin()
    getalldomainsru()
    getalldomainsnet()
    getalldomainsca() 
    getalldomainsorg()
    getalldomainscom()       
       
          
if __name__=="__main__":
    print("find pending",date,".in domains")
    
    getdomains()
    
    
        