class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        l,r=0,0
        n=len(fruits)
        res=0
        while r<n:
            basket[fruits[r]]=1+basket.get(fruits[r],0)

            while len(basket)>2:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                    del basket[fruits[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res