import urllib
import urllib2
import re
from bs4 import BeautifulSoup
hasvisited=[]
url='http://www.freebuf.com/'
x=0
def findphoto(bs):
    global x
    jieguo=bs.findAll(name ="img",attrs={"src":re.compile(r"^http://")})
    for temp in jieguo:
        print "find picture %s"% temp["src"]
        urllib.urlretrieve(temp["src"].encode("gb2312"),'%s.%s' %(temp["src"][-7:-3],temp["src"][-2:])) 
        x=x+1
def findurl(url):
    if url in hasvisited:
        return
    else:
        hasvisited.append(url)
    res=urllib.urlopen(url)
    try:
        html = BeautifulSoup(res.read(),"html.parser")
    except:
        print "%s this html might have some error so i have to pass" % url
    findphoto(html)
    article = html.findAll(name ="a",attrs={"href":re.compile(r"^http://www.freebuf.com")})
    try:
        for temp in article:
            if temp["href"] not in hasvisited:
                print temp["href"]
                findurl(temp["href"])
            #urllib.urlretrieve(temp["src"],'%s.jpg' % x)  
            #x = x + 1
    except:
        pass
findurl(url)
#respHtml = resp.read();
 
#binfile = open(fileToSave, "wb");
#binfile.write(respHtml);
 
#binfile.close();