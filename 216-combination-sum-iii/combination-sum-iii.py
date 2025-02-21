class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i,target,list_):
            if target==0 and len(list_)==k:
                res.append(list_.copy())
                return 
            if target<0 or len(list_)>k or i>9:
                return
            
            for j in range(i,10):
                list_.append(j)
                dfs(j+1,target-j,list_)
                list_.pop()
        
        res=[]
        dfs(1,n,[])
        return res