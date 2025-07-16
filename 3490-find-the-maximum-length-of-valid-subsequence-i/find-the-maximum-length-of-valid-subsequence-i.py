class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even=[]
        odd=[]
        alt=[]
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                even.append(nums[i])
            elif nums[i]%2==1:
                odd.append(nums[i])
        print(even)
        print(odd)
        prev_parity=nums[0]%2
        alt.append(nums[0])
        for i in range(1,n):
            if nums[i]%2!=prev_parity:
                alt.append(nums[i])
                prev_parity=nums[i]%2
        print(alt)

        
        return max(len(even),len(odd),len(alt))