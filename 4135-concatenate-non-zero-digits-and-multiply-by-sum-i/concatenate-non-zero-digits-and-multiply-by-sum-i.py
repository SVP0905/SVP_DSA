class Solution:
    def sumAndMultiply(self, n: int) -> int:

        #math way using place value
        # x=0
        # sum_=0
        # place=1

        # while n:
        #     digit=n%10
            
        #     if digit!=0:
        #         x=(digit*place)+x
        #         sum_+=digit
        #         place*=10
        #     n=n//10
        

        # print(sum_)
        # print(x)

        # return x*sum_

        #strings way (pythonic way)
        digits=[ch for ch in str(n) if ch!='0']

        print(digits)
        if not digits:
            return 0
        
        sum_=sum(int(d) for d in digits)
        x=int(''.join(digits))

        return x*sum_
        
        
        
