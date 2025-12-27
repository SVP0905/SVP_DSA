class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        n=len(stones)
        dp=[[False]*(target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=True   # it possible to have target 0 with 0 stones

        
        for i in range(n-1,-1,-1):
            for j in range(1,target+1):
                 # we already filled for target 0
                skip=dp[i+1][j]

                take=False
                if j>=stones[i]:
                    take=dp[i+1][j-stones[i]] 
                    # if we take we need to have formed(j-stones) with the remaining stones
                
                dp[i][j]=skip or take
        


        for j in range(target,-1,-1):
            if dp[0][j]:
                return total-2*j
        
        
                

                



        

