lt=1000000
li=[]
prm=[0]*lt
for i in range(2,lt):
    if(prm[i]==0):
        for j in range(i+i,lt,i):
            prm[j]=prm[j]+1
for i in range(2,lt):
    if(prm[i]==prm[i+1]==prm[i+2]==prm[i+3]==4):
        break
print(i)
