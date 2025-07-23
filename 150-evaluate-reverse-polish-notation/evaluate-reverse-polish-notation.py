class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch in ['+','-','*','/']:
                b=stack.pop()
                a=stack.pop()
                if ch=='+':
                    res=a+b
                elif ch=='-':
                    res=a-b
                elif ch=='*':
                    res=a*b
                elif ch=='/':
                    res=int(a/b)
                
                stack.append(res)
            else:
                stack.append(int(ch))
        
        return stack[-1]