class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        res=[]
        def dfs(i,cur_s):
            if i>=len(digits):
                res.append(cur_s)
                return
            
            cur_set=map_[digits[i]]

            for ch in cur_set:
                dfs(i+1,cur_s+ch)

        dfs(0,'')
        return res