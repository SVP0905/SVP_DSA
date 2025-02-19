class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res=[]
        stack=[]
        n=len(pattern)

        for i in range(n+1):
            stack.append(i+1)

            if i==n or pattern[i]=='I':
                while stack:
                    res.append(str(stack.pop()))
        
        return ''.join(res)