class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr=[]

        while n:
            digit=n%10
            
            if digit!=0:
                arr.append(digit)

            n=n//10
        
        sum_=sum(arr)
        print(sum_)
        print(arr)
        arr.reverse()

        x=0
        for a in arr:
            x=x*10+a
        
        res=x*sum_
        
        return res
        
