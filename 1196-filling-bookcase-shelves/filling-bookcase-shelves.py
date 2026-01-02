class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[float('inf')]*(n+1)

        dp[n]=0


        for i in range(n-1,-1,-1):
            cur_width=0
            max_height_on_cur_shelf=0
            for j in range(i,n):
                book_w,book_h=books[j]

                cur_width+=book_w
                max_height_on_cur_shelf=max(max_height_on_cur_shelf,book_h)

                if cur_width>shelfWidth:
                    break
                
                dp[i]=min(dp[i],max_height_on_cur_shelf+dp[j+1])

                
        
        return dp[0]


