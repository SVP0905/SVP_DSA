class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        n=len(s)
        map_={ch:i for i,ch in enumerate(s)}
        seen=set()
        for i,ch in enumerate(s):
            if ch in seen:
                continue

            while stack and ch<stack[-1] and map_[stack[-1]]>i:
                popped=stack.pop()
                seen.remove(popped)
            
            stack.append(ch)
            seen.add(ch)
        
        return ''.join(stack)