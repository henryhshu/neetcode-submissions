class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        row, col = [False] * R, [False] * C
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    row[r] = True
                    col[c] = True
        for r in range(R):
            for c in range(C):
                if row[r] or col[c]:
                    matrix[r][c] = 0
        