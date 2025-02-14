class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s)+1,len(t)+1
        dp=[0]*n
        dp[0]=1

        for i in range(1,m):
            new_dp=dp.copy()
            for j in range(1,n):
                if s[i-1]==t[j-1]:
                    new_dp[j]=dp[j]+dp[j-1]
                else:
                    new_dp[j]=dp[j]
            dp=new_dp

        return dp[n-1]