class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i<0 and j<0:
                return True
            
            if j<0:
                return False
            
            if i<0:
                return all(p[x]=="*" for x in range(j+1))
            
            if p[j]=='?':
                memo[(i,j)]=dfs(i-1,j-1)
            elif p[j]=="*":
                memo[(i,j)]=dfs(i-1,j) or dfs(i,j-1)
            else:
                memo[(i,j)]=s[i]==p[j] and dfs(i-1,j-1)

            return memo[(i,j)]

        return dfs(m-1,n-1)            

        