class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set=set(wordDict)

        @cache
        def dfs(start_i):
            if start_i==len(s):
                return True
            


            for j in range(start_i,len(s)):
                chunk=s[start_i:j+1]
                if chunk in word_set:
                    if dfs(j+1):
                        return True
            
            return False

        return dfs(0)
