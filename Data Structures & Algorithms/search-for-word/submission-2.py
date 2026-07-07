class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. search for first letter
        # 2. search for neighbouring letters . do not visit same letter twice (keep visited coords)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if self.connected(board, word, [[i, j]]):
                        return True
        return False

    def connected(self, board, word, visited):
        cur = visited[-1]
        letters = len(visited)
        if letters == len(word):
            return True

        # possible 4 next coords. explore only if OK.
        top = [cur[0] + 1, cur[1]]
        if top[0] < len(board) and top not in visited and board[top[0]][top[1]] == word[letters]:
            if self.connected(board, word, visited + [top]):
                return True
                
        bottom = [cur[0] - 1, cur[1]]
        if bottom[0] >= 0 and bottom not in visited and board[bottom[0]][bottom[1]] == word[letters]:
            if self.connected(board, word, visited + [bottom]):
                return True

        left = [cur[0], cur[1] - 1]
        if left[1] >= 0 and left not in visited and board[left[0]][left[1]] == word[letters]:
            if self.connected(board, word, visited + [left]):
                return True
                
        right = [cur[0], cur[1] + 1]
        if right[1] < len(board[0]) and right not in visited and board[right[0]][right[1]] == word[letters]:
            if self.connected(board, word, visited + [right]):
                return True
    
        return False