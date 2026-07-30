class Solution:
    def minimumPushes(self, word: str) -> int:
        # most_common() with no argument returns all items sorted by count, highest first. If you only want the top N, pass a number: freq.most_common(3).
        sorted_freq=Counter(word).most_common()
        print(sorted_freq)

        # Using sorted() (more control):
        # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # If you want a dict back (not a list of tuples):
        # sorted_dict = dict(freq.most_common())


        # Note on ties: Both methods keep equal-frequency elements in the order they first appeared in the original data (insertion order) — they don't sort ties alphabetically or anything like that. If you want a secondary sort (e.g., alphabetical for ties), you can do:
        # sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))


        res=0
        placed=0
        for ch,freq in sorted_freq:
            if placed<8:
                cost=1
            elif placed<16:
                cost=2
            elif placed<24:
                cost=3
            else:
                cost=4
            
            res+=(freq*cost)
            placed+=1
        
        return res

            
        