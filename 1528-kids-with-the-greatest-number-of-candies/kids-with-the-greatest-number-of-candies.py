class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val=max(candies)
        res=[False]*len(candies)
        for i in range(len(candies)):
            candy=candies[i]+extraCandies
            if candy>=max_val:
                res[i]=True
        
        return res
        