def pan(x):
    dig=[0]*10
    while(x):
        y=x%10
        dig[y]=dig[y]+1
        x=x//10
    if(dig[0]>0):
        return 0
    for i in range (1,10):
        if(dig[i]!=1):
            return 0
    return 1

us=[0,1,2,3,4,5,6,7,8,9]
s=[]
for d1 in us:
    us.remove(d1)
    for d2 in us:
        #print(d1,d2,sep=' ')
        us.remove(d2)
        for d3 in us:
            us.remove(d3)
            for d4 in us:
                if((d2*100+d3*10+d4)%2==0):
                    us.remove(d4)
                    for d5 in us:
                        if((d3*100+d4*10+d5)%3==0):
                            us.remove(d5)
                            for d6 in us:
                                if((d4*100+d5*10+d6)%5==0):
                                    us.remove(d6)
                                    for d7 in us:
                                        if((d5*100+d6*10+d7)%7==0):
                                            us.remove(d7)
                                            for d8 in us:
                                                if((d6*100+d7*10+d8)%11==0):
                                                    us.remove(d8)
                                                    for d9 in us:
                                                        if((d7*100+d8*10+d9)%13==0):
                                                            us.remove(d9)
                                                            for d10 in us:
                                                                if((d8*100+d9*10+d10)%17==0):
                                                                    s.append(str(d10)+str(d9)+str(d8)+str(d7)+str(d6)+str(d5)+str(d4)+str(d3)+str(d2)+str(d1))
                                                            us.append(d9)
                                                            us.sort()
                                                    us.append(d8)
                                                    us.sort()
                                            us.append(d7)
                                            us.sort()
                                    us.append(d6)
                                    us.sort()
                            us.append(d5)
                            us.sort()
                    us.append(d4)
                    us.sort()
            us.append(d3)
            us.sort()
        us.append(d2)
        us.sort()
    us.append(d1)
    us.sort()
for i in range(len(s)):
    s[i]=int(s[i][::-1])
print(sum(s))

                        
    
