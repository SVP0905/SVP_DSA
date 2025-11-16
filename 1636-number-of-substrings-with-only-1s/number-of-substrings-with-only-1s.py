class Solution:
    def numSub(self, s: str) -> int:
        MOD=10**9+7
        n=len(s)
        res=0
        k=0
        for i in range(n):
            if s[i]=='1':
                k+=1
            else:
                res+=(k*(k+1)//2)%MOD
                k=0
        
        res+=(k*(k+1)//2)%MOD
        
        return res