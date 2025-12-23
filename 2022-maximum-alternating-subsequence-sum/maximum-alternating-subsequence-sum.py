class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def dfs(i,flag):
            if i==len(nums):
                return 0
            
            val=nums[i] if flag else -nums[i]
            pick=val+dfs(i+1,not flag)

            skip=dfs(i+1,flag)

            return max(pick,skip)
        
        return dfs(0,True)