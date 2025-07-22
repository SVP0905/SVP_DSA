class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=0
        l=0
        seen=set()
        n=len(nums)
        cur_sum=0

        for r in range(n):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur_sum-=nums[l]
                l+=1
            
            seen.add(nums[r])
            cur_sum+=nums[r]
            res=max(res,cur_sum)
        
        return res