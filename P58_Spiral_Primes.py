import math
x=0
val=1
for i in range (1,50001):
    for j in range (1,5):
        val=val+2*i
        y=int(math.sqrt(val))
        f=0
        for k in range(2,y+1):
            if(val%k==0):
                f=1
                break
        if(f==0):
            x=x+1
    t=(i)*4+1;
    #print(x,t,sep=' ')
    if(x/t<0.1):
        break
print(x,t)
print(2*i+1)
