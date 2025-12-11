class Solution:
    def minCut(self, s: str) -> int:
        res=0

        @cache
        def dfs(start_idx):
            if start_idx==len(s):
                #if we reached the end then we need 0 cuts
                return 0
            
            mincuts=float('inf')
            for j in range(start_idx,len(s)):
                chunk=s[start_idx:j+1]
                if chunk==chunk[::-1]:
                    if j==len(s)-1:
                        mincuts=0
                    else:
                        cuts=1+dfs(j+1)
                        mincuts=min(mincuts,cuts)

            
            return mincuts
        
        return dfs(0)