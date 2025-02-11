class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)+1
        total_sum=sum(nums)
        dp_size=2*total_sum+1

        dp=[0]*dp_size
        dp[total_sum]=1

        for num in nums:
            next_dp=[0]*dp_size
            for j in range(dp_size):
                if dp[j]>0:
                    if j+num<dp_size:
                        next_dp[j+num]+=dp[j]
                    if j-num>=0:
                        next_dp[j-num]+=dp[j]
            dp=next_dp
        
        final_idx=total_sum+target

        if final_idx<0 or final_idx>=dp_size:
            return 0
        return dp[final_idx]
        