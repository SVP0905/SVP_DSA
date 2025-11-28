class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        map_={0:-1}
        cur_sum=0
        for i,n in enumerate(nums):
            cur_sum+=n
            rem=cur_sum%k
            if rem in map_:
                if i-map_[rem]>=2:
                    return True
            else:
                map_[rem]=i

        
        return False