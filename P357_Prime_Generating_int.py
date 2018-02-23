import math
n=100000001
pr=[1]*n
pr[1]=0
pr[0]=0
for i in range(2,n):
    if(pr[i]==1):
        for j in range(i+i,n,i):
            pr[j]=0;
sm=1
val=[1]*n
for i in range(2,n):
    if(pr[i]==1):
        x=i*i;
        for j in range(x,n,x):
            val[j]=0;
for i in range(2,n-1,2):
    if(val[i]==1):
        if(pr[i+1]==1 and pr[(i//2)+2]==1):
           lt=int(math.sqrt(i))
           fl=1
           for j in range(2,lt+1):
               if(i%j==0):
                   if(pr[j+i//j]==0):
                       fl=0;
                       break;
           if(fl==1):
               sm=sm+i
print(sm)
