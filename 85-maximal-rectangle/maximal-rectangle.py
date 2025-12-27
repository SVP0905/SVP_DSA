class Solution:
    def largest_rect(self,heights):
        n=len(heights)
        max_=0
        stack=[]
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                cur_idx=stack.pop()
                left=stack[-1] if stack else -1
                right=i
                width=right-left-1
                height=heights[cur_idx]
                max_=max(max_,width*height)
            
            stack.append(i)
        
        while stack:
            cur_idx=stack.pop()
            left=stack[-1] if stack else -1
            right=n
            width=right-left-1
            height=heights[cur_idx]
            max_=max(max_,width*height)

        
        return max_

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        heights=[0]*n
        res=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    heights[j]=0
                else:
                    heights[j]+=1
            res=max(res,self.largest_rect(heights))
        
        return res
