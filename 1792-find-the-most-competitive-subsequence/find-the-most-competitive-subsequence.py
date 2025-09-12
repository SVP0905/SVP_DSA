class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        n=len(nums)

        for i in range(n):
            # Only pop if:
            # 1. Current element is smaller than stack top
            # 2. We have enough remaining elements to reach size k
            while (stack and nums[i]<stack[-1] and len(stack)+n-i>k):
                stack.pop()
            
            if len(stack)<k:
                stack.append(nums[i])

        return stack