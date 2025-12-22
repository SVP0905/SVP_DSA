class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @cache
        # def dfs(i,state,no_of_trans):
        #     if no_of_trans>=2:
        #         return 0
            
        #     if i>=len(prices):
        #         return 0
            
        #     profit=0

        #     if state==0:
        #         buy=-prices[i]+dfs(i+1,1,no_of_trans)
        #         skip=dfs(i+1,state,no_of_trans)
        #         profit=max(buy,skip)
        #     elif state==1:
        #         sell=prices[i]+dfs(i+1,0,no_of_trans+1)
        #         skip=dfs(i+1,state,no_of_trans)
        #         profit=max(sell,skip)
            
        #     return profit
        
        # return dfs(0,0,0)

        n=len(prices)
        dp=[[[0]*2 for _ in range(3)] for _ in range(n+1)]
        no_of_transactions=2
        for i in range(n-1,-1,-1):
            for k in range(2):
                #buy
                buy=-prices[i]+dp[i+1][k][1]
                skip=dp[i+1][k][0]

                dp[i][k][0]=max(buy,skip)

                #sell
                sell=prices[i]+dp[i+1][k+1][0]
                skip=dp[i+1][k][1]
                dp[i][k][1]=max(sell,skip)
        
        return dp[0][0][0]
