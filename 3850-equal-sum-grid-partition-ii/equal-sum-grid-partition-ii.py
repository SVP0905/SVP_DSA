class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        # --- CHECK HORIZONTAL CUTS ---
        top_sum = 0
        top_set = set()
        
        # Pre-count values for the bottom section
        bot_val_counts = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                bot_val_counts[val] = bot_val_counts.get(val, 0) + 1

        for r in range(m - 1): # For each horizontal cut
            # 1. Update sums and sets as we move the cut line down
            row_total = 0
            for c in range(n):
                val = grid[r][c]
                top_set.add(val)
                row_total += val
                # Remove current row's values from the bottom's available pool
                bot_val_counts[val] -= 1
                if bot_val_counts[val] == 0:
                    del bot_val_counts[val]
            
            top_sum += row_total
            bot_sum = total_sum - top_sum
            diff = top_sum - bot_sum
            
            # Case: Perfect split
            if diff == 0: return True
            
            # Case: Need to remove from TOP (diff > 0)
            if diff > 0:
                target = diff
                if target in top_set:
                    # Connectivity Rule: 2D block OR end of 1D strip
                    h, w = (r + 1), n
                    if (h > 1 and w > 1) or (h == 1 and (grid[r][0] == target or grid[r][n-1] == target)) or (w == 1 and (grid[0][0] == target or grid[r][0] == target)):
                        return True
            
            # Case: Need to remove from BOTTOM (diff < 0)
            elif diff < 0:
                target = -diff
                if target in bot_val_counts:
                    h, w = (m - 1 - r), n
                    if (h > 1 and w > 1) or (h == 1 and (grid[r+1][0] == target or grid[r+1][n-1] == target)) or (w == 1 and (grid[r+1][0] == target or grid[m-1][0] == target)):
                        return True

        # --- CHECK VERTICAL CUTS ---
        left_sum = 0
        left_set = set()
        
        # Pre-count values for the right section
        right_val_counts = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                right_val_counts[val] = right_val_counts.get(val, 0) + 1

        for c in range(n - 1): # For each vertical cut
            col_total = 0
            for r in range(m):
                val = grid[r][c]
                left_set.add(val)
                col_total += val
                right_val_counts[val] -= 1
                if right_val_counts[val] == 0:
                    del right_val_counts[val]
            
            left_sum += col_total
            right_sum = total_sum - left_sum
            diff = left_sum - right_sum

            if diff == 0: return True
            
            # Case: Need to remove from LEFT (diff > 0)
            if diff > 0:
                target = diff
                if target in left_set:
                    h, w = m, (c + 1)
                    if (h > 1 and w > 1) or (h == 1 and (grid[0][0] == target or grid[0][c] == target)) or (w == 1 and (grid[0][c] == target or grid[m-1][c] == target)):
                        return True
            
            # Case: Need to remove from RIGHT (diff < 0)
            elif diff < 0:
                target = -diff
                if target in right_val_counts:
                    h, w = m, (n - 1 - c)
                    if (h > 1 and w > 1) or (h == 1 and (grid[0][c+1] == target or grid[0][n-1] == target)) or (w == 1 and (grid[0][c+1] == target or grid[m-1][c+1] == target)):
                        return True

        return False
            
            
                    
        
            
            
                    
        