class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m,n=len(coins)+1,amount+1
        dp=[[0]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]+=dp[i-1][j]
                if j>=coins[i-1]:
                    dp[i][j]+=dp[i][j-coins[i-1]]
        
        return dp[m-1][n-1]
        