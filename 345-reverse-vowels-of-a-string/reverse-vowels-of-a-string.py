class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}

        l,r=0,len(s)-1
        arr=[ch for ch in s]
        while l<r:
            if arr[l] in vowels and arr[r] in vowels:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            
            if arr[l] not in vowels:
                l+=1
            if arr[r] not in vowels:
                r-=1
        
        return ''.join(arr)
