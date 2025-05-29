class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False

        counter1=Counter(word1)
        counter2=Counter(word2)

        if set(word1)!=set(word2):
            return False
        
        if sorted(counter1.values())!=sorted(counter2.values()):
            return False
        
        return True
        
        
