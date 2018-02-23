ck=[0]*10000000;
def pls(x):
    if(ck[x]!=0):
        return ck[x]
    k=x;
    lol=0;
    while(k>0):
        lol=lol+(k%10)*(k%10)
        k=k//10;
    if(lol==1):
        ck[x]=1;
    elif(lol==89):
        ck[x]=89;
    else:
        ck[x]=pls(lol)
    return ck[x]
for i in range(1,10000000):
    if(ck[i]==0):
        ck[i]=pls(i)
print(ck.count(89))
