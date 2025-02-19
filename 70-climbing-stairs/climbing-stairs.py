class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def dfs(i):
            if i==0:
                return 1
            if i==1:
                return 1
            if i in memo:
                return memo[i]

            left=dfs(i-1)
            right=dfs(i-2)

            memo[i]=left+right 

            return memo[i]
        
        return dfs(n)