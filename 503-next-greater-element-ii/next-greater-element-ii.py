class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*len(nums)
        nums.extend(nums)

        for i in range(n):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    res[i]=nums[j]
                    break
        
        return res