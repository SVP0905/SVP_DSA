class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_={}
        for i,n in enumerate(nums):
            map_[n]=i
        

        
        for i,val in enumerate(nums):
            diff=target-val
            if diff in map_ and map_[diff]!=i:
                return sorted([i,map_[diff]])
        return []

        
        
        
        
        
        