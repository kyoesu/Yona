import pandas as pd
import numpy as np
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
    access=False

    for i in range(len(tex)-2):
        if tex[i]=="<":
            access=False
        if access:
            tex2+=tex[i]
        if tex[i]==">":
            access=True
    #print(tex2)        
    tex2=tex2.replace("&lt;","<")
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


def forma_arr(tex,name):
    tex1=[]
    tex2=""
    tex3=[]
    boof=[]
    ch1 = ch2 =  ch3 = False
    for i  in range(len(tex)):
        if tex[i:i+6]=="  Вы, " :
            ch1 = True
            role="вопрос:"
        elif tex[i:i+13]=="  "+name+", ":
            ch1 = True
            role="ответ:"
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
                tex1.append(" "+role+" "+tex[i0:i_last])
                tex2+=" "+role+" "+tex[i0:i_last]
                boof.append(role)
                boof.append(tex[i0:i_last])
                tex3.append(boof)
                boof=[]
            ch3 = False
    #tex1 - arr      
    #tex2 - string
    #tex3 - arr[arr]
    return tex1,tex2, tex3

def save_np(arr,name,ch=False):
    num_arr=np.array(arr)
    df = pd.DataFrame(num_arr)
    name='req/'+name+'.csv'
    try:
        if ch:
            np.save('req/res.npy',num_arr)
        df.to_csv(name, index=False)
    except:
        print("error")



def save_txt(text):
    with open('req/out.txt','w', encoding="utf-8") as f:
        f.write(text)
        f.close()



def reverce_np(arr):
    new_arr=arr
    for i in range(50):#len(my_array)):
        #print (my_array[(len(my_array)-i)-1])
        new_arr.append(arr[(len(arr)-i)-1])
    return(new_arr)


i=0
result=""
while i <=157750:
    file="req/lin/messages"+str(i)+".html"
    f = open (file , 'r')
    result += prop(f.read())
    
    #print(i)
    f.close()
    
    i+=50
import sys
#print(result)
print(sys.getsizeof(result))

#write(result)
a1,a2,a3=forma_arr(result,"Ланая Кит")
#save_txt(a2)
#print(a3)
#save_np(a3)
print("первый массив готов")
arr_time=reverce_np(a3)
print("перевернутый готов")
save_np(a3,"first")
save_np(arr_time,"second")
print("записалось")

