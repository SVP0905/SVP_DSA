class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(sum_):
            if sum_==target:
                return 1
            
            if sum_>target:
                return 0
            
            total=0
            for num in nums:
                total+=dfs(sum_+num)
            
            return total

        return dfs(0)