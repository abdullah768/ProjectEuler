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
ls=[]
for i in range (1,4):
    j1=10**(i-1)
    j=10**i
    for x in range (j1,j):
        lt=10**(5-i)
        for y in range(x,lt):
                k=x;
                res=0;
                while(k):
                    res=res*10+k%10;
                    k=k//10;
                k=y
                while(k):
                    res=res*10+k%10;
                    k=k//10;
                k=x*y
                while(k):
                    res=res*10+k%10;
                    k=k//10;
                ck=pan(res)
                if(ck==1):
                    ls.append(x*y)
print(*ls,sep=' ')
print(sum(set(ls)))
                
