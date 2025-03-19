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
                        map_[i]=0
                        stack.pop()
        
        res=[]
        map_=[0]*len(nums)
        stack=[]
        permute(stack,map_)
        return res
