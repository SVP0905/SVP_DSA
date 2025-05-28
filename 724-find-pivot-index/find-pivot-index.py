class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix=[0]*len(nums)
        right_prefix=[0]*len(nums)

        for i in range(1,len(nums)):
            left_prefix[i]=left_prefix[i-1]+nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right_prefix[i]=right_prefix[i+1]+nums[i+1]
        
        
        for i in range(len(nums)):
            if i==0 and left_prefix[i]==right_prefix[i]:
                return i
            if i==len(nums)-1 and left_prefix[i]==right_prefix[i]:
                return i
            if left_prefix[i]==right_prefix[i]:
                return i
            
        return -1
