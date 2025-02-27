class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)

        if n<3:
            return 0
        
        max_=0
        map_={arr[i]:i for i in range(n)}

        def dfs(i,j,len_):
            nonlocal max_
            next_val=arr[i]+arr[j]

            if next_val in map_ and map_[next_val]>j:
                dfs(j,map_[next_val],len_+1)
            
            if len_>=3:
                max_=max(max_,len_)

        for i in range(n-2):
            for j in range(i+1,n-1):
                dfs(i,j,2)
        
        return max_