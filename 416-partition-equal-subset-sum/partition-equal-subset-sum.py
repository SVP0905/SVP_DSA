class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)

        if total_sum%2!=0:
            return False
        
        target_sum=total_sum//2

        M,N=len(nums),target_sum
        dp=[False]*(N+1)
        dp[0]=True
        for i in range(1,M+1):
            for j in range(N,nums[i-1]-1,-1):
                dp[j]=dp[j-nums[i-1]] or dp[j]
        
        return dp[N]