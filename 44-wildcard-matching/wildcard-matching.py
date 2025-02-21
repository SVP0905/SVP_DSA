class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s)+1,len(p)+1
        dp=[[False]*n for _ in range(m)]
        dp[0][0]=True

        for j in range(1,n):
            if p[j-1]=="*":
                dp[0][j]=dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                if p[j-1]=="*":
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
        
        return dp[m-1][n-1]