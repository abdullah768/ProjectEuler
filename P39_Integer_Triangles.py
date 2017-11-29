ck=[0]*10000
for x in range(1,1001):
    if(x%20==0):
        print(x)
    for a in range(1,x):
        for b in range(1,x-a):
            c=x-a-b
            if(c<=0):
                break
            if((a*a+b*b)==c*c):
                ck[x]=ck[x]+1
ans=0
for i in range(1,1001):
    if(ck[i]>ck[ans]):
        ans=i
print(ans)
