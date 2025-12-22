class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m,n=len(triangle),len(triangle[-1])
        @cache
        def dfs(i,j):
            if i==m-1:
                return triangle[i][j]
            
            
            if i>=m and j>=n:
                return float('inf')
            

            return triangle[i][j]+min(dfs(i+1,j),dfs(i+1,j+1))
        
        return dfs(0,0)