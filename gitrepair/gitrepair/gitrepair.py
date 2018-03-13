#! /usr/bin/env python  
import os
import argparse

repairstr="\n[receive]\ndenyCurrentBranch = ignore\n"

def OpenFileAndWrite(Path):
    pathname="%sconfig"%Path
    with open(pathname,'a+') as hFile:
        hFile.write(repairstr)

def main():
    parser = argparse.ArgumentParser(prog="gitrepair",description='Repaire Git Config.')#usage="test")
    parser.add_argument(type=str,action="store",dest="path",help="path to the .git") 
    args = parser.parse_args()

    #enable777object="chmod 777 %sobjects" % args.path
    #enable777lock="chmod 777 %srefs/heads/master" % args.path
    #os.system(enable777object)
    #os.system(touchlock)
    #os.system(enable777lock)
    OpenFileAndWrite(args.path)

if(__name__ == "__main__"):
    main()