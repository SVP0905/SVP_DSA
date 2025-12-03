class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_={0:1}
        cur_sum=0
        cnt=0
        for i,n in enumerate(nums):
            cur_sum+=n
            req_sum=cur_sum-k

            if req_sum in map_:
                cnt+=map_[req_sum]
            
            map_[cur_sum]=map_.get(cur_sum,0)+1
        
        return cnt
