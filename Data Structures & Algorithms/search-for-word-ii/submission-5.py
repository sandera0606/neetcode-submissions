class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make words into a trie and keep traversing it
        root = [None] * 27

        for word in words:
            cur = root
            for letter in word:
                if not cur[ord(letter) - ord('a')]:
                    cur[ord(letter) - ord('a')] = [None] * 27
                cur = cur[ord(letter) - ord('a')] 
            cur[-1] = word # is a word
        
        answer = set()
        
        # helper function to traverse board
        def traverse(visited, node, r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if (r, c) in visited:
                return
            if not node[ord(board[r][c]) - ord('a')]:
                return
            node = node[ord(board[r][c]) - ord('a')]
            if node[-1] != None:
                answer.add(node[-1])
            visited.add((r, c))
            traverse(visited, node, r+1, c)
            traverse(visited, node, r-1, c)
            traverse(visited, node, r, c+1)
            traverse(visited, node, r, c-1)
            visited.remove((r, c))
            

        # traverse board
        for r in range(len(board)):
            for c in range(len(board[0])):
                traverse(set(), root, r, c)

        return list(answer)