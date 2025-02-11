class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2

        dp=[[False]*(target+1) for _ in range(len(stones)+1)]
        dp[0][0]=True

        for i in range(1,len(stones)+1):
            for j in range(target+1):
                if j<stones[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-stones[i-1]]
        
        for j in range(target,-1,-1):
            if dp[len(stones)][j]:
                return total-2*j
            
        return total