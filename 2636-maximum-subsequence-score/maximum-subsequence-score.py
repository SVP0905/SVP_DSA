class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr=list(zip(nums1,nums2))
        arr.sort(key=lambda x:x[1],reverse=True)

        min_heap=[]
        cur_sum,max_=0,0
        for n1,n2 in arr:
            heapq.heappush(min_heap,n1)
            cur_sum+=n1

            if len(min_heap)>k:
                cur_sum-=heapq.heappop(min_heap)
            if len(min_heap)==k:
                max_=max(max_,cur_sum*n2)

        return max_