class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)

        if 2 * candidates >= n:
            costs.sort()
            return sum(costs[:k])
            
        l_heap,r_heap=[],[]

        for i in range(candidates):
            heapq.heappush(l_heap,(costs[i],i))
        
        for i in range(n-candidates,n):
            heapq.heappush(r_heap,(costs[i],i))
        
        l_ptr=candidates
        r_ptr=n-candidates-1
    
        total=0
        for _ in range(k):
            l_min=l_heap[0] if l_heap else (float('inf'),float('inf'))
            r_min=r_heap[0] if r_heap else (float('inf'),float('inf'))

            if l_min[0]<r_min[0] or (l_min[0]==r_min[0] and l_min[1]<r_min[1]):
                cost,i=heapq.heappop(l_heap)
                total+=cost

                if l_ptr<=r_ptr:
                    heapq.heappush(l_heap,(costs[l_ptr],l_ptr))
                    l_ptr+=1
            else:
                cost,i=heapq.heappop(r_heap)
                total+=cost

                if l_ptr<=r_ptr:
                    heapq.heappush(r_heap,(costs[r_ptr],r_ptr))
                    r_ptr-=1
        
        return total