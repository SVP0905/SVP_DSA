class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        j=1
        while j<n:
            num1=nums[j-1]
            num2=nums[j]
            if num1==num2:
                nums[j-1]=nums[j-1]*2
                nums[j]=0

            j+=1
            
        temp=[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i]=temp[i]
        
        for i in range(len(temp),n):
            nums[i]=0
        
        return nums



        