class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m,n=len(dungeon),len(dungeon[0])
        # @cache
        # def dfs(i,j):
        #     if i==m-1 and j==n-1:
        #         return max(1,1-dungeon[i][j])
            
        #     if i>=m or j>=n:
        #         return float('inf')
            
        #     return max(1,min(dfs(i+1,j),dfs(i,j+1))-dungeon[i][j])
        
        # return dfs(0,0)

        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            dp[i][n]=float('inf')
        
        for j in range(n):
            dp[m][j]=float('inf')
        

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[i][j]=max(1,1-dungeon[i][j])
                else:
                    dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
        
        return dp[0][0]