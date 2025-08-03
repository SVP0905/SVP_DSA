class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        
        # Step 1: Create a prefix sum for the amounts for O(1) range queries.
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + fruits[i][1]

        def get_fruits_in_range(i, j):
            if i > j:
                return 0
            return prefix_sum[j + 1] - prefix_sum[i]

        max_fruits = 0
        left = 0

        # Step 2: Use a sliding window. 'right' expands, 'left' shrinks.
        for right in range(n):
            # The current window of fruits to consider is from index 'left' to 'right'
            left_pos = fruits[left][0]
            right_pos = fruits[right][0]

            # Calculate the minimum steps to harvest the entire [left, right] window.
            # This involves going to one end and then traversing to the other.
            # The optimal way is to go to the nearest end first, then cross the window.
            cost = min(abs(startPos - left_pos), abs(startPos - right_pos)) + (right_pos - left_pos)

            # Step 3: If the cost is too high, shrink the window from the left.
            # The 'while' loop ensures 'left' catches up to make the window valid.
            while cost > k and left <= right:
                left += 1
                if left > right:
                    break
                # Recalculate cost with the new 'left' position
                left_pos = fruits[left][0]
                cost = min(abs(startPos - left_pos), abs(startPos - right_pos)) + (right_pos - left_pos)
            
            # Step 4: This window [left, right] is valid. Update the max fruits.
            current_fruits = get_fruits_in_range(left, right)
            max_fruits = max(max_fruits, current_fruits)

        return max_fruits
        