ma=0
for i in range(1,10000000):
    j=str(i)
    t=''.join(sorted(j))
    f=0
    for k in range(2,7):
        x=''.join(sorted(str(i*k)))
        if(x!=t):
            f=1
            break;
    if(f==0):
        break
print(i)
