class Solution:
    def find_digits_prod(self,num):
        temp=num
        prod=1
        while temp:
            digit=temp%10
            prod*=digit
            temp//=10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        for i in itertools.count(start=n,step=1):
            prod=self.find_digits_prod(i)
            if prod%t==0:
                return i
        
            