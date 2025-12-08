class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set=set(nums)

        def dfs(cur_s):
            if len(cur_s)>=len(nums):
                if cur_s not in num_set:
                    return cur_s
                else:
                    return None
            
            res=dfs(cur_s+'0')
            if res: return res

            res=dfs(cur_s+'1')
            if res: return res

            return None
        
        return dfs('')