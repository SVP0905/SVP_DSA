class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
            
        directions=[(0,1),(1,0)]
        @cache
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            
            
            path=0
            for dr,dc in directions:
                new_dr,new_dc=dr+i,dc+j
                if 0<=new_dr<m and 0<=new_dc<n and obstacleGrid[new_dr][new_dc]==0:
                    path+=dfs(new_dr,new_dc)
            
            return path
        
        return dfs(0,0)

            
