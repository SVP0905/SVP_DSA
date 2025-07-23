class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        res=[-1]*len(nums)
        for i in range(2*n-1,-1,-1):
            cur_idx=i%n
            cur_val=nums[cur_idx]

            while stack and stack[-1]<=cur_val:
                stack.pop()

            if i<n and stack:
                res[cur_idx]=stack[-1]
            stack.append(cur_val)
        
        return res

            
        
