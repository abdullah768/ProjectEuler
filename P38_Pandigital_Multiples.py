def pan(x):
    dig=[0]*10
    while(x):
        y=x%10
        dig[y]=dig[y]+1
        x=x//10
    if(dig[0]>0):
        return 0
    for i in range (1,10):
        if(dig[i]!=1):
            return 0
    return 1
mx=0
x=""
lt=10000000000
for i in range(1,100000):
    x=i
    s=""
    j=0
    while(j<lt):
        s=s+str(x)
        j=int(s)
        if(pan(j)):
           if(j>mx):
               mx=j
        x=x+i
print(mx)
