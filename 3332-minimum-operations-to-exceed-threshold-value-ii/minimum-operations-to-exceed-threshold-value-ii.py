class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if all(x>=k for x in nums):
            return 0
        
        heapq.heapify(nums)
        ops=0

        while len(nums)>=2 and nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)

            new_val=min(x,y)*2+max(x,y)

            heapq.heappush(nums,new_val)
            ops+=1

        if nums[0]<k:
            return -1
        
        return ops