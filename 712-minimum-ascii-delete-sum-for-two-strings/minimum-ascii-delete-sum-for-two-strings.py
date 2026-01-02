class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n=len(s1),len(s2)

        @cache
        def dfs(i,j):
            if i==m and j==n:
                return 0
            
            if i==m:
                return sum(ord(ch) for ch in s2[j:])
            
            if j==n:
                return sum(ord(ch) for ch in s1[i:])
            
            if s1[i]==s2[j]:
                return dfs(i+1,j+1)
            else:
                delete_s1=ord(s1[i])+dfs(i+1,j)
                delete_s2=ord(s2[j])+dfs(i,j+1)
                return min(delete_s1,delete_s2)
        
        return dfs(0,0)