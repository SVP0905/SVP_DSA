class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        res=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res+=4
                    for dr,dc in [[-1,0],[0,-1]]:
                        new_dr,new_dc=dr+i,dc+j
                        if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc]==1:
                            res-=2
        
        return res