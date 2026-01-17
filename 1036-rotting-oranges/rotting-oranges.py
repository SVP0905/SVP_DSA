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

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        time=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,dc+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr,nc))
            time+=1

        if fresh==0:
            return time-1
        else:
            return -1
