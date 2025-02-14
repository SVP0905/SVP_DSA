class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s)+1,len(t)+1
        dp=[[0]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0]=1

        for i in range(1,m):
            for j in range(1,n):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m-1][n-1]