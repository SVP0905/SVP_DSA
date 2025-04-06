class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        dp=[[n] for n in nums]
        res=[]

        for i in reversed(range(n)):
            for j in range(i+1,n):
                if nums[j]%nums[i]==0:
                    tmp=[nums[i]]+dp[j]
                    dp[i]=tmp if len(tmp)>len(dp[i]) else dp[i]
            res=res if len(res)>len(dp[i]) else dp[i]


        return res
