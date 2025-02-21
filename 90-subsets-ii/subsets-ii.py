class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def dfs(i,list_):
            if i>=len(nums):
                res.append(list_.copy())
                return
            
            list_.append(nums[i])
            dfs(i+1,list_)
            list_.remove(nums[i])

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1

            dfs(i+1,list_)
        
        dfs(0,[])

        return res