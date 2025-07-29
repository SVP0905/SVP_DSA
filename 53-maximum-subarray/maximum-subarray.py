class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_=nums[0]
        cur_sum=0
        for n in nums:
            cur_sum=max(cur_sum+n,n)
            max_=max(max_,cur_sum)

        return max_