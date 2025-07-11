class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[-x for x in nums]
        heapq.heapify(arr)
        res=0
        for i in range(k):
            res=heapq.heappop(arr)
        
        return -res