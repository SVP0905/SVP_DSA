class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        cur_max,cur_min=nums[0],nums[0]

        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                cur_max,cur_min=cur_min,cur_max
            
            cur_max=max(nums[i],nums[i]*cur_max)
            cur_min=min(nums[i],nums[i]*cur_min)

            res=max(res,cur_max)
        
        return res