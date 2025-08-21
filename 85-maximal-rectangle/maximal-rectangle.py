class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        heights=[0]*n
        max_=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
        
            max_=max(max_,self.longestRecInHisto(heights))

        return max_
    
    def longestRecInHisto(self,heights):
        heights=heights+[0]
        stack=[-1]
        max_=0

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                r=i
                l=stack[-1]
                area=h*(r-l-1)
                max_=max(max_,area)
            stack.append(i)
        
        stack.pop()
        return max_