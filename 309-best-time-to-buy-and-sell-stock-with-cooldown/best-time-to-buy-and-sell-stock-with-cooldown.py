class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i,state):
            if i>=len(prices):
                return 0
            
            if (i,state) in memo:
                return memo[(i,state)]
                
            if state==0:
                buy=-prices[i]+dfs(i+1,1)
                skip=dfs(i+1,state)
                memo[(i,state)]=max(buy,skip)
            elif state==1:
                sell=prices[i]+dfs(i+1,2)
                skip=dfs(i+1,state)
                memo[(i,state)]=max(sell,skip)
            else:
                memo[(i,state)]=dfs(i+1,0)
            


            return memo[(i,state)]
        
        return dfs(0,0)
