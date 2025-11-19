class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        map_={}
        for i in range(len(nums)):
            map_[nums[i]]=i
        
        
        while original in map_:
            original*=2
            
        return original
        