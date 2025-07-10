class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events=sorted(list(zip(startTime,endTime)))

        free_time_arr=[]
        prev_end=0
        for start,end in events:
            free_time_arr.append(start-prev_end)
            prev_end=end
        
        free_time_arr.append(eventTime-prev_end)

        n=len(events)
        maxRight=[0]*(n+1)
        for i in range(n-1,-1,-1):
            maxRight[i]=max(maxRight[i+1],free_time_arr[i+1])
        
        maxLeft=[0]*(n+1)
        for i in range(1,n+1):
            maxLeft[i]=max(maxLeft[i-1],free_time_arr[i-1])
        

        max_=max(free_time_arr)
        for i in range(n):
            d=events[i][1]-events[i][0]
            f1,f2=free_time_arr[i],free_time_arr[i+1]
            merged_gap=f1+d+f2

            max_alt_gap=max(maxLeft[i],maxRight[i+1])

            if max_alt_gap<d:
                max_=max(max_,merged_gap-d)
            else:
                max_=max(max_,merged_gap)
        return max_