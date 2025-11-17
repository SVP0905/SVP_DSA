class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx=-1
        for i in range(len(nums)):
            if nums[i]==1:
                if last_idx!=-1 and i-last_idx-1<k:
                    return False
                last_idx=i
        
        return True