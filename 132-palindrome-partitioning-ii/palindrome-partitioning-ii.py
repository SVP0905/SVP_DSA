class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[float('inf')]*(n+1)
        dp[n]=-1

        for i in range(n-1,-1,-1):
            for j in range(1,n-i+1):
                substr=s[i:i+j]
                if substr==substr[::-1]:
                    dp[i]=min(dp[i],1+dp[i+j])
        
        return dp[0]