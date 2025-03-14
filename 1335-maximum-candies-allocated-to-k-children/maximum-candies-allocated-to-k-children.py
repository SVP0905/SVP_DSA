class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0

        n=len(candies)
        l,r=1,max(max(candies),sum(candies)//k)

        while l<=r:
            mid=(l+r)//2
            count=0

            for i in range(n):
                count+=candies[i]//mid
            
            if count>=k:
                l=mid+1
            else:
                r=mid-1
        return r