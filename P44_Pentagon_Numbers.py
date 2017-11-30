pe=[]
for i in range(1,5000):
    pe.append(i*(3*i-1)//2)
a=0
pex=set(pe)
for i in range (len(pe)):
       for j in range (i-1,0,-1):
           if((pe[i]+pe[j]in pex) and (pe[i]-pe[j] in pex)):
               a=pe[i]-pe[j]
               break
       if(a!=0):
           break
print(a)
