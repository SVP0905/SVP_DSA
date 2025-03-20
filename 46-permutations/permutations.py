class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute(stack,map_):
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
                        permute(stack,map_)
                        stack.pop()
                        map_[i]=0
        
        res=[]
        stack=[]
        map_=[0]*len(nums)
        permute(stack,map_)
        return res