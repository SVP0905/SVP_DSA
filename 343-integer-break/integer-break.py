class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dfs(num):
            if num<=1:
                return 1
            
            max_prod=0
            for i in range(1,num):
                val=max(i*(num-i),i*dfs(num-i))
                max_prod=max(max_prod,val)
            
            return max_prod
        
        return dfs(n)