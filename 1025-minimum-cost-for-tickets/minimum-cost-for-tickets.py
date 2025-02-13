class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days=set(days)
        dp={}
        def dfs(day):
            if day>days[-1]:
                return 0
            
            if day not in travel_days:
                return dfs(day+1)
            
            if day in dp:
                return dp[day]
            
            option1=costs[0]+dfs(day+1)
            option2=costs[1]+dfs(day+7)
            option3=costs[2]+dfs(day+30)

            dp[day]=min(option1,option2,option3)

            return dp[day]
        
        return dfs(days[0])