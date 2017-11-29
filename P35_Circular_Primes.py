lt=1000000
prm=[1]*lt
for i in range(2,lt):
    if(prm[i]==1):
        for j in range(i+i,lt,i):
            prm[j]=0
ct=0
for i in range(2,lt):
    x=i
    dc=0
    if(prm[i]==1):
        while(x):
            x=x//10
            dc=dc+1
        x=i;
        f=0
        for j in range (0,dc):
            y=x%10
            x=y*10**dc+x
            x=x//10
            if(prm[x]==0):
                f=1;
                break
        if(f==0):
            ct=ct+1
print(ct)
            
    
