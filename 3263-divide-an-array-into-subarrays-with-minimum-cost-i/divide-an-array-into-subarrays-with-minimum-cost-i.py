class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res=0
        res+=nums[0]
        
        sorted_nums=sorted(nums[1:])
        res+=(sorted_nums[0]+sorted_nums[1])

        return res