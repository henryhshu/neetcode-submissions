class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        remaining = 0
        visiting = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    remaining += 1
                if grid[i][j] == 2:
                    visiting.append((i,j))
        
        while visiting:
            temp = deque()
            while visiting:
                x, y = visiting.pop()
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    remaining -= 1
                    temp.append((x-1, y))
                if x < n-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    remaining -= 1
                    temp.append((x+1, y))
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    remaining -= 1
                    temp.append((x, y-1))
                if y < m-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    remaining -= 1
                    temp.append((x, y+1))
            visiting = temp
            if visiting:
                res += 1

        return res if remaining == 0 else -1