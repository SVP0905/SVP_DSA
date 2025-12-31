class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dfs(i):
            if i>=len(arr):
                return 0
            
            max_sum=0
            for j in range(1,k+1):
                if i+j>len(arr):
                    break
                total=max(arr[i:i+j])*j+dfs(i+j)
                max_sum=max(max_sum,total)
            
            return max_sum
        
        return dfs(0)