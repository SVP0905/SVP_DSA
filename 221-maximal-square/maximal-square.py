class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            
            if matrix[i][j]=='0':
                return 0
            
            area=0
            if matrix[i][j]=='1':
                area=1+min(dfs(i+1,j),dfs(i+1,j+1),dfs(i,j+1))
            return area
        
        
        res=float('-inf')
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j))
        
        return res*res
