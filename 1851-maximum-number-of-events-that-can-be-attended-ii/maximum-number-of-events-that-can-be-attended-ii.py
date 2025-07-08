class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n=len(events)

        next_valid_events=[n]*n

        for i in range(n):
            target=events[i][1]+1
            l,r=i+1,n
            while l<r:
                mid=(l+r)//2
                if events[mid][0]>=target:
                    r=mid
                else:
                    l=mid+1
            next_valid_events[i]=l
        

        @lru_cache(maxsize=None)
        def dfs(i,events_attended):
            if i>=n or events_attended>=k:
                return 0
            
            not_choose=dfs(i+1,events_attended)
            
            choose=events[i][2]+dfs(next_valid_events[i],events_attended+1)

            return max(choose,not_choose)
        return dfs(0,0)
