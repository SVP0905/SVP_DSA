class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_={}
        def dfs(i,map_):
            if i>=len(nums):
                return None
            
            diff=target-nums[i]
            if diff in map_:
                return (i,map_[diff])
            map_[nums[i]]=i
            return dfs(i+1,map_)
        return dfs(0,map_)