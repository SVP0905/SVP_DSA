class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(start_idx,path):
            if sum(path)==target:
                res.append(path.copy())
                return
            
            for i in range(start_idx,len(candidates)):
                    
                if candidates[i]+sum(path)>target:
                    return

                if i>start_idx and candidates[i]==candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                dfs(i+1,path)
                path.pop()

        
        dfs(0,[])
        return res