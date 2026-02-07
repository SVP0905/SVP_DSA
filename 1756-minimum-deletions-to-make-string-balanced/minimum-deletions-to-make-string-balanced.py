class Solution:
    def minimumDeletions(self, s: str) -> int:
        n=len(s)
        stack=[]
        deletions=0
        for ch in s:
            if stack and stack[-1]>ch:
                deletions+=1
                stack.pop()
            else:
                stack.append(ch)
        
        return deletions