class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN,INT_MAX=-2**31,2**31-1
        reverse_=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            digit=x%10
            if reverse_>(INT_MAX-digit)//10:
                return 0
            reverse_=reverse_*10+digit
            x=x//10
        return sign*reverse_