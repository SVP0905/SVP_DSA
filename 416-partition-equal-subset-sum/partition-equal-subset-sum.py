class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False

        req=sum(nums)//2
        n=len(nums)
        dp=[[False]*(req+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][req]=True
        
        for i in range(n-1,-1,-1):
            for j in range(req-1,-1,-1):
                take=False
                if nums[i]+j<=req:
                    take=dp[i+1][nums[i]+j]

                skip=dp[i+1][j]
                dp[i][j]=take or skip
        
        return dp[0][0]