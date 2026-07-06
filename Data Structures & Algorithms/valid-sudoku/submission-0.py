class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                rs = r // 3
                cs = c // 3
                if board[r][c] in squares[(rs, cs)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(rs, cs)].add(board[r][c])
        return True