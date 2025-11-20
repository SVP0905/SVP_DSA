class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        prevEnd=intervals[0][1]
        for i in range(1,len(intervals)):
            cur_start,cur_end=intervals[i][0],intervals[i][1]
            if cur_start<=prevEnd:
                prevEnd=max(prevEnd,cur_end)
                res[-1][1]=prevEnd
            else:
                res.append([cur_start,cur_end])
                prevEnd=res[-1][1]
        
        return res
        
