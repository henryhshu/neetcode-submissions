class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each treasure chest to all the land cells
        # do bfs starting from each treasure
        # iterate over all the grid values to find the treasures
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visit = set()
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        dist = 0
        while q:
            for _ in range(len(q)):
                # process the current cell
                i, j = q.popleft()
                grid[i][j] = dist
                for di, dj in directions:
                    newi = i + di
                    newj = j + dj
                    if (newi == ROWS or newj == COLS or 
                        newi < 0 or newj < 0 or
                        (newi, newj) in visit or
                        grid[newi][newj] == -1):
                        continue
                    q.append((newi, newj))
                    visit.add((newi, newj))
            dist += 1
                


                    

