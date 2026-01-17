class Solution:
    def bfs(self,heights,starts):
        m,n=len(heights),len(heights[0])
        q=deque(starts)
        visited=set(starts)
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if 0<=nr<m and 0<=nc<n and heights[nr][nc]>=heights[r][c] and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
        
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific_border_cells=[]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pacific_border_cells.append((i,j))
        

        atlantic_border_cells=[]
        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    atlantic_border_cells.append((i,j))
        

        pacific=self.bfs(heights,pacific_border_cells)
        atlantic=self.bfs(heights,atlantic_border_cells)
        

        return list(pacific & atlantic)
        