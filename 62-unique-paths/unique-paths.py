class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions=[(1,0),(0,1)]

        @cache
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            
            path=0
            for dr,dc in directions:
                new_dr,new_dc=i+dr,j+dc
                if 0<=new_dr<m and 0<=new_dc<=n:
                    path+=dfs(new_dr,new_dc)
            
            return path
        
        return dfs(0,0)
            