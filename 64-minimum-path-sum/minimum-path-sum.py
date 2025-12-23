class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return float('inf')
            
            if i==m-1 and j==n-1:
                return grid[i][j]
            
            return min(grid[i][j]+dfs(i+1,j),grid[i][j]+dfs(i,j+1))

        
        return dfs(0,0)