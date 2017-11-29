k=0
ans=1;
j=0;
for i in range(1,1000000):
    x=str(i)
    for m in range(len(x)):
        k=k+1
        s=int(x[m])
        if(k==10**j):
            j=j+1
            ans=ans*s
    if(k>1000000):
        break
print(ans)
