class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup=x
        reverse_=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            digit=x%10
            reverse_=reverse_*10+digit
            x=x//10
        
        if dup==reverse_:
            return True
        else:
            return False