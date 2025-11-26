class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD=10**9+7
        m,n=len(grid),len(grid[0])
        directions=[(1,0),(0,1)]


        @cache
        def dfs(i,j,rem):
            new_rem=(rem+grid[i][j])%k

            if i==m-1 and j==n-1 and new_rem==0:
                return 1

            cnt=0
            for r,c in directions:
                dr,dc=i+r,j+c
                if 0<=dr<m and 0<=dc<n:
                    cnt+=dfs(dr,dc,new_rem)

            return cnt
        
        return dfs(0,0,0)%MOD

            
