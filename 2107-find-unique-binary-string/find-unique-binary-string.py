class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        nums=set(nums)
        def dfs(str_):
            if len(str_)==n:
                if str_ not in nums:
                    return str_
                return ''
            
            left=dfs(str_+'0')
            right=dfs(str_+'1')

            if left:
                return left
            else:
                return right
        
        return dfs('')
