class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)

        if n<d:
            return -1

        @cache
        def dfs(i,days_left):
            if days_left==1:
                return max(jobDifficulty[i:])
            

            cur_day_max=0
            min_total=float('inf')

            for j in range(i,n-(days_left-1)):
                cur_day_max=max(cur_day_max,jobDifficulty[j])

                res=cur_day_max+dfs(j+1,days_left-1)

                min_total=min(min_total,res)
            
            return min_total
        
        return dfs(0,d)