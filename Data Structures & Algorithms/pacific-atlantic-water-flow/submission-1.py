class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # water can flow into the ocean as long as one of it's coordinates is bordering the ocean
        # must be able to flow into both the top/left and bottom/right
        # need a way to determine if both pacific and atlantic has been reached

        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or r > ROW-1 or c < 0 or c > COL-1 or 
                heights[r][c] < prevHeight):
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        res = []
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL-1, atl, heights[r][COL-1])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW-1, c, atl, heights[ROW-1][c])
        
        res = []
        for coord in pac:
            if coord in atl:
                res.append(list(coord))

        return res

