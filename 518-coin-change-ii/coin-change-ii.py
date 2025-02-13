class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m,n=len(coins),amount+1
        dp=[0]*n
        dp[0]=1

        for i in range(m):
            new_dp=dp.copy()
            for j in range(1,n):
                if j>=coins[i]:
                    new_dp[j]+=new_dp[j-coins[i]]
            dp=new_dp
        
        return dp[n-1]

        