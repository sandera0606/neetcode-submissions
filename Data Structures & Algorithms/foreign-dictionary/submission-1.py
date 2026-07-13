class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # similar to course prerequisite question
        pre = defaultdict(set) # letter : set() <- where the set is everything lexicographically before it
        letters = set(char for w in words for char in w)

        # 1. get rules (directed graph!)
        for i in range(len(words) - 1):
            # get the words that are adjacent to each other
            a = words[i]
            b = words[i+1]

            # find the first different letter
            j = 0
            smaller = min(len(a), len(b))
            while j < smaller:
                if a[j] != b[j]:
                    break
                j += 1

            if j >= smaller and len(a) != smaller:
                return "" # impossible
            elif j < smaller: # gives us prerequisite info
                pre[b[j]].add(a[j])
            # otherwise it doesn't give us any new information

        order = ""
        visited = {letter : False for letter in letters}
        # 2. check if cycles exist. if cycle exist, then bad. 
        # otherwise, how to figure out the order?? 
        # idea: dfs on each, while marking which ones have been visited, so that it's in order
        # go through the list so you can "print in any order" if there 2 two subgraphs

        def dfs(path, letter):
            nonlocal order
            if visited[letter]:
                return True
            if letter in path:
                return False # invalid (cycle)
        
            path.add(letter)
            for p in pre[letter]:
                if not dfs(path, p):
                    return False
            pre[letter] = set()
            path.remove(letter)
            visited[letter] = True
            order += letter
            return True

        for letter in letters:
            if visited[letter]:
                continue
            else:
                path = set()
                if dfs(path, letter) == False:
                    return ""
        
        return order

