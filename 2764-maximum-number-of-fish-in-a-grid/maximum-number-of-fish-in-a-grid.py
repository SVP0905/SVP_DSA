class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        max_=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]>0 and (r,c) not in visited:
                    visited.add((r,c))
                    q=deque([(r,c)])
                    cur=0
                    while q:
                        x,y=q.popleft()
                        cur+=grid[x][y]
                        for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                            new_dr,new_dc=dr+x,dc+y
                            if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc]>0 and (new_dr,new_dc) not in visited:
                                q.append((new_dr,new_dc))
                                visited.add((new_dr,new_dc))
                    
                    max_=max(max_,cur)
        
        return max_