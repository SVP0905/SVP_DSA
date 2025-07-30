class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cur_sum=0
        cur_str=''
        for ch in s:
            if ch.isdigit():
                cur_sum=cur_sum*10+int(ch)
            elif ch=='[':
                stack.append(cur_str)
                stack.append(cur_sum)
                cur_str=''
                cur_sum=0
            elif ch==']':
                num=stack.pop()
                prev_str=stack.pop()
                cur_str=prev_str+cur_str*num
            else:
                cur_str+=ch
        return cur_str
