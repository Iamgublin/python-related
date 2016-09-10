import urllib2
import urllib
import json
header={"Host":"www.nowcoder.com","Accept":"text/plain, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)","Referer":"http://www.nowcoder.com/263608",
        "Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"zh-CN,zh;q=0.8","Cookie":"""gr_user_id=7edbdc1a-b7d6-4ccb-9073-4224229553b1; t=3AABF14367A2A2E5397EE512E0F7E3EB; NOWCODERUID=039A9100B9EFD8D76861509792E7427D; NOWCODERCLINETID=0E1EE6FD5A28C2CDA3779B259762D70D; CNZZDATA1253353781=1338405783-1460595648-%7C1473475604; _cnzz_CV1253353781=%E6%98%AF%E5%90%A6%E7%99%BB%E5%BD%95%7C%E5%B7%B2%E7%99%BB%E5%BD%95%7C1473482805346; SERVERID=04b0d01c5f76391d48534b2801b3cad1|1473475604|1473474248"""}
header1={"Host":"www.nowcoder.com","Accept":"text/plain, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)","Referer":"http://www.nowcoder.com/263608",
        "Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"zh-CN,zh;q=0.8","Cookie":"""Cookie: gr_user_id=7edbdc1a-b7d6-4ccb-9073-4224229553b1; t=3AABF14367A2A2E5397EE512E0F7E3EB; NOWCODERUID=039A9100B9EFD8D76861509792E7427D; NOWCODERCLINETID=0E1EE6FD5A28C2CDA3779B259762D70D; CNZZDATA1253353781=1338405783-1460595648-%7C1473475604; _cnzz_CV1253353781=%E6%98%AF%E5%90%A6%E7%99%BB%E5%BD%95%7C%E5%B7%B2%E7%99%BB%E5%BD%95%7C1473482805346; SERVERID=04b0d01c5f76391d48534b2801b3cad1|1473475604|1473474248"""}
header2={"Host":"www.nowcoder.com","Content-Length":"8","Accept":"text/plain, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)","Referer":"http://www.nowcoder.com/263608",
        "Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"zh-CN,zh;q=0.8","Cookie":"""gr_user_id=7edbdc1a-b7d6-4ccb-9073-4224229553b1; t=3AABF14367A2A2E5397EE512E0F7E3EB; NOWCODERUID=039A9100B9EFD8D76861509792E7427D; NOWCODERCLINETID=0E1EE6FD5A28C2CDA3779B259762D70D; dc_pid_set_next_pre=8059_8392_8771_8835_9202_9219_9207_9166_9201_9218_9213_9181_9179_9188_9217_9216_9107_9215_9214_9210_9168_9198_9211_9212_9161_9195_9208_9209_9150_9204; CNZZDATA1253353781=1338405783-1460595648-%7C1473476285; _cnzz_CV1253353781=%E6%98%AF%E5%90%A6%E7%99%BB%E5%BD%95%7C%E5%B7%B2%E7%99%BB%E5%BD%95%7C1473483486692; SERVERID=04b0d01c5f76391d48534b2801b3cad1|1473476298|1473474248"""}
temp={"feeling":""}
data=urllib.urlencode(temp)
req=urllib2.Request("http://www.nowcoder.com/clock/todayInfo?token=&_=1473475604626",None,header)
req1=urllib2.Request("http://www.nowcoder.com/token/login-other-place?token=&_=1473475604626",None,header1)
req2=urllib2.Request("http://www.nowcoder.com/clock/new?token=",data,header2)
res=urllib2.urlopen(req)
res1=urllib2.urlopen(req1)
res2=urllib2.urlopen(req2)
dict=json.loads(res.read())
print dict
print res1.read()