class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)

        dp = [[False] * n for x in range(n)]

        count = 0

        for x in range(n):
            dp[x][x] = True
            count += 1

        for x in range(n-1):
            if(s[x] == s[x+1]):
                dp[x][x+1] = True
                count += 1

        
        for length in range(3,n+1):

            for i in range(n-length+1):
                j = i + length - 1

                if(s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        
        return count