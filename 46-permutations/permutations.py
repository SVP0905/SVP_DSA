class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(idx):
            if idx==len(nums):
                res.append(nums.copy())
                return
            for i in range(idx,len(nums)):
                nums[i],nums[idx]=nums[idx],nums[i]
                permute(idx+1)
                nums[i],nums[idx]=nums[idx],nums[i]
        
        res=[]
        permute(0)
        return res
