class Solution:
    def __init__(self):
        self.mod = 10**9 + 7
        
    def preComputeFactorials(self,MX):
        fact=[1]*(MX+1)
        for i in range(1,MX+1):
            fact[i]=(fact[i-1]*i)%self.mod
        return fact
    
    def mod_inverse(self,base,mod):
        return pow(base,mod-2,mod)

    def combination(self,n,r,fact):
        if r > n or r < 0:
            return 0

        numerator=fact[n]
        denominator=(fact[n-r]*fact[r])%self.mod
        return (numerator*self.mod_inverse(denominator,self.mod))%self.mod
    
    def mod_power(self,base, exp, mod):
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp >> 1
            base = (base * base) % mod
        return result

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        fact = self.preComputeFactorials(n)
        ways_to_partition = self.combination(n - 1, k, fact)
        first_segment_choices = m % self.mod
        remaining_segments = n - k - 1


        if remaining_segments == 0:
            remaining_choices = 1
        else:
            remaining_choices = self.mod_power(m - 1, remaining_segments, self.mod)
            
        result = (ways_to_partition * first_segment_choices) % self.mod
        result = (result * remaining_choices) % self.mod
            
        return result