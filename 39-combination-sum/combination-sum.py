class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,sum_,arr):
            if sum_==target:
                res.append(arr.copy())
                return
            
            if sum_>target or i>=len(candidates):
                return
            
            arr.append(candidates[i])
            dfs(i,sum_+candidates[i],arr)

            arr.pop()
            dfs(i+1,sum_,arr)
        
        dfs(0,0,[])

        return res