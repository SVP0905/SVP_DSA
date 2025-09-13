class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        stack=[]

        for i in range(n):
            if stack and arr[i]<stack[-1]:
                cur_stack_max=stack.pop()
                while stack and arr[i]<stack[-1]:
                    cur_stack_max=max(cur_stack_max,stack.pop())
                stack.append(cur_stack_max)
            else:
                stack.append(arr[i])
        
        return len(stack)