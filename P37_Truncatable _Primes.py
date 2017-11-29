lt=1000000
prm=[1]*lt
prm[0]=0
prm[1]=0
for i in range(2,lt):
    if(prm[i]==1):
        for j in range(i+i,lt,i):
            prm[j]=0
ct=0
for i in range (10,lt):
    f=0
    x=i
    while(x):
        if(prm[x]==0):
            f=1
            break
        x=x//10
    x=i
    while(x):
        if(prm[x]==0):
            f=1
            break
        x=int(str(x)[::-1])
        x=x//10
        x=int(str(x)[::-1])
        
    if(f==0):
        print(i)
        ct=ct+i
print(ct)
