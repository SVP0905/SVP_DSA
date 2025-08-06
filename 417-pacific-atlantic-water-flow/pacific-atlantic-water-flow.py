class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific,atlantic=[],[]

        for j in range(n):
            pacific.append((0,j))
            atlantic.append((m-1,j))
        for i in range(m):
            pacific.append((i,0))
            atlantic.append((i,n-1))

        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(start_cells):
            visited=set()
            stack=start_cells[:]

            while stack:
                r,c=stack.pop()
                visited.add((r,c))
                for dr,dc in directions:
                    new_dr,new_dc=dr+r,dc+c
                    if (0<=new_dr<m and 0<=new_dc<n and heights[new_dr][new_dc]>=heights[r][c] and (new_dr,new_dc) not in visited):
                        stack.append((new_dr,new_dc))
                        visited.add((new_dr,new_dc))
            return visited
        
        pacific_cells=dfs(pacific)
        atlantic_cells=dfs(atlantic)

        res=[]
        for cell in pacific_cells:
            if cell in atlantic_cells:
                res.append([cell[0],cell[1]])

        return res
