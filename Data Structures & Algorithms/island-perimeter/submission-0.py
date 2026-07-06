class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # find the 1s
        # perform dfs
        # keep track of visited indices
        # count perimeter
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def dfs(i, j):
            # out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 1
            # hit water
            if grid[i][j] == 0:
                return 1
            if (i, j) in visit:
                return 0
            visit.add((i, j))
            perim = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)
            return perim
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
            
            