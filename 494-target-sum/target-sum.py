class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @cache
        def dfs(i,sum_):
            if i>=n:
                if sum_==target:
                    return 1
                else:
                    return 0

            add=dfs(i+1,sum_+nums[i])
            sub=dfs(i+1,sum_-nums[i])

            return add+sub
        
        return dfs(0,0)