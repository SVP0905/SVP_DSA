class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m,n=len(coins),amount+1
        dp=[float('inf')]*n
        dp[0]=0

        for i in range(len(coins)):
            new_dp=dp.copy()
            for j in range(1,n):
                if j>=coins[i]:
                    new_dp[j]=min(dp[j],1+new_dp[j-coins[i]])
            dp=new_dp

        return dp[n-1] if dp[n-1]!=float('inf') else -1 