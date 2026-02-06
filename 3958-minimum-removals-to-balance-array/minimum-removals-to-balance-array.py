class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()

        ans=n
        i,j=0,0
        while i<n:

            while j<n and nums[j]<=nums[i]*k:
                j+=1
            ans=min(ans,n-(j-i))

            i+=1

        return ans

        