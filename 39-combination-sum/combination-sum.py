class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def dfs(i,target,list_):
            if target==0:
                res.append(list_.copy())
                return
            if target<0 or i>=n:
                return
            
            list_.append(candidates[i])
            dfs(i,target-candidates[i],list_)
            list_.pop()

            dfs(i+1,target,list_)
        
        res=[]
        dfs(0,target,[])

        return res