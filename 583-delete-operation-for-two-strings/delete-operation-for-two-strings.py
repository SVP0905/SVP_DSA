class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)

        @cache
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            
            cnt=0
            if word1[i]==word2[j]:
                cnt+=dfs(i+1,j+1)+1
            else:
                cnt+=max(dfs(i+1,j),dfs(i,j+1))
            
            return cnt
        
        LCS=dfs(0,0)
        res=(m-LCS)+(n-LCS)

        return res
            