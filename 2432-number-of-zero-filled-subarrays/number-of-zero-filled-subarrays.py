class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        l=0
        while l<n:
            if nums[l]==0:
                r=l
                while r<n and nums[r]==0:
                    r+=1
                k=r-l
                cnt+=k*(k+1)//2
                l=r
            else:
                l+=1
        
        return cnt