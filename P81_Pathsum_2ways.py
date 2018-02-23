# your code goes here
mx=9999999999
dp = [[mx for i in range(100)] for j in range(100)]
ar=[[int(j) for j in input().split(',')] for i in range(80)]
def cal(i,j):
	if(dp[i][j]!=mx):
		return dp[i][j];
	if(i==79 and j==79):
		dp[i][j]=ar[i][j];
	elif(i==79):
		dp[i][j]=ar[i][j]+cal(i,j+1)
	elif(j==79): 
		dp[i][j]=ar[i][j]+cal(i+1,j)
	else:
		dp[i][j]=min(ar[i][j]+cal(i+1,j),ar[i][j]+cal(i,j+1))
	return dp[i][j]
print(cal(0,0))