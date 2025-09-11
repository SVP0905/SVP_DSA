class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
        
