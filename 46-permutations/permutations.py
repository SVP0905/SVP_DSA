class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(stack_,map_):
            if len(stack_)==len(nums):
                res.append(stack_.copy())
                return
            
            for i in range(len(nums)):
                if map_[i]==1:
                    continue
                map_[i]=1
                stack_.append(nums[i])
                dfs(stack_,map_)
                stack_.pop()
                map_[i]=0
        
        res=[]
        map_=[0]*len(nums)
        stack_=[]
        dfs(stack_,map_)
        return res