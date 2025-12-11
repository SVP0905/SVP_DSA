class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=[False]*len(nums)
        def dfs(depth,path):
            if depth==len(nums):
                res.append(path.copy())
                return
            

            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i]=True
                    dfs(depth+1,path)
                    path.pop()
                    visited[i]=False
        
        dfs(0,[])

        return res
