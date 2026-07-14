class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited, index, r, c):
            if index == len(word):
                return True
            if (r, c) in visited or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index]:
                return False
            
            visited.add((r, c))
            res = dfs(visited, index + 1, r + 1, c) or dfs(visited, index + 1, r - 1, c) or dfs(visited, index + 1, r, c + 1) or dfs(visited, index + 1, r, c-1)
            visited.remove((r, c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                if dfs(visited, 0, r, c):
                    return True
        return False