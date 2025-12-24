class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        
        @cache
        def dfs(i,j,health):
            if i>=m or j>=n:
                return False

            health+=dungeon[i][j]

            if health<=0:
                return False
            
            if i==m-1 and j==n-1 and health>0:
                return True
            
            if dfs(i+1,j,health) or dfs(i,j+1,health):
                return True
            
            return False


        for hp in range(1,100000):
            if dfs(0,0,hp):
                return hp

