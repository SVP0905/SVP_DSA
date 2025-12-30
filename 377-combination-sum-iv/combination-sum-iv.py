class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(cur_sum):
            if cur_sum==target:
                return 1
            if cur_sum>target:
                return 0
            
            cnt=0
            for num in nums:
                cnt+=dfs(cur_sum+num)
            
            return cnt
        
        return dfs(0)