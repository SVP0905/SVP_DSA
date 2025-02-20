class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        nums=set(nums)
        def dfs(str_):
            if len(str_)==n:
                if str_ not in nums:
                    res.append(str_)
                    return True
                else:
                    return False
            
            if dfs(str_+'0'):
                return True
            if dfs(str_+'1'):
                return True

        res=[]
        if dfs(''):
            return ''.join(res)
