class Solution:
    def reverseWords(self, s: str) -> str:
        # words=s.split()
        # return ' '.join(reversed(words))

        words=[]
        word=''

        for char in s:
            if char!=' ':
                word+=char
            elif word:
                words.append(word)
                word=''
        
        if word:
            words.append(word)
            
        return ' '.join(reversed(words))