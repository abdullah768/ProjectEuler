import math
def chk(x):
    th="1234567890";
    n=str(x*x);
   # print(n)
    f=0;
    for j in range (10):
        #print (th[j],n[j*2+1])
        if(th[j]!=n[j*2]):
            f=1;
            break;
    return f;
for i in range(int(math.sqrt(10203040506070809)),10000000000000):
    if(chk(i*10)==0):
        print(i)
        break
