import urllib
import urllib2
import sgmllib
from bs4 import BeautifulSoup
class my_sgm(sgmllib.SGMLParser):
    def unknown_starttag(self, tag, attrs):        #解析html
        print "tag type:"+tag
        try:
            for attr in attrs:
                if attr[0]=="href":
                    print attr[0]+':'+attr[1].encode("utf-8")
        except:
            pass
    def unknown_endtag(self, tag):
        pass
res=urllib.urlopen("http://www.freebuf.com")
zlz_sgm=my_sgm()
zlz_sgm.feed(res.read())
