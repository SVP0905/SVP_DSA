class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(start_idx,path):
            if sum(path)==target:
                res.append(path.copy())
                return
            
            i=start_idx
            while i<len(candidates):
                if candidates[i]+sum(path)>target:
                    return
                
                path.append(candidates[i])
                dfs(i+1,path)
                path.pop()
                while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                    i+=1
                i+=1
        
        dfs(0,[])
        return res