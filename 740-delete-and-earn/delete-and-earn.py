class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values=[0]*(max(nums)+1)

        for num in nums:
            values[num]+=num
        
        dp=[0]*len(values)
        dp[0]=values[0]
        dp[1]=max(values[0],values[1])

        for i in range(2,len(values)):
            dp[i]=max(dp[i-1],values[i]+dp[i-2])
        
        return dp[-1]