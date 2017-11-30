lt=10000
pr=[1]*lt
ck=[0]*lt
sq=[]
for i in range(2,lt):
    if(pr[i]==1):
        for j in range(i+i,lt,i):
            pr[j]=0
for i in range (1,10000):
    sq.append(2*i*i)
for i in range(2,lt):
    if(pr[i]==1):
        for j in range(0,10000):
            x=i+sq[j]
            if(x>=lt):
                break
            ck[x]=1
        ck[i]=1
for i in range(2,lt):
    if(i%2==1 and ck[i]==0):
        ans=i
        break
print(ans)
