class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_={}
        # for i,val in enumerate(nums):
        #     map_[val]=i
        
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
        
        
        