class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = amount + 1
        dp = [0] * n
        dp[0] = 1

        for coin in coins:

            for x in range(1, n):
                
                if(coin <= x):
                    dp[x] += dp[x-coin]
        
        return dp[-1]