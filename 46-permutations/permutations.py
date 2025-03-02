class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(list_,map_):
            if len(list_)==len(nums):
                res.append(list_.copy())
                return
            
            for i in range(len(nums)):
                if map_[i]==1:
                    continue
                map_[i]=1
                list_.append(nums[i])
                dfs(list_,map_)
                list_.pop()
                map_[i]=0
        
        res=[]
        map_=[0]*len(nums)
        dfs([],map_)
        return res