class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit=0
        for n in nums:
            max_bit=max_bit|n
        
        # cnt=0
        def dfs(i,arr):
            # nonlocal cnt
            if i>=len(nums):
                if not arr:
                    return 0
                cur=0
                for n in arr:
                    cur=cur|n
                if cur==max_bit:
                    return 1
                return 0
            left,right=0,0
            arr.append(nums[i])
            left+=dfs(i+1,arr)
            arr.pop()
            right+=dfs(i+1,arr)

            return left+right

        subs=[]
        return dfs(0,[])

        # return cnt