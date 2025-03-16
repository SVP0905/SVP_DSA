class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def dfs(cap):
            dp=[0]*(len(nums)+2)
            for i in range(len(nums)):
                if nums[i]<=cap:
                    dp[i+2]=max(dp[i+1],dp[i]+1)
                else:
                    dp[i+2]=dp[i+1]
            return dp[-1]>=k
        
        left,right=min(nums),max(nums)
        while left<right:
            mid=(left+right)//2
            
            if dfs(mid):
                right=mid
            else:
                left=mid+1
        
        return left
                