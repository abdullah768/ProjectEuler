sum=0;
for i in range (1,100):
    f=0;
    for j in range(1,10):
        lol=j**i;
        if(len(str(lol))==i):
            sum=sum+1;
print(sum)
