from itertools import permutations
lt=10000
pr=[0]*10000
for i in range(2,lt):
    if(pr[i]==0):
        for j in range(i+i,lt,i):
            pr[j]=1
for i in range(1000,10000):
    if(pr[i]==0):
        x=str(i)
        lol=[]
        for p in permutations(x):
            p=''.join(p)
            if(pr[int(p)]==0):
                lol.append(int(p))
        zz=set(lol)
        lol=list(zz)
        lol.sort()
        for m in range (len(lol)):
            for n in range(m+1,len(lol)):
                for o in range(n+1,len(lol)):
                    if(lol[o]-lol[n]==lol[n]-lol[m]):
                        print(lol[m],lol[n],lol[o],sep=' ')
