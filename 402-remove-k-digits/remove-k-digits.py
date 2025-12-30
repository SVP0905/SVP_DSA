class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        n=len(num)
        req_len=n-k
        for i,ch in enumerate(num):
            while stack and ch<stack[-1] and len(stack)-1+(n-i)>=req_len:
                stack.pop()
            
            if len(stack)<req_len:
                stack.append(ch)
        
        str_=''.join(stack)
        cleaned_str=str_.lstrip('0')

        return cleaned_str if cleaned_str!='' else '0'