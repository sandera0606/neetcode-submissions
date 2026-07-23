class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited, r, c, ind):
            if ind >= len(word):
                return True
            if (r, c) in visited or not(0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != word[ind]:
                return False
            visited.add((r, c))
            res = dfs(visited, r+1, c, ind+1) or dfs(visited, r-1, c, ind+1) or dfs(visited, r, c+1, ind+1) or dfs(visited, r, c-1, ind+1)
            visited.remove((r, c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r, c))
                    if dfs(visited, r+1, c, 1) or dfs(visited, r-1, c, 1) or dfs(visited, r, c+1, 1) or dfs(visited, r, c-1, 1):
                        return True
        return False