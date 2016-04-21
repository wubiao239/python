'''
Created on 2016-4-16

@author: admin
'''
import xml.dom.minidom as minidom
s="""
<hashtable>
  <entry>
    <string>actiontypedesc</string>
    <string>Registration of homeinteriordecorators.pw for 1 year</string>
  </entry>
  <entry>
    <string>unutilisedsellingamount</string>
    <string>-4.000</string>
  </entry>
  <entry>
    <string>pendingamount</string>
    <string>4.0</string>
  </entry>
  <entry>
    <string>sellingamount</string>
    <string>-4.000</string>
  </entry>
  <entry>
    <string>entityid</string>
    <string>67262002</string>
  </entry>
  <entry>
    <string>status</string>
    <string>Success</string>
  </entry>
  <entry>
    <string>customerid</string>
    <string>14663552</string>
  </entry>
  <entry>
    <string>invoiceid</string>
    <string>60740358</string>
  </entry>
  <entry>
    <string>sellingcurrencysymbol</string>
    <string>CNY</string>
  </entry>
  <entry>
    <string>actionstatusdesc</string>
    <string>Invoice is partly paid</string>
  </entry>
</hashtable>


"""
def checksuccess():
    
    doc = minidom.parseString(s) 
    
    
    # get root element: <employees/>
    root = doc.documentElement
  
    print(root)
    entrys = root.getElementsByTagName("entry")
  
    for entry in entrys:
    
    
        sta = entry.getElementsByTagName("string")[0].childNodes[0].nodeValue.lower()
        suc = entry.getElementsByTagName("string")[1].childNodes[0].nodeValue.lower()
        print(sta,suc)
        if(sta=="status" and suc=="success"):
            print("register success")
    
checksuccess()