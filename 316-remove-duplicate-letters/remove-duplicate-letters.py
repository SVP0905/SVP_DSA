class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter=Counter(s)
        n=len(s)
        stack=[]
        for ch in s:
            counter[ch]-=1
            if ch in stack:
                continue
            while stack and ch<stack[-1] and counter[stack[-1]]>0:
                stack.pop()
            
            stack.append(ch)
        
        return ''.join(stack)