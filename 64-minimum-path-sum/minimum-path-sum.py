class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        cost=[[float('inf')]*n for _ in range(m)]

        cost[-1][-1]=grid[-1][-1]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                #move right
                if j+1<n:
                    cost[i][j]=min(cost[i][j],cost[i][j+1]+grid[i][j])
                
                #move down
                if i+1<m:
                    cost[i][j]=min(cost[i][j],cost[i+1][j]+grid[i][j])
        
        return cost[0][0]