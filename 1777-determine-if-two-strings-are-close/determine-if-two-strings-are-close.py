class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        counter1=Counter(word1)
        counter2=Counter(word2)
        vals1=sorted(counter1.values())
        vals2=sorted(counter2.values())

        if set(word1)!=set(word2):
            return False
        
        for i in range(len(vals1)):
            if vals1[i]!=vals2[i]:
                return False
        return True