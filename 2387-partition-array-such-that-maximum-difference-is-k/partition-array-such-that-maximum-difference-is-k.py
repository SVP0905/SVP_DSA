class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
            
        nums.sort()
        subsequence=1
        min_=nums[0]

        for i in range(1,len(nums)):
            if nums[i]-min_>k:
                subsequence+=1
                min_=nums[i]
        
        return subsequence