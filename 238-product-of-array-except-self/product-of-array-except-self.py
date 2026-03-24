class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n  
        suffix=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        
        
        res=[1]*n
        for i in range(n):
            if i==0:
                res[i]=suffix[i]
            elif i==n-1:
                res[i]=prefix[i]
            else:
                res[i]=prefix[i]*suffix[i]
            
        return res
            
