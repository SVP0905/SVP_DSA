class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        def dfs(i,target,list_):
            if target==0:
                res.append(list_.copy())
                return
            if target<0 or i>=n:
                return
            list_.append(candidates[i])
            # take the current element 
            dfs(i+1,target-candidates[i],list_)
            list_.pop()

            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1

            #don't take the current element
            dfs(i+1,target,list_)
        
        res=[]
        dfs(0,target,[])
        return res