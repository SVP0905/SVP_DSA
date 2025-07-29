class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            res[i]=res[i-1]*nums[i-1]
        
        suffix_pro=1
        for i in range(n-1,-1,-1):
            res[i]*=suffix_pro
            suffix_pro=suffix_pro*nums[i]
        
        return res