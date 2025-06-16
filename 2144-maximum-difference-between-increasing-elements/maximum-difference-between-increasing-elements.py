class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        max_=float('-inf')
        for i in range(0,n-1):
            for j in range(i,n):
                if nums[j]>nums[i]:
                    max_=max(max_,nums[j]-nums[i])
        
        if max_==float('-inf'):
            return -1
        else:
            return max_