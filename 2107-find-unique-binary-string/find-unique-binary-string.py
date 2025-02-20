class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        num=set(nums)
        def dfs(str_):
            if len(str_)==n:
                if str_ not in nums:
                    res.append(str_)
                    return True
                else:
                    return False
            
            addzeros=dfs(str_+'0')
            if addzeros:
                return True
            addones=dfs(str_+'1')
            if addones:
                return True

        res=[]
        if dfs(''):
            return ''.join(res)
