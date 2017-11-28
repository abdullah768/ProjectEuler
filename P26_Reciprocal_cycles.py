m=0
ind=0;
for i in range(2,1000):
    pls=[0]*10000
    x=1;
    for k in range (0,10000):
        x=x*10
        if(pls[x%i]==1):
           break
        pls[x%i]=1
        x=x%i
    if(k>m):
        ind=i
        m=k
print(ind)
    
