class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n=len(books)
        @cache
        def dfs(i):
            if i==n:
                return 0
            
            cur_width=0
            max_height_on_cur_shelf=0
            min_total_height=float('inf')

            for j in range(i,n):
                book_w,book_h=books[j]

                cur_width+=book_w
                max_height_on_cur_shelf=max(max_height_on_cur_shelf,book_h)

                if cur_width>shelfWidth:
                    break
                
                cur_shelf_cost=max_height_on_cur_shelf+dfs(j+1)

                min_total_height=min(cur_shelf_cost,min_total_height)

            return min_total_height
            
        return dfs(0)