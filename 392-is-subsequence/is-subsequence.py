class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(s_idx,t_idx):
            if s_idx==len(s):
                return True
            
            if t_idx==len(t):
                return False
            
            if s[s_idx]==t[t_idx]:
                return dfs(s_idx+1,t_idx+1)
            else:
                return dfs(s_idx,t_idx+1)
        
        return dfs(0,0)