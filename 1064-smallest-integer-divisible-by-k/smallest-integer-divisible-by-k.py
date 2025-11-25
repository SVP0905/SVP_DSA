class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        
        rem=0
        for i in range(1,k+1):
            rem=(10*rem+1)
            if rem%k==0:
                return i
        
        return -1


