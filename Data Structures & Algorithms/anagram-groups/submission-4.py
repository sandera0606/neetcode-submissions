class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # empty list by default

        for string in strs:
            # turn each string into a list of characters
            freqs = [0] * 26
            for c in string: 
                freqs[ord(c) - ord('a')] += 1
            result[tuple(freqs)].append(string) # don't need to check if it is in it or not because defaultdict

        return list(result.values())