class Solution:
    def find_max(self,heights):
        n=len(heights)
        stack=[]
        max_=0

        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                cur_idx=stack.pop()
                nse=i
                pse=stack[-1] if stack else -1
                height=heights[cur_idx]
                width=nse-pse-1
                max_=max(max_,height*width)
            stack.append(i)
        
        while stack:
            cur_idx=stack.pop()
            nse=n
            pse=stack[-1] if stack else -1
            height=heights[cur_idx]
            width=nse-pse-1
            max_=max(max_,height*width)
        
        return max_

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])

        max_=0
        heights=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0

                
            max_=max(max_,self.find_max(heights))
        
        return max_
        