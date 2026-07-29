class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set([letter for word in words for letter in word])
        pre = defaultdict(set)
        # get ordering by graph nodes 
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i+1]
            bLen = len(b)
            i = 0
            while i < len(a):
                if i >= bLen:
                    return ""
                if a[i] != b[i]:
                    break
                i += 1
            if i == len(a):
                continue
            # first differing letter
            pre[b[i]].add(a[i])
        
        res = ""
        visited = set()
        def dfs(path, letter):
            nonlocal res
            if letter in path:
                return False
            if letter in visited:
                return True
            path.add(letter)
            for p in pre[letter]:
                if not dfs(path, p):
                    return False
            res += letter
            visited.add(letter)
            path.remove(letter)
            return True
        
        for letter in letters:
            if not dfs(set(), letter):
                return ""
    
        return res