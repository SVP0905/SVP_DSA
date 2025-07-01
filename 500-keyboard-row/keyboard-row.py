class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")
        res=[]

        for word in words:
            word_chars=set(word.lower())
            if word_chars.issubset(first_row):
                res.append(word)
            if word_chars.issubset(second_row):
                res.append(word)
            if word_chars.issubset(third_row):
                res.append(word)
        return res