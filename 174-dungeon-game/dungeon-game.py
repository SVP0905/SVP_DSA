class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m,n=len(dungeon),len(dungeon[0])
        @cache
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return max(1,1-dungeon[i][j])
            
            if i>=m or j>=n:
                return float('inf')
            
            return max(1,min(dfs(i+1,j),dfs(i,j+1))-dungeon[i][j])
        
        return dfs(0,0)