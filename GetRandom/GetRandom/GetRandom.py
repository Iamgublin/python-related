# -*- coding: gbk -*-
import re
import requests
from bs4 import BeautifulSoup

r1=re.compile(u"�ٶ�Ϊ���ҵ���ؽ��Լ([^��]*)")
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}  
payload = {'wd':u'222'}  
  
url = 'http://www.baidu.com/s'  
 

def main():
    ser=input('����Ҫ��������:')
    payload['wd']=ser
    res=requests.get(url, params=payload, headers=headers, timeout=5) 
    #print(res.encoding)
    #print(res.content.decode('gb2312','ignore'))
    end=r1.findall(res.text)
    number=end[0].replace(',','')
    print('�����������Ϊ:',end='')
    print(number)
    input()
    #soup=BeautifulSoup(res.content,"html.parser")
    #soup.find()
    #with open("1.txt", 'wb',encoding=None) as f:             
        #f.write(res.content)
        #f.close()
if(__name__=='__main__'):
    main()