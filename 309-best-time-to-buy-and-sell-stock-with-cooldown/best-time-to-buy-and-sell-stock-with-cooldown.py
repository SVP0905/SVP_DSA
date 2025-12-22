class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i,state):
            if i>=len(prices):
                return 0
            
            profit=0
            if state==0:
                buy=-prices[i]+dfs(i+1,1)
                skip=dfs(i+1,state)
                profit=max(buy,skip)
            elif state==1:
                sell=prices[i]+dfs(i+1,2)
                skip=dfs(i+1,state)
                profit=max(sell,skip)
            else:
                profit=dfs(i+1,0)
            


            return profit
        
        return dfs(0,0)
