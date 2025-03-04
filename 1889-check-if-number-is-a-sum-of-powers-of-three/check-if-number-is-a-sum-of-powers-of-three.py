class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def dfs(power,n):
            if n==0:
                return True
            if 3**power>n:
                return False
            
            include=dfs(power+1,n-3**power)
            skip=dfs(power+1,n)

            return include or skip
        
        return dfs(0,n)