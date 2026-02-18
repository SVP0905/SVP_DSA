class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n=list(bin(n)[2:])
        
        # print(bin_n)
        
        for i in range(1,len(bin_n)):
            if bin_n[i]==bin_n[i-1]:
                return False
        
        return True