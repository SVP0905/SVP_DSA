class Solution:
    def maxProduct(self, n: int) -> int:
        res=1
        digits=[]
        while n!=0:
            digits.append(n%10)
            n//=10
        
        digits.sort(reverse=True)
        

        for i in range(2):
            res*=digits[i]
        
        return res