class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum,max_sum=0,float('-inf')

        for i,n in enumerate(nums):
            cur_sum+=n

            if cur_sum>max_sum:
                max_sum=cur_sum
                
            if cur_sum<0:
                cur_sum=0
            
        
        return max_sum