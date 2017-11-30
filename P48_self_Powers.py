mo=10000000000
lol=0
for i in range(1,1000):
    x=1
    for j in range(1,i+1):
        x=(x*i)%mo
    lol=(lol+x)%mo
print(lol)
    
