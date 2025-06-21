class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq=Counter(word)
        freq_values=list(freq.values())
        freq_values.sort()

        min_del=float('inf')

        for f in range(freq_values[0],freq_values[-1]+1):
            deletions=0
            for val in freq_values:
                if val<f:
                    deletions+=val
                elif val>f+k:
                    deletions+=val-(f+k)
            
            min_del=min(min_del,deletions)
        return min_del
