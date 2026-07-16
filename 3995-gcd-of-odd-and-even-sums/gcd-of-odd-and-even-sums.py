class Solution:
    def findGCD(self,a,b):
        if b==0:
            return a
        else:
            return self.findGCD(b,a%b)

    def gcdOfOddEvenSums(self, n: int) -> int:
        evenSum=0
        oddSum=0
        temp_n=n
        val=2
        while temp_n!=0:
            evenSum+=val
            val+=2
            temp_n-=1
        
        temp_n=n
        val=1
        while temp_n!=0:
            oddSum+=val
            val+=2
            temp_n-=1

        # print(evenSum)
        # print(oddSum)
        return self.findGCD(oddSum,evenSum)
            
            

        