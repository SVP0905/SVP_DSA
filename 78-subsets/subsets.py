class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set=[]
        def dfs(arr,i):
            if i>=len(nums):
                power_set.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(arr,i+1)
            arr.pop()
            dfs(arr,i+1)
        
        dfs([],0)
        return power_set
        
