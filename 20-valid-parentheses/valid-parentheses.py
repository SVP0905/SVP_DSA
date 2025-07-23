class Solution:
    def isValid(self, s: str) -> bool:
        brackets={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]
        for ch in s:
            if stack and ch in brackets and stack[-1]==brackets[ch]:
                stack.pop()
                continue
            stack.append(ch)
        return True if not stack else False