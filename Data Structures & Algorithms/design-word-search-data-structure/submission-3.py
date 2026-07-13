class WordDictionary:

    def __init__(self):
        self.root = [None] * 27

    def addWord(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if not cur[ord(letter) - ord('a')]:
                cur[ord(letter) - ord('a')] = [None] * 27
            cur = cur[ord(letter) - ord('a')]

        cur[-1] = True # mark as word

    def search(self, word: str) -> bool:
        def dfs(cur, index):
            if index >= len(word):
                return cur[-1]
            # wildcard case
            if word[index] == '.':
                for i in range(26):
                    if cur[i]:
                        res = dfs(cur[i], index + 1)
                        if res:
                            return True
                return False
            else:
                if cur[ord(word[index]) - ord('a')]:
                    return dfs(cur[ord(word[index]) - ord('a')], index + 1)
                else:
                    return False
    
        return False if not dfs(self.root, 0) else True
