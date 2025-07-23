class Solution:
    def find_sum_ab(self,s,x,y):
        sum_=0
        stack=[]
        for ch in s:
            if stack and stack[-1]=='a' and ch=='b':
                stack.pop()
                sum_+=x
                continue
            stack.append(ch)
        return ''.join(stack),sum_
    
    def find_sum_ba(self,s,x,y):
        sum_=0
        stack=[]
        for ch in s:
            if stack and stack[-1]=='b' and ch=='a':
                stack.pop()
                sum_+=y
                continue
            stack.append(ch)
        return ''.join(stack),sum_

    def maximumGain(self, s: str, x: int, y: int) -> int:
        sum1,sum2=0,0
        res=0
        if x>y:
            str_,sum1=self.find_sum_ab(s,x,y)
            _,sum2=self.find_sum_ba(str_,x,y)
        else:
            str_,sum1=self.find_sum_ba(s,x,y)
            _,sum2=self.find_sum_ab(str_,x,y)
        
        return max(sum1,sum2,sum1+sum2)
        
        
