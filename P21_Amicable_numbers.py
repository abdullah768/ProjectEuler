# cook your dish here
# your code goes here
import math
ct=0;
lol=[0]*100001
for i in range (2,10001):
    x=1;
    y=int(math.sqrt(i));
    for j in range (2,y+1):
        if(i%j==0):
            x=x+j;
            if(j!=i/j):
                x=x+int(i/j);
    lol[i]=x;
for i in range (2,10001):
    if(lol[i]>1 and lol[i]!=i):
        if(i==lol[lol[i]]):
            ct=ct+i;
print(ct)
