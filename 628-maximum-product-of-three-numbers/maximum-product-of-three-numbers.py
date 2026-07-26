class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        res1=1
        for i in range(3):
            res1*=nums[i]
        

        res2=1
        for i in range(-1,-3,-1):
            res2*=nums[i]
        
        res2*=nums[0]

        return max(res1,res2)
    