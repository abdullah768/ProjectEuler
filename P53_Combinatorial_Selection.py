f=[0]*1000
f[0]=1;
for i in range (1,101):
    f[i]=f[i-1]*i
ct=0
for n in range (1,101):
    for r in range(1,n+1):
        c=f[n]/f[r]
        c=c/f[n-r]
        if(c>1000000):
            ct=ct+1
print(ct)
