class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m,n=min(nums),max(nums)
        unique_set=set(nums)
        res=[]
        for n in range(m,n+1):
            if n not in unique_set:
                res.append(n)
        
        return res