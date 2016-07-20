def init():
    c={}
    return c
def zlzappend(name,dirc):
    lable="xing","ming"
    names=name.split()
    temp=zip(lable,names)
    temp1,temp2=temp[0]
    temp3,temp4=temp[1]
    dirc.setdefault(temp2,temp4)
    return dirc
a=init()
a=zlzappend("zhao lizhou",a)
a=zlzappend("zhao asffdd",a)
a=zlzappend("zhu xiang",a)
a=zlzappend("du laolao",a)
for xing in a:
    print "xing:"+xing+'\t'+"ming:"+a[xing]
