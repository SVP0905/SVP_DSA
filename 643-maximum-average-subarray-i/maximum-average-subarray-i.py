class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        res=window_sum

        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            res=max(res,window_sum)
        
        return res/k