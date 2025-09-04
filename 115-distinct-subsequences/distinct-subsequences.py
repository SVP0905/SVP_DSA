class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        memo={}
        def dfs(i,j):
            if j>=n:
                return 1
            if i>=m:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            cnt=0
            
            if s[i]==t[j]:
                cnt+=dfs(i+1,j+1)

            cnt+=dfs(i+1,j)
            

            memo[(i,j)]=cnt

            return memo[(i,j)]
        
        return dfs(0,0)
        