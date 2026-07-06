class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # brute force is to find the first letter then iterate
        roots = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    roots.append([i, j])

        def dfs(coord, i, visited):
            if i == len(word):
                return True
            if coord[0] >= len(board) or coord[0] < 0:
                return False
            if coord[1] >= len(board[0]) or coord[1] < 0:
                return False
            if word[i] == board[coord[0]][coord[1]] and coord not in visited:
                print(coord)
                left = [coord[0]-1, coord[1]]
                right = [coord[0]+1, coord[1]]
                up = [coord[0], coord[1]+1]
                down = [coord[0], coord[1]-1]
                visited.append(coord)
                return dfs(left, i+1, visited.copy()) or dfs(right, i+1, visited.copy()) or dfs(up, i+1, visited.copy()) or dfs(down, i+1, visited.copy())
            return False

        for root in roots:
            # print(root)
            if dfs(root, 0, []):
                return True
        return False
        


        