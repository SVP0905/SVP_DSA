class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)+1
        prev1,prev2=0,0

        for i in range(2,n):
            prev1,prev2=prev2,min(cost[i-2]+prev1,cost[i-1]+prev2)
        
        return prev2