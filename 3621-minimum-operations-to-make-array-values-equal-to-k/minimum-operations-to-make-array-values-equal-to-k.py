class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set_=set()
        for num in nums:
            if num<k:
                return -1
            elif num>k:
                set_.add(num)
        
        return len(set_)