class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        sum_=0
        place=1

        while n:
            digit=n%10
            
            if digit!=0:
                x=(digit*place)+x
                sum_+=digit
                place*=10
            n=n//10
        

        print(sum_)
        print(x)

        return x*sum_
        
        
        
