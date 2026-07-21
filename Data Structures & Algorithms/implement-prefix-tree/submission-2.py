class PrefixTree:

    def __init__(self):
        self.root = [None] * 27

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not cur[index]:
                cur[index] = [None] * 27
            cur = cur[index]
        cur[-1] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not cur[index]:
                return False
            cur = cur[index]
        return cur[-1] == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if not cur[index]:
                return False
            cur = cur[index]
        return True