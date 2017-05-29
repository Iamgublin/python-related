#!/usr/bin/python
#coding:utf-8
import sys
import os
from subprocess import Popen, PIPE
command="python "
commands =set("")                  #需要扫描的类型
commanddic={"--profile":"","-f":""}
def changestdout(filehandle):
    sys.stdout=filehandle
def createnewoutfileandout(filename,command):
    filehandle=os.open(filename,os.O_RDWR|os.O_CREAT)
    p = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    output = p.stdout.read()
    inter=os.write(filehandle,output)
    os.close(filehandle)
def loadcommands():
    global commands
    hfile=open("config","r+")
    for com in hfile.readlines():
        commands.add(com.rstrip())
def main():
    global command
    loadcommands()
    command=command+sys.path[0]+'\\'+"vol.py"
    if "--profile" not in sys.argv:
        print "you must produce a profile!"
        return
    if "-f" not in sys.argv:
        print "filename is required"
        return 
    commanddic["--profile"]=sys.argv[sys.argv.index("--profile")+1]
    commanddic["-f"]=sys.argv[sys.argv.index("-f")+1]
    for tmp1,tmp2 in commanddic.iteritems():
        command=command+" "+tmp1+" "+tmp2
    if not os.path.exists("output"):
        os.makedirs("output")
    for tmp in commands:
        commandend=command+" "+tmp
        createnewoutfileandout(".//output//"+tmp+".txt",commandend)
    return
if(__name__=='__main__'):
    main()