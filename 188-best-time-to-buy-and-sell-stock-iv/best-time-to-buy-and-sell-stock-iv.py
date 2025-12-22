class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dfs(i,state,no_of_trans):
            if no_of_trans>=k:
                return 0
            
            if i>=len(prices):
                return 0
            
            profit=0

            if state==0:
                buy=-prices[i]+dfs(i+1,1,no_of_trans)
                skip=dfs(i+1,state,no_of_trans)
                profit=max(buy,skip)
            elif state==1:
                sell=prices[i]+dfs(i+1,0,no_of_trans+1)
                skip=dfs(i+1,state,no_of_trans)
                profit=max(sell,skip)
            
            return profit
        
        return dfs(0,0,0)
            