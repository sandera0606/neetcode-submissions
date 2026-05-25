class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            cur = [0] * 26
            for char in word:
                cur[ord(char) - ord('a')] += 1
            key = tuple(cur)
            if key not in seen.keys():
                seen[key] = []
            seen[key].append(word)
        
        return list(seen.values())
        