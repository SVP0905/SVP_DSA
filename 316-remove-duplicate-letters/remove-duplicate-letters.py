class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        map_={ch:i for i,ch in enumerate(s)}

        for i,ch in enumerate(s):
            if ch in seen:
                continue
            
            while stack and ch<stack[-1] and map_[stack[-1]]>i:
                seen.remove(stack.pop())
            
            stack.append(ch)
            seen.add(ch)
        
        return ''.join(stack)