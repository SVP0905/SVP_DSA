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
            i_=i+1
            while i_<len(nums) and nums[i_]==nums[i]:
                i_+=1
            dfs(i_,list_)
        dfs(0,[])

        return res


        