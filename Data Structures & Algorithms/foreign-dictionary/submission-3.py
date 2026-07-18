class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = {letter : set() for word in words for letter in word}
        # get all prerequisites
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i+1]) and words[i][j] == words[i+1][j]:
                j += 1
            if j == len(words[i+1]) and len(words[i]) > len(words[i+1]):
                return ""
            elif j == len(words[i]):
                continue
            else:
                letters[words[i+1][j]].add(words[i][j])

        ans = ""
        visited = set()
        # get the order of letters
        def dfs(path, letter):
            nonlocal ans
            if letter in path: # there is a cycle
                ans = ""
                return True # cycle found
            if letter in visited: # we've already been at this letter
                return False 
            path.add(letter)
            visited.add(letter)
            adj = letters[letter]
            for n in adj:
                if dfs(path, n):
                    return True
            ans += letter
            path.remove(letter)
        
        for letter in letters.keys():
            path = set()
            if dfs(path, letter):
                return ""

        return ans
