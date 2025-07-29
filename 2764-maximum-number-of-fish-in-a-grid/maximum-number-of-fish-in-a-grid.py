class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        max_=0
        visited=set()
        for r in range(m):
            for c in range(n):
                if grid[r][c]>0 and (r,c) not in visited:
                    cur=0
                    q=deque([(r,c)])
                    visited.add((r,c))
                    while q:
                        x,y=q.popleft()
                        cur+=grid[x][y]
                        directions=[(0,1),(1,0),(0,-1),(-1,0)]
                        for dr,dc in directions:
                            new_dr,new_dc=dr+x,dc+y
                            if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc] and (new_dr,new_dc) not in visited:
                                visited.add((new_dr,new_dc))
                                q.append((new_dr,new_dc))
                    

                    max_=max(max_,cur)
        
        return max_