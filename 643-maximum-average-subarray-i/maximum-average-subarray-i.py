class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sum_=sum(nums[:k])
        res=sum_/k

        for i in range(k,n):
            sum_-=nums[i-k]
            sum_+=nums[i]
            res=max(res,sum_/k)
        
        return res
            
