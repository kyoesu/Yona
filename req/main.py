import pandas as pd

def write(res):
    fs = open('req/res.txt','w')
    try:
    # работа с файлом
        fs.write(res)
    finally:
        fs.close()

def prop(tex):#удаление html
    messages=[]#text,time,role
    tex2=""
    for i in range(len(tex)-2):
        if tex[i]=="<":
            access=False
        if access:# and tex[i:i+1]!="\r\n":
            tex2+=tex[i]
        if tex[i]==">":
            access=True
    #print(tex2)        
    
    return tex2

def forma(tex):
    tex1=""
    ch=False
    for i  in range(len(tex)):
        if tex[i:i+25]=="ПрофильСообщенияЛаная Кит":
            ch=True
        if tex[i:i+2]!="\n\n"and ch:
            tex1+=tex[i]
        else:
            i+=1    
    return (tex1)


i=0
result=""
while i <=2:#57750:
    file="req/lin/messages"+str(i)+".html"
    f = open (file , 'r')
    result += prop(f.read())
    
    #print(result)
    f.close()
    i+=50


#write(result)

print(forma(result))