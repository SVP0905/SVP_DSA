class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt=Counter(s)
        most_freq=max(cnt.values())

        n=len(s)
        if most_freq>(n+1)//2:
            return ''

        max_heap=[]
        for ch,val in cnt.items():
            heapq.heappush(max_heap,(-val,ch))

        res=[]
        while len(max_heap)>=2:
            val1,ch1=heapq.heappop(max_heap)
            val2,ch2=heapq.heappop(max_heap)

            res.append(ch1)
            res.append(ch2)

            if val1+1<0:
                heapq.heappush(max_heap,(val1+1,ch1))
            if val2+1<0:
                heapq.heappush(max_heap,(val2+1,ch2))

        if max_heap:
            val,ch=heapq.heappop(max_heap)
            res.append(ch)
        
        return ''.join(res)