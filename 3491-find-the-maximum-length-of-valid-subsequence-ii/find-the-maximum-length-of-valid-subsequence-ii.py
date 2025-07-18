class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        # def solve_dfs(val):
        #     dp=[1]*len(nums)
        #     for i in range(1,len(nums)):
        #         for j in range(i):
        #             if (nums[i]+nums[j])%k==val:
        #                 dp[i]=max(dp[i],dp[j]+1)
            
        #     return max(dp)

        # max_=0
        # for i in range(k):
        #     max_=max(max_,solve_dfs(i))
        # return max_

        n=len(nums)
        dp=[[1]*n for _ in range(k)]
        
        max_=0

        for i in range(1,n):
            for j in range(i):
                val=(nums[i]+nums[j])%k
                dp[val][i]=max(dp[val][i],dp[val][j]+1)
                max_=max(max_,dp[val][i])
        return max_
        