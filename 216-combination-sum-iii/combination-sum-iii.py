class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i,target,list_):
            if target==0 and len(list_)==k:
                res.append(list_.copy())
                return
            if target<0 or len(list_)>k or i>9:
                return
            list_.append(i)
            dfs(i+1,target-i,list_)
            list_.pop()
            dfs(i+1,target,list_)

        res=[]
        dfs(1,n,[])
        return res