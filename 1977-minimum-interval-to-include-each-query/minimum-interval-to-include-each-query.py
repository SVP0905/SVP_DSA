class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res=[-1]*len(queries)
        queries=[(q,i) for i,q in enumerate(queries)]
        queries.sort()
        minheap=[]
        i=0
        n=len(intervals)
        for q,q_i in queries:
            while i<n and intervals[i][0]<=q:
                s,e=intervals[i]
                heapq.heappush(minheap,(e-s+1,e))
                i+=1
            
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            
            if minheap:
                res[q_i]=minheap[0][0]
        
        return res

        
        return res
        
