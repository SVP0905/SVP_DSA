class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m,n=len(coins)+1,amount+1
        dp=[[float('inf')]*n for _ in range(m)]

        for i in range(m):
            dp[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]
                if j>=coins[i-1]:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
        return dp[m-1][n-1] if dp[m-1][n-1]!=float('inf') else -1