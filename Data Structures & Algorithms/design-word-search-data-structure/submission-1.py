class WordDictionary:

    def __init__(self):
        self.root = [None] * 27

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if not cur[ord(letter) - ord('a')]:
                cur[ord(letter) - ord('a')] = [None] * 27
            cur = cur[ord(letter) - ord('a')]
        cur[-1] = True

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)
        

    def searchHelper(self, cur, suff) -> bool:
        if not suff and cur[-1]:
            return True
        if not suff:
            return False
        letter = suff[0]
        if letter == '.':
            for i in range(26):
                if cur[i] and self.searchHelper(cur[i], suff[1:]):
                    return True
            return False
        if cur[ord(letter) - ord('a')]:
            return self.searchHelper(cur[ord(letter) - ord('a')], suff[1:])
        return False
