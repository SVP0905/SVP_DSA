class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def dfs(i,arr):
            if i>=len(nums):
                subs.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()
            dfs(i+1,arr)
        
        subs=[]
        dfs(0,[])

        max_=0
        for sub in subs:
            if not sub:
                continue
            cur=0
            for n in sub:
                cur|=n
            max_=max(max_,cur)
        
        cnt=0
        for sub in subs:
            if not sub:
                continue
            cur=0
            for n in sub:
                cur|=n
            if cur==max_:
                cnt+=1
        return cnt