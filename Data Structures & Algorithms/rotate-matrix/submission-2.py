class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # treat the matrix like a nested rings of matrices
        # update the matrix from outside to inside recursively
        # base case is one or nothing in the matrix
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                  top, bottom = l, r
                  topleft = matrix[top][l+i]
                  matrix[top][l+i] = matrix[bottom-i][l]
                  matrix[bottom-i][l] = matrix[bottom][r-i]
                  matrix[bottom][r-i] = matrix[top+i][r]
                  matrix[top+i][r] = topleft
            l += 1
            r -= 1


