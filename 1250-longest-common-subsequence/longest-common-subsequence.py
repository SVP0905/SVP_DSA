class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            
            t1,t2,t3=0,0,0
            if text1[i]==text2[j]:
                t1+=1+dfs(i+1,j+1)
            t2+=dfs(i+1,j)
            t3+=dfs(i,j+1)

            return max(t1,t2,t3)
        
        return dfs(0,0)