class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        @cache
        def dfs(sum_):
            if sum_==amount:
                return 0
            if sum_>amount:
                return float('inf')

            min_=float('inf')
            for coin in coins:
                res=dfs(sum_+coin)
                if res!=float('inf'):
                    min_=min(min_,1+res)

            return min_
        
        res=dfs(0)
        return res if res!=float('inf') else -1