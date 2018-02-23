dp = [[-1 for i in range(101)] for j in range(101)]
def ways(prev,left):
    ct=0;
    if(left==0):
        return 1;
    for i in range(prev,left+1):
        if(dp[i][left-i]==-1):
            dp[i][left-i]=ways(i,left-i);
        ct=ct+dp[i][left-i];
    return ct;
n=100;
x=0
for j in range(1,n):
    if(dp[j][n-j]==-1):
        dp[j][n-j]=ways(j,n-j);
    x=x+dp[j][n-j];
print(x)
