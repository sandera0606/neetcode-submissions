class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        res = []
        i = 0

        for s in strs:
            cur = [0] * 26
            for letter in s:
                cur[ord(letter) - ord('a')] += 1
            curTuple = tuple(cur)
            if curTuple not in anagramDict:
                res.append([s])
                anagramDict[curTuple] = i
                i += 1
            else:
                res[anagramDict[curTuple]].append(s)
        return res