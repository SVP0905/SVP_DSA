class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        map_={0:1}
        cnt=0
        cur_sum=0
        for i,n in enumerate(nums):
            cur_sum+=n
            rem=cur_sum%k

            if rem in map_:
                cnt+=map_[rem]
                map_[rem]+=1
            else:
                map_[rem]=1
        
        return cnt

        