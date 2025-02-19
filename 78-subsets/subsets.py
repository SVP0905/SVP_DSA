class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,list_):
            if i==len(nums):
                res.append(list_.copy())
                return
            list_.append(nums[i])
            dfs(i+1,list_)
            list_.remove(nums[i])
            dfs(i+1,list_)
        dfs(0,[])

        return res