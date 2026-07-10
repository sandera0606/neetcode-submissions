class TrieNode:
    def __init__(self):
        self.arr = [None] * 26
        self.index = -1 #-1 indicates not a word, non -1 indicates is a word.

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, index, word):
        cur = self.root
        for letter in word:
            if not cur.arr[ord(letter) - ord('a')]:
                cur.arr[ord(letter) - ord('a')] = TrieNode()
            cur = cur.arr[ord(letter) - ord('a')]
        cur.index = index
    
    def search(self, word): # returns the index of the word
        cur = self.root
        for letter in word:
            if not cur.arr[ord(letter) - ord('a')]:
                return -1
            cur = cur.arr[ord(letter) - ord('a')]
        return cur.index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. build a trie from the words
        myTrie = Trie()
        for i, word in enumerate(words):
            myTrie.insert(i, word)
        # 2. search all possible word combos in grid
        res = []
        def dfs(visited, trieNode, i, j):
            # null or i, j out of bounds
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visited:
                return
            trieNode = trieNode.arr[ord(board[i][j])-ord('a')]
            if not trieNode:
                return
            visited.add((i, j))
            if trieNode.index != -1:
                # is a word
                res.append(words[trieNode.index])
                trieNode.index = -1
            # i, j-1
            dfs(visited.copy(), trieNode, i, j-1)
            # i, j+1
            dfs(visited.copy(), trieNode, i, j+1)
            # i-1, j
            dfs(visited.copy(), trieNode, i-1, j)
            # i+1, j
            dfs(visited.copy(), trieNode, i+1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                dfs(visited, myTrie.root, i, j)
        return res
            