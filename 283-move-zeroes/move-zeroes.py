class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=0

        while left<n and nums[left]!=0:
            left+=1
        
        right=left+1

        while right<n:
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1
        
        return nums