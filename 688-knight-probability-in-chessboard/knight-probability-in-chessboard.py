class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions=[
            (-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)
        ]
        @cache
        def dfs(i,j,moves_left):
            if i<0 or j<0 or i>=n or j>=n:
                return 0

            if moves_left==0 and (i<n and j<n):
                return 1

            cnt=0
            for dr,dc in directions:
                cnt+=dfs(i+dr,j+dc,moves_left-1)

            return cnt/8
        
        return dfs(row,column,k)
