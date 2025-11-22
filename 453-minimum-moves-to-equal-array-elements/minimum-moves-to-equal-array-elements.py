class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_=min(nums)
        res=0
        for num in nums:
            res+=num-min_
        
        return res