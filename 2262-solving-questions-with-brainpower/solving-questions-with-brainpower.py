class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo={}
        def dfs(i):
            if i>=len(questions):
                return 0
            if i in memo:
                return memo[i]
            
            points,brainstorm=questions[i]
            memo[i]=max(dfs(i+1),points+dfs(i+brainstorm+1))
            return memo[i]
        
        return dfs(0)