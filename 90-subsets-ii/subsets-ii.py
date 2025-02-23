class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i,sub_):
            if i>=len(nums):
                res.append(sub_.copy())
                return
            sub_.append(nums[i])
            dfs(i+1,sub_)
            sub_.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            dfs(i+1,sub_)
        res=[]
        dfs(0,[])
        return res