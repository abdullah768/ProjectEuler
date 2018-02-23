import math;
def prm(nm):
	f=0;
	if(nm==1):
		return 1;
	ck=int(math.sqrt(nm))
	for i in range (2,ck+1):
		if((nm%i)==0):
			f=1;
			break;
	return f;
def fn(x,s):
	global ct,n
	n=100000000000000
	if(x>(n/10)):
		return;
	if(x<10):
		ct=0
	tm=int(x/s);
	if(prm(tm)==0):
		for i in range(10):
			y=10*x+i
			if(y<=n):
				if(prm(y)==0):
					ct=ct+y		
	for i in range(10):
		y=x*10+i
		sm=s+i;
		if((y%sm)==0):
			fn(y,sm)
fn(1,1)
ans=ct;
for j in range(2,10,2):
	fn(j,j)
	print(j,ct)
	ans=ans+ct
print(ans)