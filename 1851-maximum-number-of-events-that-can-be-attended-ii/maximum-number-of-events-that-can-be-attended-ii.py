class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n=len(events)
        
        next_valid_evnts=[n]*n
        for i in range(n):
            target=events[i][1]+1
            l,r=i+1,n
            while l<r:
                mid=(l+r)//2
                if events[mid][0]>=target:
                    r=mid
                else:
                    l=mid+1
            next_valid_evnts[i]=l

        @lru_cache(maxsize=None)
        def dfs(i,evnts_cnt):
            if i>=n or evnts_cnt>=k:
                return 0
            
            not_choose=dfs(i+1,evnts_cnt)

            choose=0
            current_end=events[i][1]
            
            choose=events[i][2]+dfs(next_valid_evnts[i],evnts_cnt+1)

            return max(not_choose,choose)
        return dfs(0,0)