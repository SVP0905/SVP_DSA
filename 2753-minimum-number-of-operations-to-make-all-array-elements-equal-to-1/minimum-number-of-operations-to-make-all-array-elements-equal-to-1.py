class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ones=nums.count(1)

        if ones>0:
            return n-ones

        overall_gcd=reduce(math.gcd,nums)

        if overall_gcd!=1:
            return -1
    
        min_len=float('inf')
        if overall_gcd!=1:
            return -1
        else:
            for l in range(n):
                cur_gcd=nums[l]
                for r in range(l,n):
                    cur_gcd=math.gcd(cur_gcd,nums[r])
                    if cur_gcd==1:
                        min_len=min(min_len,r-l+1)
                        break
        
        

        return min_len+n-2


