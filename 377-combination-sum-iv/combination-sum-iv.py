class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo={}
        def dfs(target):
            if target==0:
                return 1
            if target<0:
                return 0
            if target in memo:
                return memo[target]
            
            count=0
            for n in nums:
                count+=dfs(target-n)

            memo[target]=count
            return memo[target ]

        return dfs(target) 
