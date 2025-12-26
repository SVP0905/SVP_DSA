class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        @cache
        def dfs(i,j,prev):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if matrix[i][j]<=prev:
                return 0
            
            cnt=1
            for dr,dc in directions:
                if matrix[i][j]>prev:
                    cnt=max(cnt,1+dfs(i+dr,j+dc,matrix[i][j]))
            
            return cnt
        
        res=float('-inf')
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j,-1))
        
        return res
