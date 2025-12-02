class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target_sum=sum(nums)-x
        cur_sum=0
        l,r=0,0
        res=float('-inf')
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while cur_sum>target_sum and l<=r:
                cur_sum-=nums[l]
                l+=1
            
            if cur_sum==target_sum:
                res=max(res,r-l+1)
        
        if res==float('-inf'):
            return -1
        else:
            return len(nums)-res