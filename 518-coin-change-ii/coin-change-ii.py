class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i,sum_):
            if sum_==amount:
                return 1
            
            if i>=len(coins) or sum_>amount:
                return 0
            
            
            left=dfs(i,sum_+coins[i])
            right=dfs(i+1,sum_)
        
            return left+right
        
        return dfs(0,0)

            
