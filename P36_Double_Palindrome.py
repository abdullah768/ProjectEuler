ct=0
for i in range (1,1000000):
    x=str(i)[::-1]
    x1=str(i)
    y=str(bin(i))[2:]
    y1=str(y)[::-1]
    if(y==y1 and x==x1):
        ct=ct+i
print(ct)
