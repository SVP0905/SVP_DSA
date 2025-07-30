class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        vals=counter.values()

        return len(vals)==len(set(vals))