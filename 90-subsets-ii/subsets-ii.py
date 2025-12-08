class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        power_set=[]
        def dfs(arr,i):
            if i>=len(nums):
                power_set.append(arr.copy())
                return
            arr.append(nums[i])
            dfs(arr,i+1)
            arr.pop()
            j=i
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            dfs(arr,i+1)
        
        dfs([],0)
        return power_set