class Solution:
    def isValid(self, word: str) -> bool:
        pattern = r'^(?=.*[aeiouAEIOU])(?=.*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])[a-zA-Z0-9]{3,}$'
        return bool(re.match(pattern,word))