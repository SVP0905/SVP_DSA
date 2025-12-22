class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        dp=[[0]*3 for _ in range(n+1)]

        for i in range(n-1,-1,-1):

            #buy
            buy=-prices[i]+dp[i+1][1]
            skip=dp[i+1][0]
            dp[i][0]=max(buy,skip)

            #sell
            sell=prices[i]+dp[i+1][2]
            skip=dp[i+1][1]
            dp[i][1]=max(sell,skip)

            #cooldown
            dp[i][2]=dp[i+1][0]


        return dp[0][0]