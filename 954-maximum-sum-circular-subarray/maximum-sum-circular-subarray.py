class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        cur_max,cur_min=nums[0],nums[0]
        min_sum,max_sum=nums[0],nums[0]
        total_sum=nums[0]
        for i in range(1,n):
            #std Kadane(max subarray)
            cur_max=max(nums[i],nums[i]+cur_max)
            max_sum=max(max_sum,cur_max)

            #inverted kadane(min subarray)
            cur_min=min(nums[i],nums[i]+cur_min)
            min_sum=min(min_sum,cur_min)

            total_sum+=nums[i]
        
        # EDGE CASE: If all numbers are negative (e.g., [-3, -2, -3])
        # max_sum will be -2.
        # min_sum will be -8 (total sum).
        # (Total - Min) would be 0 (an empty subarray), which isn't allowed.
        if max_sum<0:
            return max_sum
        
        return max(max_sum,total_sum-min_sum)


            

            