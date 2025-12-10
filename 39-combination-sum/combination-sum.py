class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,path):
            if i>=len(candidates) or sum(path)>target:
                return
            
            if sum(path)==target:
                res.append(path.copy())
                return
            
            for j in range(i,len(candidates)):
                if sum(path)+candidates[j]>target:
                    break
                path.append(candidates[j])
                dfs(j,path)
                path.pop()
        
        dfs(0,[])
        return res
