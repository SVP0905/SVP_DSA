class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        word = [''] * n
        curr_char = 'a'
        
        # --- Step 1: Greedy Construction ---
        for i in range(n):
            if word[i] == '':
                # If we've run out of alphabet letters, it's impossible
                if curr_char > 'z':
                    return ""
                
                # Assign this character to index i and all related indices
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        # If j already has a different char, the LCP matrix is contradictory
                        if word[j] != '' and word[j] != curr_char:
                            return ""
                        word[j] = curr_char
                
                # Move to the next lexicographical character
                curr_char = chr(ord(curr_char) + 1)
                
        # --- Step 2: LCP Matrix Validation ---
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                if word[i] == word[j]:
                    # Base case: last row/column
                    if i == n - 1 or j == n - 1:
                        expected_lcp = 1
                    else:
                        expected_lcp = 1 + lcp[i + 1][j + 1]
                else:
                    expected_lcp = 0
                
                # If our calculated expectation doesn't match the input matrix
                if lcp[i][j] != expected_lcp:
                    return ""
                    
        return "".join(word)

        