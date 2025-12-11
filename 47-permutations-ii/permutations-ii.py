class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        visited=[False]*len(nums)
        

        def dfs(depth,path):
            if depth==len(nums):
                res.append(path.copy())
                return
            
            i=0
            while i<len(nums):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i]=True
                    dfs(depth+1,path)
                    path.pop()
                    visited[i]=False

                while i+1<len(nums) and nums[i]==nums[i+1] and not visited[i]:
                    i+=1
                i+=1
        
        dfs(0,[])
        return res