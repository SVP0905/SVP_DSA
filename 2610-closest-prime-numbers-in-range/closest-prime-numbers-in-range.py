class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num<2:
                return False

            if num==2 or num==3:
                return True

            if num%2==0 or num%3==0:
                return False
            
            i=5
            while i*i<=num:
                if num%i==0 or num%(i+2)==0:
                    return False
                i+=6
            return True
        
        primes=[]
        for i in range(left,right+1):
            if isPrime(i):
                primes.append(i)
        
        if len(primes)<2:
            return [-1,-1]
        
        min_diff=float('inf')
        ans=[-1,-1]
        
        for i in range(1,len(primes)):
            diff=primes[i]-primes[i-1]
            if diff<min_diff:
                min_diff=diff
                ans=[primes[i-1],primes[i]]
        
        return ans