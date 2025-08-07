class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m,n=amount,len(coins)

        dp=[[0]*(n+1) for _ in range(amount+1)]

        for i in range(n+1):
            dp[amount][i]=1
        

        for i in range(amount-1,-1,-1):
            for j in range(n-1,-1,-1):
                take,skip=0,0
                if i+coins[j]<=amount:
                    take=dp[i+coins[j]][j]
                
                skip=dp[i][j+1]
                dp[i][j]=take+skip
        
        return dp[0][0]