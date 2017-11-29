fac=[1]*11
fac[0]=1
for i in range(1,10):
    fac[i]=fac[i-1]*i
s=0
for i in range(10,100001):
    x=i
    res=0
    while(x):
        res= res+fac[x%10]
        x=x//10
    if(i==res):
        s=s+i
print(s)
