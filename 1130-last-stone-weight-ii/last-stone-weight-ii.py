class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dfs(i,cur_val):
            if i>=len(stones):
                return abs(cur_val)
            
            add=dfs(i+1,cur_val+stones[i])
            sub=dfs(i+1,cur_val-stones[i])

            return min(add,sub)
        
        return dfs(0,0)