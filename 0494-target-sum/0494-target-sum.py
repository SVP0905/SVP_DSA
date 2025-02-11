class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def dfs(i,cur_sum,count):
            if i>=len(nums):
                return 1 if cur_sum==target else 0
            
            if (i,cur_sum) in cache:
                return cache[(i,cur_sum)]
            
            cache[(i,cur_sum)]=dfs(i+1,cur_sum+nums[i],count)+dfs(i+1,cur_sum-nums[i],count)

            return cache[(i,cur_sum)]
        return dfs(0,0,0)