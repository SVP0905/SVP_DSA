class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[(0,1),(1,0)]
        @cache
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return grid[i][j]
            
            if i>=m or j>=n:
                return float('inf')
            
            return grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
        
        return dfs(0,0)

            
