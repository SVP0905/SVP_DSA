class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        cost=[[float('inf')]*n for _ in range(m)]
        cost[-1][-1]=0 #cost of reaching last cell(m-1,n-1) is 0
        tcost=[float('inf')]*(max(max(row) for row in grid)+1)

        for t in range(k+1):
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    #move down
                    if i+1<m:
                        cost[i][j]=min(cost[i][j],cost[i+1][j]+grid[i+1][j])

                    #move right
                    if j+1<n:
                        cost[i][j]=min(cost[i][j],cost[i][j+1]+grid[i][j+1])

                    #teleport
                    if t>0:
                        cost[i][j]=min(cost[i][j],tcost[grid[i][j]])
            

            #calculate telport cost for next iteration
            for i in range(m):
                for j in range(n):
                    tcost[grid[i][j]] = min(tcost[grid[i][j]], cost[i][j])


            #prefix-min computation
            for i in range(1,len(tcost)):
                tcost[i]=min(tcost[i],tcost[i-1])
        

        return cost[0][0]


