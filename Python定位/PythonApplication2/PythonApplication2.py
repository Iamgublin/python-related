import urllib
import urllib2
import json
import ConfigParser
config=ConfigParser.ConfigParser()
try:
    config.readfp(open("conf.ini"))
    ip=config.get("base conf","ip")
    ak=config.get("base conf","ak")
    qte=config.get("base conf","qte")
    extensions=config.getint("base conf","extensions")
except IOError:
    inif=open("conf.ini","wb+")
    config.readfp(inif)
    config.add_section("base conf")
    config.set("base conf","ip","59.37.96.38"+"\n")
    config.set("base conf","ak","Ds9nHeUH42c2zVLI6A1e3nt9MIxoaK7t"+"\n")
    config.set("base conf","qte","pc"+"\n")
    config.set("base conf","extensions",3+"\n")
    config.write(open("conf.ini","wb+"))
    ip="59.37.96.38"
    ak="Ds9nHeUH42c2zVLI6A1e3nt9MIxoaK7t"
    qte="pc"
    extensions=3
print ip
url="http://api.map.baidu.com/highacciploc/v1?"
param={"qcip":ip,"ak":ak,"qte":qte,"extensions":extensions}
data=urllib.urlencode(param)
req=urllib2.Request(url+data);
res=urllib2.urlopen(req)
#print res.read().decode("utf-8").encode("gb2312")
result=json.loads(res.read())
try:
    print """IP position"""
    for temp1 in result["content"]["address_component"]:
        print temp1+":",
        print result["content"]["address_component"][temp1]
    print "business"+":",
    print result["content"]["business"]                                        #IP大概地址
    print "\n\n"
    num=len(result["content"]["pois"])
    a=0
    while a<num:
        #附近的一些地点
        print "position%d:" % a
        for temp in result["content"]["pois"][a]:
            print temp+":",
            print result["content"]["pois"][a][temp]
        a=a+1
        print "\n\n"
except:
    pass