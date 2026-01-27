class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.cost=0
        def dfs(i):
            nonlocal cost

            if i>n:
                return 0
            
            left=dfs(2*i)
            right=dfs(2*i+1)
            self.cost+=abs(left-right)
            return cost[i-1]+max(left,right)

        dfs(1)

        return self.cost