class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<2:
            return 0
            
        dp=[0]*n    
        res=float('-inf')
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=(dp[i-2] if i>=2 else 0)+2
                elif i-1-dp[i-1]>=0 and s[i-1-dp[i-1]]=="(":
                    dp[i]=2+dp[i-1]+(dp[i-1-dp[i-1]-1] if i-1-dp[i-1]-1>=0 else 0)

            res=max(res,dp[i])
        return res