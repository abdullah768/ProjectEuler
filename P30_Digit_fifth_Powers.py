n=0;
po=[]
for i in range(0,11):
    po.append(int(i**5))
for i in range (10,300001):
    k=i
    lol=0;
    while(k>0):
        x=int(k%10);
        lol=lol+po[x]
        k=k//10
    if(lol==i):
        n=n+i
print(n)
