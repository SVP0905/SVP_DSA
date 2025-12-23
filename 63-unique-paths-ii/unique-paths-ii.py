class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0

        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return 0

            if obstacleGrid[i][j]==1:
                return 0

            if i==m-1 and j==n-1:
                return 1
            
            path=0
            path+=dfs(i+1,j)
            path+=dfs(i,j+1)
            
            return path
        
        return dfs(0,0)

            
