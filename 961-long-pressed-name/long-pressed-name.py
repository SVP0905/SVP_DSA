class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0
        m,n=len(name),len(typed)
        while i<m and j<n:
            if name[i]==typed[j]:
                i+=1
                j+=1
            elif j>0 and typed[j]==typed[j-1]:
                j+=1
            else:
                return False

        
        if i<m:
            return False
        
        while j<n:
            if typed[j]!=typed[j-1]:
                return False
            j+=1
        return True
        
        