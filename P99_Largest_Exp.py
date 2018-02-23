import math
# your code goes here
n=1000;
mx=0;
ind=0
tst=10000000000
for i in range(n):
	x=[int(j) for j in input().split(',')]
	tmp=math.log(tst,x[0]);
	lol=x[1]/tmp;
	if(lol>mx):
		mx=lol
		ind=i+1
print(ind)