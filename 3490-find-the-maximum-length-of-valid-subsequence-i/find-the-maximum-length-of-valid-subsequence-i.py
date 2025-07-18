class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even,odd,alt=[],[],[]
        for num in nums:
            if num%2==0:
                even.append(num)
            elif num%2==1:
                odd.append(num)
        
        prev_parity=nums[0]%2
        alt.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]%2!=prev_parity:
                alt.append(nums[i])
                prev_parity=nums[i]%2
        
        return max(len(even),len(odd),len(alt))