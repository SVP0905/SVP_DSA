class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res=0
        max_=0
        length,width=0,0
        for a,b in dimensions:
            temp=math.sqrt(a**2+b**2)
            area=a*b
            if temp>res:
                res=temp
                length,width=a,b
            if temp==res and area>max_:
                max_=area
                length,width=a,b
                


        return length*width
            
        