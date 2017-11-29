prime=[0]*100001
for i in range(2,100001):
    if(prime[i]==0):
        for j in range (i+i,100001,i):
            prime[j]=1;
prm=[]
for i in range(2,1001):
    if(prime[i]==0):
        prm.append(i);
m=0
res=0
for i in range (1,1001):
    a1=i
    for j in prm:
        x=1
        k=j;
        while(prime[k]==0):
            k=x*x+x*i+j;
            x=x+1;
        if(x>m):
            m=x
            res=i*j
        x=1
        k=j;
        while(prime[k]==0):
            k=abs(x*x+x*i-j);
            x=x+1;
        if(x>m):
            m=x
            res=i*j*-1
    a1=-1*i
    for j in prm:
        x=1
        k=j;
        while(prime[k]==0):
            k=abs(x*x+x*a1+j);
            x=x+1;
        if(x>m):
            m=x
            res=i*j*-1
        x=1
        k=j;
        while(prime[k]==0):
            k=abs(x*x+x*a1-j);
            x=x+1;
        if(x>m):
            m=x
            res=i*j
print(m,res)
        
