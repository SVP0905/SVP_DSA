class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
        
        res=0
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            q_len=len(q)
            rotten=False
            for _ in range(q_len):
                x,y=q.popleft()
                for dr,dy in directions:
                    new_x,new_y=dr+x,dy+y
                    if (0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]==1):
                        grid[new_x][new_y]=2
                        q.append((new_x,new_y))
                        fresh-=1
                        rotten=True
            
            if rotten==True:
                res+=1
        
        return res if fresh==0 else -1 