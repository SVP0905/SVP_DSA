class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_=defaultdict(int)
        n=len(nums)
        for i in range(n):
            map_[nums[i]]=i
        
        for i in range(n):
            diff=target-nums[i]
            if diff in map_ and i!=map_[diff]:
                return [i,map_[diff]]
        return []
