class Solution:
    def maxSum(self, nums: List[int]) -> int:
        p_nums=set([n for n in nums if n>0])
        return max(nums) if len(p_nums)==0 else sum(p_nums)