class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        fresh=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        res=0
        while q:
            q_len=len(q)
            rotten=False
            for _ in range(q_len):
                x,y=q.popleft()
                for dr,dc in directions:
                    new_dr,new_dc=dr+x,dc+y
                    if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc]==1:
                        grid[new_dr][new_dc]=2
                        fresh-=1
                        q.append((new_dr,new_dc))
                        rotten=True

            if rotten==True:
                res+=1
        
        return res if fresh==0 else -1
                    

        