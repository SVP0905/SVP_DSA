class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(stack,map_):
            if len(stack)==len(nums):
                res.append(stack.copy())
                return
            else:
                for i in range(len(nums)):
                    if map_[i]==1:
                        continue
                    else:
                        map_[i]=1
                        stack.append(nums[i])
                        dfs(stack,map_)
                        stack.pop()
                        map_[i]=0
        
        res=[]
        map_=[0]*len(nums)
        stack=[]
        dfs(stack,map_)
        return res