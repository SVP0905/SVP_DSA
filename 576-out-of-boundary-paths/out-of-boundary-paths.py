class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD=10**9+7
        @cache
        def dfs(i,j,moves_left):
            if i<0 or i>=m or j<0 or j>=n:
                return 1

            if moves_left==0:
                return 0
            
            cnt=(dfs(i+1,j,moves_left-1)+dfs(i,j+1,moves_left-1)+dfs(i-1,j,moves_left-1)+dfs(i,j-1,moves_left-1))%MOD

            return cnt
        
        return dfs(startRow,startColumn,maxMove)

