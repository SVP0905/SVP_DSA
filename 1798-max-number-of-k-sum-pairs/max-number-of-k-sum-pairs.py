class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1

        cnt=0
        nums.sort()
        while l<r:
            cur_sum=nums[l]+nums[r]
            
            if cur_sum==k:
                l+=1
                r-=1
                cnt+=1
            elif cur_sum<k:
                l+=1
            else:
                r-=1
        return cnt