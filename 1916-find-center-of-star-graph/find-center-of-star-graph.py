class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        A_u=edges[0][0]
        A_v=edges[0][1]

        B_u=edges[1][0]
        B_v=edges[1][1]

        if A_u==B_u or A_u==B_v:
            return A_u
        else:
            return A_v
            