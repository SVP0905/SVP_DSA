class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        grid=image
        m,n=len(grid),len(grid[0])
        pixel=grid[sr][sc]

        if pixel==color:
            return grid 
            
        grid[sr][sc]=color
        q=deque([(sr,sc)])

        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    new_dr,new_dc=dr+r,dc+c
                    if 0<=new_dr<m and 0<=new_dc<n and grid[new_dr][new_dc]==pixel:
                        grid[new_dr][new_dc]=color
                        q.append((new_dr,new_dc))

        return grid