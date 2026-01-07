class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack=[]
        for n in arr:
            if not stack:
                stack.append(n)
            else:
                largest=max(n,stack[-1])
                while stack and n<stack[-1]:
                    stack.pop()
                stack.append(largest)
        
        return len(stack)
