class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k=sum(nums)%p

        if k==0:
            return 0

        cur_sum=0
        map_={0:-1}
        length=0
        res=float('inf')
        for i,n in enumerate(nums):
            cur_sum+=n
            cur_rem=cur_sum%p
            req_rem=(cur_rem-k)%p

            if req_rem in map_:
                start_i=map_[req_rem]
                length=i-start_i
                if length<res:
                    res=length
            
            map_[cur_rem]=i
        
        return res if res<len(nums) else -1