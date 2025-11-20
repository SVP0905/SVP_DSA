class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))

        points=[]

        for start,end in intervals:
            cnt=0
            for i in points[-2:]:
                if start<=i<=end:
                    cnt+=1
            
            if cnt==0:
                points.append(end-1)
                points.append(end)
            elif cnt==1:
                points.append(end)
        

        return len(points)
        
                
