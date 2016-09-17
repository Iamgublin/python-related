﻿import urllib
import urllib2
import re
import time
import thread
from bs4 import BeautifulSoup
import urlparse
from selenium import webdriver
mode=1                                       #0:简单模式 速度快    #1虚拟浏览器模式：穿透反爬虫，但速度慢
fliter=re.compile("\.(jpg|gif|bmp|png)")    #图片正则过滤
hasvisited=[]
needtovisited=[]
threadcount=10                                #线程数
spinlock=0
base="http://image.baidu.com"
url='http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B1%C8%BB%F9%C4%E1&hs=0&fr=ala&ori_query=%E6%AF%94%E5%9F%BA%E5%B0%BC&ala=0&alatpl=sp&pos=0'
headers={'referer':'http://www.baidu.com/', 'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
x=0
def download(url):
    try:
        global x
        req=urllib2.Request(url,None,headers)
        te=urllib2.urlopen(req,timeout=5)
        temp1=fliter.findall(url)
        file=open("%s.%s"% (x,temp1[0][-3:]),"wb")
        file.write(te.read())
        file.close()
        spinlock.acquire()
        x=x+1
        spinlock.release()
        print "complete"
    except:
        print "failed"
        pass
def findphoto(bs,url):
    global x
    jieguo=bs.findAll(name ="img",attrs={"src":re.compile(r"^http://")})  #re.compile(r"^http://")
    for temp in jieguo:
        print "find picture %s"% temp["src"]
        if(re.compile(r"http://").findall(temp["src"])):
            download(temp["src"])                            #下载方式一
        else:
            print "\n\n\n\n\n\n\n"
            b=urlparse.urlparse(url)
            tempurl=b[0]+r"://"+b[1]+r"/"+temp["src"]
            print tempurl
            download(tempurl)
        #urllib.urlretrieve(temp["src"].encode("gb2312"),'%s.%s' %(x,temp["src"][-3:]))    #下载方式二
def openurlbystatic(url):
    req=urllib2.Request(url,None,headers)
    repeat_time = 0
    while True:
       try:
           res = urllib2.urlopen(req,None,10)
           return res.read()
       except:
           print "Open Url Failed !!! Repeat"
           time.sleep(1)
           repeat_time = repeat_time+1
           if repeat_time == 5:
                return None
def openurlbybrowner(url):
    try:
        driver=webdriver.PhantomJS(executable_path="phantomjs.exe")
        res=driver.get(url)
        time.sleep(3)
        res=driver.page_source
        driver.get_screenshot_as_file("10000.jpg")
        return res
    except:
        return None
def findurl(url):
    global spinlock
    if url in hasvisited:
        return
    if(fliter.findall(url)):                        #有时候图片可能直接在a标签里
        spinlock.acquire()
        hasvisited.append(url)
        spinlock.release()
        download(url)
        return 
    else:
        spinlock.acquire()
        hasvisited.append(url)
        spinlock.release()
    global mode
    if(mode==0):
        res=openurlbystatic(url)
    if(mode==1):
        res=openurlbybrowner(url)
    if(res==None):
        return
    try:
        html=None
        html = BeautifulSoup(res,"html.parser")
    except:
        print "%s this html might have some error so i have to pass" % url
        return 
    if(html==None):
        return
    findphoto(html,url)                          #只分析网址时注释此句
    article = html.findAll(name ="a",attrs={"href":re.compile(r"^.*/search/")})   #过滤规则  # re.compile(r"^http://")   re.compile(r".*//.*")
    try:
        for temp in article:
            if temp["href"] not in hasvisited:
                global base
                temp["href"]=base+temp["href"]
                print temp["href"]
                findurl(temp["href"])
    except:
        pass
def main():
    global spinlock
    sum=0
    spinlock=thread.allocate_lock()
    while sum<threadcount:
        thread.start_new_thread(findurl,(url,))
        sum=sum+1
    time.sleep(100)
if(__name__=="__main__"):
    main()