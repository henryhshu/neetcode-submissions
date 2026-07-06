class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        # define prefix summed matrix
        self.matsum = [[0] * (COL+1) for _ in range(ROW+1)]
        # calculate the matsum
        for i in range(1, ROW+1):
            for j in range(1, COL+1):
                # prefix sum = current cell in matrix + left cell + above cell - overlapping cell
                self.matsum[i][j] = matrix[i-1][j-1] + self.matsum[i][j-1] + self.matsum[i-1][j] - self.matsum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # update the indexing pattern to the prefix summed matrix
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        # sum = bottom left - top section - left section + overlapping section
        res = self.matsum[r2][c2] - self.matsum[r1-1][c2] - self.matsum[r2][c1-1] + self.matsum[r1-1][c1-1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)