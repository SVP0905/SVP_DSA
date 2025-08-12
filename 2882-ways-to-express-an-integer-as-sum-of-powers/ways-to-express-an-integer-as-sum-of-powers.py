class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD=10**9+7
        @cache
        def dfs(num,cur_sum):
            if cur_sum==n:
                return 1
            if cur_sum>n or num**x>n-cur_sum:
                return 0
            
            val=num**x
            left=dfs(num+1,cur_sum+val)
            right=dfs(num+1,cur_sum)

            return (left+right)%MOD
        
        return dfs(1,0)