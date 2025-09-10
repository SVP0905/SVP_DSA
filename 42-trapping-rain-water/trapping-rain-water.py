class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        stack=[]
        water=0
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                valley_idx=stack.pop()
                if not stack:
                    break
                
                left_boundary=stack[-1]
                right_boundary=i
                water_level=min(height[left_boundary],height[right_boundary])-height[valley_idx]
                width=right_boundary-left_boundary-1

                water+=water_level*width
            
            stack.append(i)
        
        return water
        
        return water

            
