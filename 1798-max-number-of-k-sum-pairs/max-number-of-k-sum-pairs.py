class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res=0
        n=len(nums)
        nums.sort()

        if n<2:
            return res
        
        l,r=0,n-1

        while l<r:
            current_sum=nums[l]+nums[r]
            if current_sum==k:
                res+=1
                l+=1
                r-=1
            elif current_sum<k:
                l+=1
            else:
                r-=1
        
        return res
        
        return res