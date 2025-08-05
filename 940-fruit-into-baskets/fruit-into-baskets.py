class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        n=len(fruits)
        map_={}
        res=0
        while r<n:
            map_[fruits[r]]=1+map_.get(fruits[r],0)
            
            while len(map_)>2:
                map_[fruits[l]]-=1
                if map_[fruits[l]]==0:
                    del map_[fruits[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
            