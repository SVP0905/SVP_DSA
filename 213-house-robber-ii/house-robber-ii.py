class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        def linear_rob(arr):
            n_arr=len(arr)
            if n_arr==1:
                return arr[0]
            if n_arr==2:
                return max(arr[0],arr[1])
            
            dp=[0]*n_arr
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])

            for i in range(2,len(arr)):
                dp[i]=max(dp[i-1],dp[i-2]+arr[i])
            
            return max(dp)
        

        return max(linear_rob(nums[:-1]),linear_rob(nums[1:]))
