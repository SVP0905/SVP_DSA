class Solution:
    def numSquares(self, n: int) -> int:
        perfect_sqrs=[]

        for i in range(1,int(math.sqrt(n))+1):
            perfect_sqrs.append(i*i)
        

        @cache
        def dfs(cur_sum):
            if cur_sum==n:
                return 0
            if cur_sum>n:
                return float('inf')
            
            min_path=float('inf')

            for sq in perfect_sqrs:
                res=dfs(cur_sum+sq)

                if res!=float('inf'):
                    min_path=min(min_path,res+1)
            
            return min_path
        

        return dfs(0)