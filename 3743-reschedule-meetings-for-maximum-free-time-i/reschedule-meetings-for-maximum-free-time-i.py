class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        events=list(zip(startTime,endTime))
        free_time_arr=[]

        prev_end=0
        for start,end in events:
            free_time_arr.append(start-prev_end)
            prev_end=end
        
        free_time_arr.append(eventTime-prev_end)

        if k>=len(free_time_arr):
            return eventTime

        if len(free_time_arr)<k+1:
            return sum(free_time_arr)
        
        window_sum=sum(free_time_arr[:k+1])
        max_sum=window_sum

        for i in range(k+1,len(free_time_arr)):
            window_sum=window_sum-free_time_arr[i-(k+1)]+free_time_arr[i]
            max_sum=max(max_sum,window_sum)
        
        return max_sum