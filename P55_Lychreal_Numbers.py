ct=0
for i in range(1,10000):
    x=str(i)
    for j in range(51):
        t=x[::-1]
        z=int(x)+int(t)
        if(str(z)[::-1]==str(z)):
            break
        x=str(z)
    if(j>=49):
        ct=ct+1;
print(ct)
