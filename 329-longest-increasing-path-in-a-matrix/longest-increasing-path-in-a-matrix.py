class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        @cache
        def dfs(i,j):
            cnt=1
            for dr,dc in directions:
                nr,nc=dr+i,dc+j
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[i][j]:
                    cnt=max(cnt,1+dfs(nr,nc))
            
            return cnt
        

        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j))
        
        return res
            