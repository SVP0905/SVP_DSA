class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1)+1,len(text2)+1
        dp=[0]*n

        for i in range(1,m):
            new_dp=dp.copy()
            for j in range(1,n):
                if text1[i-1]==text2[j-1]:
                    new_dp[j]=1+dp[j-1]
                else:
                    new_dp[j]=max(new_dp[j-1],dp[j])
            dp=new_dp
        return dp[n-1]