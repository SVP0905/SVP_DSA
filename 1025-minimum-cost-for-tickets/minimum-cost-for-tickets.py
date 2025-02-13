class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]*(days[-1]+1)
        travel_days=set(days)

        for i in range(1,len(dp)):
            if i not in travel_days:
                dp[i]=dp[i-1]
            else:
                one_day=dp[i-1]+costs[0]
                seven_day=dp[max(0,i-7)]+costs[1]
                thirty_day=dp[max(0,i-30)]+costs[2]

                dp[i]=min(one_day,seven_day,thirty_day)

        return dp[days[-1]]