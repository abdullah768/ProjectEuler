from itertools import permutations
import math
perms = [''.join(p) for p in permutations('1234567')]
ct=0
for i in perms:
    x=int(i)
    y=int(math.sqrt(x))
    f=0
    for j in range(2,y+1):
        if(x%j==0):
            f=1
            break
    if(f==0 and x>ct):
        ct=x
print(ct)
