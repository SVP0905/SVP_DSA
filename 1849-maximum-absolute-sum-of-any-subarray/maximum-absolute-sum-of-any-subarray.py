class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        min_sum=0
        cur_max=0
        cur_min=0

        for n in nums:
            cur_max=max(cur_max+n,n)
            max_sum=max(cur_max,max_sum)

            cur_min=min(cur_min+n,n)
            min_sum=min(cur_min,min_sum)

        return max(max_sum,abs(min_sum))