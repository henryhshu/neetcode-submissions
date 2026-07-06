class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        def capture(r,c):
            if r<0 or c<0 or r==ROW or c==COL or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        #run capture dfs on all non bordering
        for r in range(ROW):
            for c in range(COL):
                if r == ROW-1 or c == COL-1 or r == 0 or c == 0:
                    capture(r,c)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"