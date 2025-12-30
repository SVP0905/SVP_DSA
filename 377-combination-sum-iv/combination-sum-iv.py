class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)

        dp[0]=1


        for a in range(1,target+1):
            for num in nums:
                if a-num>=0:
                    dp[a]+=dp[a-num]
        
        return dp[target]
