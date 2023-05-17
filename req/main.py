def prop(tex):
    messages=[]#text,time,role
    tex2=""
    for i in range(len(tex)-1):
        if tex[i]=="<":
            access=False
        if access and tex[i:i+1]!="\n\n":
            tex2+=tex[i]
        if tex[i]==">":
            access=True
    #print(tex2)        
    
    return tex2
i=0
result=""
while i <=1:#57750:
    file="req/lin/messages"+str(i)+".html"
    f = open (file , 'r')
    result += prop(f.read())

    print(result)
    f.close()
    i+=50


