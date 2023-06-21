import pandas as pd

def write(res):
    fs = open('req/res.txt','w')
    try:
    # работа с файлом
        fs.write(res)
    finally:
        fs.close()

def prop(tex):#удаление html кода
    
    tex=tex.replace("<br>","\n")
    tex2=""

    for i in range(len(tex)-2):
        if tex[i]=="<":
            access=False
        if access:
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
        #if tex[i:i+2]!="\n\n"and ch:
        
        elif tex[i:i+10]=="123&raquo;":
            ch=False
        elif tex[i-10:i]=="123&raquo;":
            ch=True
        if ch:
            tex1+=tex[i]
           
    return (tex1)


def forma_arr(tex):
    tex1=[]
    tex2=""
    ch1 = ch2 =  ch3 = False
    for i  in range(len(tex)):
        if tex[i:i+6]=="  Вы, " :
            ch1 = True
            role=" вопрос: "
        elif tex[i:i+13]=="  Ланая Кит, ":
            ch1 = True
            role=" ответ: "
        elif ch1 and tex[i:i+3]=="\n  ":
            ch2 = True
            i0 = i+3
            ch1 = False
        
        elif tex[i:i+44]=="\n  1 прикреплённое сообщение\n  \n\n\n  \n  \n\n  \n" or tex[i:i+12]=="\n\n  \n  \n\n  \n" and ch2:
            ch3 = True
            i_last = i
            ch2 = False
        if ch3:
            if tex[i0:i_last]!="\n  Стикер\n  \n":
                tex1.append(tex[i0:i_last])
                tex2+=role+tex[i0:i_last]
            ch3 = False
            

    return tex1, tex2


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
a1,a2=forma_arr(result)
print(a2)
