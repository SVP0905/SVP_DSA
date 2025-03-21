class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt=0
        cur_cnt=0

        for i in range(len(nums)):
            if nums[i]==1:
                cur_cnt+=1
            else:
                max_cnt=max(max_cnt,cur_cnt)
                cur_cnt=0
        
        max_cnt=max(max_cnt,cur_cnt)

        return max_cnt
