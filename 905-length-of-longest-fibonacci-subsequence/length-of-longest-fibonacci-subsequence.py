class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        if n<3:
            return 0
            
        map_={arr[i]:i for i in range(n)}

        max_=0

        def dfs(i,j,cnt):
            nonlocal max_
            next_val=arr[i]+arr[j]

            if next_val in map_ and map_[next_val]>j:
                dfs(j,map_[next_val],cnt+1)
            
            if cnt>=3:
                max_=max(max_,cnt)

        for i in range(n-2):
            for j in range(i+1,n-1):
                dfs(i,j,2)
        
        return max_
             