class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r=0,0
        zeros=0
        max_=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
            if zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            max_=max(max_,r-l+1)
            r+=1
        return max_-1