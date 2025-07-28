class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit=0
        for n in nums:
            max_bit=max_bit|n
        
        cnt=0
        def dfs(i,arr):
            nonlocal cnt
            if i>=len(nums):
                if not arr:
                    return
                cur=0
                for n in arr:
                    cur=cur|n
                if cur==max_bit:
                    cnt+=1
                return
            
            arr.append(nums[i])
            dfs(i+1,arr)
            arr.pop()
            dfs(i+1,arr)
        subs=[]
        dfs(0,[])

        return cnt