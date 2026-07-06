class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        print(intervals)
        n=len(intervals)
        
        max_end=0
        res=0
        for a,b in intervals:
            if b>max_end:
                max_end=b
                res+=1

        return res


                