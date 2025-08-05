class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        left = 0
        max_picked = 0

        # Use 'right' to expand the window
        for right in range(len(fruits)):
            fruit_type = fruits[right]
            baskets[fruit_type] += 1

            # If we have more than 2 types of fruit, shrink the window
            while len(baskets) > 2:
                left_fruit_type = fruits[left]
                baskets[left_fruit_type] -= 1
                
                # If a fruit count drops to 0, remove it from our baskets
                if baskets[left_fruit_type] == 0:
                    del baskets[left_fruit_type]
                
                # Move the left pointer to shrink the window
                left += 1

            # Update the maximum number of fruits picked so far
            max_picked = max(max_picked, right - left + 1)
            
        return max_picked
            