class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n=len(s1),len(s2)

        if (m+n)!=len(s3):
            return False
        
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[m][n]=True

        for j in range(n-1,-1,-1):
            if s2[j]==s3[j+m]:
                dp[m][j]=dp[m][j+1]
        
        for i in range(m-1,-1,-1):
            if s1[i]==s3[i+n]:
                dp[i][n]=dp[i+1][n]
        

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i]==s3[i+j]:
                    dp[i][j]|=dp[i+1][j]
                if s2[j]==s3[i+j]:
                    dp[i][j]|=dp[i][j+1]
        
        return dp[0][0]