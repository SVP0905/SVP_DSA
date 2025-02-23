class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i,sub_):
            if i>=len(nums):
                res.append(sub_.copy())
                return
            sub_.append(nums[i])
            dfs(i+1,sub_)
            sub_.pop()
            dfs(i+1,sub_)

        res=[]
        dfs(0,[])

        return res