coin=[1,2,5,10,20,50,100,200]
dp=[0]*1000
dp[0]=1;
for i in range(0,8):
    for j in range(coin[i],201):
        dp[j]=dp[j]+dp[j-coin[i]]
print (dp[200])
