class Solution:
    def coloredCells(self, n: int) -> int:
        blue_cells=1
        addend=4
        while n-1:
            blue_cells+=addend
            addend+=4
            n-=1
        return blue_cells