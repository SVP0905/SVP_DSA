class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD=10**9+7
        bin_n=bin(n)[2:]
        expo=[]
        for i,bit in enumerate(reversed(bin_n)):
            if bit=='1':
                expo.append(i)
        
        prefix=[0]*len(expo)
        prefix[0]=expo[0] 
        for i in range(1,len(expo)):
            prefix[i]=prefix[i-1]+expo[i] 
        
        
        ans=[]
        for l,r in queries:
            if l==0:
                sum_=prefix[r]
            else:
                sum_=prefix[r]-prefix[l-1]
            ans.append(pow(2,sum_,MOD))
        
        return ans