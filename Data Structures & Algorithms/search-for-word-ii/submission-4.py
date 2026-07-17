class Solution:
    class TrieNode:
        def __init__(self):
            self.arr = [None] * 26
            self.word = None
        def insertWord(self, word, index):
            if index == len(word):
                self.word = word
                return
            i = ord(word[index]) - ord('a')
            if not self.arr[i]:
                self.arr[i] = Solution.TrieNode()
            self.arr[i].insertWord(word, index + 1)
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # put all possible words into a trie and go through the words to look for them
        root = self.TrieNode()

        # insert words into trie
        for word in words:
            root.insertWord(word, 0)
        
        res = set()
        # search for the words at every index
        def dfs(visited, r, c, cur):
            if not cur or r < 0 or r>= len(board) or c < 0 or c >= len(board[0]) or (r, c) in visited:
                return
            cur = cur.arr[ord(board[r][c])-ord('a')]
            if cur and cur.word:
                res.add(cur.word)
            visited.add((r, c))
            dfs(visited, r-1, c, cur)
            dfs(visited, r+1, c, cur)
            dfs(visited, r, c-1, cur)
            dfs(visited, r, c+1, cur)
            visited.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = set()
                dfs(visited, r, c, root)
        
        
        return list(res)