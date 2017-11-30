lt=1000000
prm=[1]*lt
ck=[0]*lt
prm[0]=0
prm[1]=0
for i in range(2,lt):
    if(prm[i]==1):
        for j in range(i+i,lt,i):
            prm[j]=0
li=[]
for i in range(1,lt):
    if(prm[i]==1):
       li.append(i)
for i in range(len(li)):
    x=0
    for j in range(i,len(li)):
        x=x+li[j]
        if(x>=lt):
            break
        if(ck[x]<j-i+1 and prm[x]==1):
            ck[x]=j-i+1
x=0
for i in range(lt):
    if(ck[i]>ck[x]):
        x=i
print(x)
        
