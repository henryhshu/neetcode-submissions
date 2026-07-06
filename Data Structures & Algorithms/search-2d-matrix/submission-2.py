class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def binary_search(arr: List, target: int) -> int:
            r = len(arr)
            l = 0
            while r>=l:
                m = (r+l)//2
                if target >= arr[m]:
                    if m+1 == len(arr):
                        return m
                    elif arr[m+1] > target:
                        return m
                    else:
                        l = m + 1
                if target < arr[m]:
                    r = m - 1
            return m

        first_column = [row[0] for row in matrix]
        target_row = binary_search(first_column, target)
        candidate_index = binary_search(matrix[target_row], target)
        return target == matrix[target_row][candidate_index]

                