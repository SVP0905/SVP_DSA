class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        
        map_arr=[float('inf')]*k
        map_arr[k-1]=0
        
        res=float('-inf')
        for i,n in enumerate(nums):
            rem=i%k

            if map_arr[rem]!=float('inf'):
                previous_sum=map_arr[rem]
                cur_sum=prefix_sum[i]-previous_sum
                res=max(res,cur_sum)
            
            if prefix_sum[i]<map_arr[rem]:
                map_arr[rem]=prefix_sum[i]
        
        return res