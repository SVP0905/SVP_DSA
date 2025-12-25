class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n=len(happiness)
        happiness.sort(reverse=True)
        res=0
        # for i in range(k):
        #     res+=happiness[i]
        #     print(happiness)
        #     for j in range(i+1,n):
        #         happiness[i]-=1 if happiness[i]-1>=0 else 0
        #     print(happiness)
        
        # return res

        for i in range(k):
            if i==0:
                res+=happiness[i]
            else:
                res+=happiness[i]-i if happiness[i]-i>=0 else 0
        
        return res