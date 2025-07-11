class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh_cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh_cnt+=1
        
        if fresh_cnt==0:
            return 0
        
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        res=0
        while q:
            q_len=len(q)
            rotten=False
            for i in range(q_len):
                x,y=q.popleft()
                for dx,dy in directions:
                    new_x,new_y=x+dx,y+dy
                    if (0<=new_x<m and 0<=new_y<n and grid[new_x][new_y]==1):
                        q.append((new_x,new_y))
                        grid[new_x][new_y]=2
                        fresh_cnt-=1
                        rotten=True
            
            if rotten==True:
                res+=1
        
        return res if fresh_cnt==0 else -1
            
        
        