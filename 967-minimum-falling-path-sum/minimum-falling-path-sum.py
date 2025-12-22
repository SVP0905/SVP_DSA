class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,n=len(matrix),len(matrix)
        @cache
        def dfs(i,j):
            if j<0 or j>=n:
                return float('inf')

            if i==n-1:
                return matrix[i][j]
            
            
            return matrix[i][j]+min(dfs(i+1,j-1),dfs(i+1,j),dfs(i+1,j+1))
        
        
        res=float('inf')
        for i in range(n):
            res=min(res,dfs(0,i))
        
        return res