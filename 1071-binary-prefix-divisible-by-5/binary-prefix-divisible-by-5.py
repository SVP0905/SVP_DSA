class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur_val=0
        sum_=0
        res=[False]*len(nums)
        for i,n in enumerate(nums):
            sum_=2*sum_+n
            cur_val=(sum_)%5
            if cur_val==0:
                res[i]=True
        
        return res
