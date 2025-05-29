class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)

        list_count=list(counter.values())
        
        return len(list_count)==len(set(list_count))