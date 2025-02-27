class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        if n<3:
            return 0
        map_={arr[i]:i for i in range(n)}
        memo={}
        def fib(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            next_val=arr[i]+arr[j]

            if next_val not in map_ or map_[next_val]<=j:
                return 0
            
            memo[(i,j)]=1+fib(j,map_[next_val])
            
            return memo[(i,j)]
        
        max_=0
        for i in range(n):
            for j in range(i+1,n):
                len_=fib(i,j)

                if len_>0:
                    max_=max(max_,len_+2)
        return max_