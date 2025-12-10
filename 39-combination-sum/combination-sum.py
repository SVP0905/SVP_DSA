class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(start_idx,path):
            if sum(path)==target:
                res.append(path.copy())
                return
            
            for i in range(start_idx,len(candidates)):
                if candidates[i]+sum(path)>target:
                    return
                path.append(candidates[i])
                dfs(i,path)
                path.pop()
        
        dfs(0,[])

        return res
