class WordDictionary:

    def __init__(self):
        self.root = [None] * 27

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not cur[index]:
                cur[index] = [None] * 27
            cur = cur[index]
        cur[-1] = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
        
    def dfs(self, node, word, index):
        if index >= len(word):
            return node[-1] == True
        if word[index] == ".":
            for i in range(26):
                nxt = node[i]
                if nxt and self.dfs(nxt, word, index + 1):
                    return True
            return False
        else:
            i = ord(word[index]) - ord('a')
            if not node[i]:
                return False
            return self.dfs(node[i], word, index + 1)