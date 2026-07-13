class PrefixTree:

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if not cur[ord(letter) - ord('a')]:
                cur[ord(letter) - ord('a')] = [None] * 27
            cur = cur[ord(letter) - ord('a')]
        cur[-1] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if cur[ord(letter) - ord('a')]:
                cur = cur[ord(letter) - ord('a')]
            else:
                return False
        return cur[-1] == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if cur[ord(letter) - ord('a')]:
                cur = cur[ord(letter) - ord('a')]
            else:
                return False
        return True
        