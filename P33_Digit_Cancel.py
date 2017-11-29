import math
prod1=1;
prod2=1;
for i in range (1,100):
    for j in range (i+1,100):
        #print(prod)
        n1=i%10;
        n2=i//10
        d1=j%10
        d2=j//10
        x=math.gcd(i,j)
        a1=i//x;
        a2=j//x
        if(n1==0 or d1==0 or n2==0 or d2==0):
            continue
        if(n1==d1):
            x=math.gcd(n2,d2)
            t1=n2//x
            t2=d2//x
            if(a1==t1 and a2==t2):
                prod1=prod1*a1
                prod2=prod2*a2
                continue
        if(n1==d2):
            x=math.gcd(n2,d1)
            t1=n2//x
            t2=d1//x
            if(a1==t1 and a2==t2):
                prod1=prod1*a1
                prod2=prod2*a2
                continue
        if(n2==d1):
            x=math.gcd(n1,d2)
            t1=n1//x
            t2=d2//x
            if(a1==t1 and a2==t2):
                prod1=prod1*a1
                prod2=prod2*a2
                continue
        if(n2==d2):
            x=math.gcd(n1,d1)
            t1=n1//x
            t2=d1//x
            if(a1==t1 and a2==t2):
                prod1=prod1*a1
                prod2=prod2*a2
                continue
x=math.gcd(prod1,prod2)
prod1=prod1/x
prod2=prod2/x
print(prod2)
