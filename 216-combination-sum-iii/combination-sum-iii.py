class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        nums=[i for i in range(1,10)]

        def dfs(start_idx,path):
            if len(path)==k and sum(path)==n:
                res.append(path.copy())
                return
            

            for i in range(start_idx,len(nums)):
                if nums[i]+sum(path)>n:
                    break
                
                if i>start_idx and nums[i]==nums[i-1]:
                    continue

                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        
        dfs(0,[])

        return res

            
