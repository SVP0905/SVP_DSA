class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_={}

        for i,num in enumerate(nums):
            diff=target-num
            if diff in map_:
                return (i,map_[diff])
            map_[num]=i
        


        

        