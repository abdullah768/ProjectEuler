# your code goes here
# your code goes here
import math
fn=3/7;
#print(fn)
cls=0;
ans=0;
n=1000001
#n=8
for i in range(1,n):
	nm=fn*i;
	dn=i;
	x=int(math.floor(nm));
	cur=x/dn
	#print(i,cur,sep=' ')
	if(cur<fn and cur>cls and x<n and nm!=0):
		#lol=math.gcd(nm,dn);
		lol=1
		nm=nm/lol
		dn=dn/lol;
		cls=cur
		ans=nm 
print(ans)
		