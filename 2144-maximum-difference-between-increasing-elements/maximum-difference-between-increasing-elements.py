class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_,premin=float('-inf'),nums[0]

        for i in range(1,len(nums)):
            if nums[i]>premin:
                max_=max(max_,nums[i]-premin)
            else:
                premin=nums[i]
        
        if max_==float('-inf'):
            return -1
        else:
            return max_