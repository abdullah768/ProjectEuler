# your code goes here
n=1000001;
#n=10
sv=[1]*n;
pr=[1]*n;
for i in range (1,n):
	sv[i]=i;
for i in range(2,n):
	if(pr[i]==1):
		x=(1-(1/i))
		for j in range(i,n,i):
			pr[j]=0;
			sv[j]=sv[j]*x 
	sv[i]=i/sv[i]
sv[1]=0;
z=1
for i in range(2,n):
	#print(i,sv[i],sep=' ')
	if(sv[i]>sv[z]):
		z=i;
print(z)