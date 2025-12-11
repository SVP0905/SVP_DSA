class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        info=[False]*len(nums)
        def dfs(depth,path):
            if depth==len(nums):
                res.append(path.copy())
                return
            

            for i in range(len(nums)):
                if not info[i]:
                    path.append(nums[i])
                    info[i]=True
                    dfs(depth+1,path)
                    path.pop()
                    info[i]=False
        
        dfs(0,[])

        return res
