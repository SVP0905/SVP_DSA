class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)

        list_counter=list(counter.values())

        return len(list_counter)==len(set(list_counter))