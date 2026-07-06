class PrefixTree:

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if not cur[ord(letter) - ord('a')]:
                cur[ord(letter) - ord('a')] = [None] * 27
            cur = cur[ord(letter) - ord('a')]

        cur[-1] = True # word 

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if not cur[ord(letter) - ord('a')]:
                return False
            cur = cur[ord(letter) - ord('a')]
        return cur[-1] if cur[-1] else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if not cur[ord(letter) - ord('a')]:
                return False
            cur = cur[ord(letter) - ord('a')]
        return True
        